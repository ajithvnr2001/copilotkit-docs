# CopilotKit Docs — End-to-End Crawler

Crawls **https://docs.copilotkit.ai/** completely (sitemap + `llms.txt` + subdomains) and saves clean markdown docs. Three stacks combined: **Scrapling** (fast fetch) → **Crawl4AI** (JS fallback) → **ScrapeGraphAI** (HTML→MD, local, no LLM key needed).

## Results (verified)

> Last verified: 2026-10-10 — see `docs/_last_verified.json` (rewritten daily by GitHub Actions).

| Scope | Coverage |
|---|---|
| docs `sitemap.xml` | 3992/3993 = 99.97% (1 origin-500, curl-confirmed) |
| Total | **4,552 files / 4,554 urls, ~99M** (+27 subdomain pages) |

Methods: scrapling 4304 / crawl4ai 247 / httpx 3. Junk 0. Local docs excluded from git — regenerate with one command below.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install crawl4ai scrapling scrapegraphai beautifulsoup4 lxml html2text httpx
```

## Run

```bash
# full crawl (resume-safe)
python3 crawl_copilotkit.py --max-pages 8000 --concurrency 30
# steady state — only NEW pages, never recrawls existing
python3 update_incremental.py --check-only
python3 update_incremental.py
python3 update_incremental.py --force <URL>
```

Rerun verified no-op (5.1 s, visited 4554→4554). Cron: `0 3 * * * cd <repo> && python3 update_incremental.py >> update.log 2>&1`.

## How it works

1. **Seed**: `sitemap.xml` (3993, single urlset) + `llms.txt`/`llms-full.txt` (~1045 links) → ~4027 seeds.
2. **Fetch per URL**: Scrapling `Fetcher.get(stealthy_headers=True)` → keep `<main>/<article>` → ScrapeGraphAI `convert_to_md`; thin/fail → Crawl4AI → httpx. Frontmatter + `# title` + `> Source:`.
3. **Expand**: `normalize_url()` allows `*.copilotkit.ai`, drops binary/`.json`/backtick.
4. **Output**: `docs/<path>.md`, `_meta/`, `_index.jsonl`, `_manifest.json`, `_llms/`, `crawl_state.json`.

## Verify

```bash
python3 update_incremental.py --check-only   # new=1 = known origin-500
find docs -name '*.md' | wc -l               # 4552
cat docs/_manifest.json
curl -s -o /dev/null -w '%{http_code}\n' https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-powered-textarea/step-2-setup-copilotkit/  # 500
```

## Layout

```
crawl_copilotkit.py  update_incremental.py
guide_code/          # in-depth coder guide + coder_scrape.py / coder_update.py
docs/                # full crawl output (committed: 4,552 files, all <10MB)
tools/               # git-ignored (symlinks to shared clones)
```

## Limits

- 1 sitemap URL 500s on origin (site bug). `dashboard.*` login-walled. ScrapeGraphAI used locally (LLM graphs need keys; not required).
