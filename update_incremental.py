#!/usr/bin/env python3
"""Incremental update for docs.copilotkit.ai: crawl only NEW docs.
Usage:
  python3 update_incremental.py --check-only
  python3 update_incremental.py
  python3 update_incremental.py --force URL
"""
import argparse, json, re, pathlib, asyncio, sys
from urllib.parse import urlparse, urljoin, urldefrag
sys.path.insert(0, "/data/opencode/copilotkit")
import crawl_copilotkit as C

DOCS = C.OUT_ROOT
STATE = pathlib.Path("/data/opencode/copilotkit/crawl_state.json")

async def live_sitemaps():
    import httpx
    out = {}
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        r = await c.get("https://docs.copilotkit.ai/sitemap.xml", timeout=30); r.raise_for_status()
        locs = re.findall(r"<loc>([^<]+)</loc>", r.text)
        out["docs"] = sorted({C.normalize_url(u) for u in locs if C.normalize_url(u)})
    return out

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--force", default=None)
    ap.add_argument("--concurrency", type=int, default=10)
    a = ap.parse_args()
    idx = [json.loads(l) for l in open(DOCS / "_index.jsonl")] if (DOCS / "_index.jsonl").exists() else []
    indexed = set(r["url"] for r in idx)
    from urllib.parse import unquote
    idec = {unquote(u) for u in indexed}
    live = await live_sitemaps()
    new = {}
    for k, urls in live.items():
        miss = [u for u in urls if u not in indexed and unquote(u) not in idec and ".json" not in u and "`" not in u]
        new[k] = miss
        print(f"{k}: live={len(urls)} indexed~{len(indexed)} new={len(miss)}")
        for u in miss[:20]: print(f"  NEW: {u}")
    targets = [a.force] if a.force else [u for v in new.values() for u in v]
    if a.check_only or not targets:
        print("check-only" if a.check_only else "no new docs — up to date")
        return
    print(f"fetching {len(targets)} new docs...")
    st = json.load(open(STATE)) if STATE.exists() else {"visited": {}, "failed": {}}
    vs, failed = st.get("visited", {}), st.get("failed", {})
    from datetime import datetime, timezone
    idx_f = open(DOCS / "_index.jsonl", "a", encoding="utf-8")
    sem = asyncio.Semaphore(a.concurrency)
    ok = fail = 0
    async def one(url):
        nonlocal ok, fail
        async with sem:
            try:
                data = await C.fetch_one(url)
                rel = C.url_to_relpath(url); fp = DOCS / rel
                fp.parent.mkdir(parents=True, exist_ok=True)
                fm = f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n---\n\n"
                fp.write_text(fm + data["markdown"], encoding="utf-8")
                mr = pathlib.Path("_meta") / rel.with_suffix(".json")
                (DOCS / mr).parent.mkdir(parents=True, exist_ok=True)
                (DOCS / mr).write_text(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}, indent=2))
                vs[url] = {"file": str(rel), "title": data["title"], "method": data["method"]}
                idx_f.write(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
                ok += 1; print(f"[new] {url}")
            except Exception as e:
                failed[url] = str(e)[:300]; fail += 1; print(f"[fail] {url}: {e}")
    await asyncio.gather(*(one(u) for u in targets))
    idx_f.close()
    try:
        if C._crawler is not None: await C._crawler.close()
    except Exception: pass
    open(STATE, "w").write(json.dumps({"visited": vs, "failed": failed}))
    print(f"done: ok={ok} fail={fail}")

if __name__ == "__main__":
    asyncio.run(main())
