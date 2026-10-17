# GUIDE — docs.copilotkit.ai docs: full redo + incremental updates (end to end)

4,554 URLs, 100% crawl, daily GitHub Action green. Redo from scratch via §2; daily updates via §3.

## 0. Architecture

```
crawl_copilotkit.py    → docs/<path>.md        (resume-safe crawl)
update_incremental.py  → incremental pass      (new + lastmod-stale, capped refresh)
.github/workflows/update-docs.yml              → daily 03:00 UTC on GitHub Actions
guide_code/             coder_scrape.py / coder_update.py (one-page scrape + manual incremental)
```

Stack: **Scrapling → Crawl4AI → ScrapeGraphAI → httpx** fallback chain. Saved as frontmatter `.md` + `_meta/*.json` + `_index.jsonl` + `_manifest.json` + daily stamp `_last_verified.json`. State: `crawl_state.json`.

## 1. Setup

```bash
pip install -r requirements.txt && python -m playwright install chromium
# patched tool clones under tools/ — see ai-docs GUIDE §1
```

## 2. Full redo

```bash
python3 crawl_copilotkit.py --concurrency 15
python3 update_incremental.py --check-only       # expect new=0
find docs -name '*.md' | wc -l                   # ~4,554
```

- Seeds: `https://docs.copilotkit.ai/sitemap.xml` + llms.txt links; resumable; login-walled recorded as failed.
- Single-page test end to end: `python3 guide_code/coder_scrape.py https://docs.copilotkit.ai/ PREFIX-anything /tmp/k.md`

## 3. Incremental updates (GitHub Action, daily 03:00 UTC)

Same mechanics as cloudflare (02:00) and ai-docs (04:00) — staggered so the three Actions never fight for the shared VM's outbound bandwidth:

1. live sitemap + llms.txt diff → crawl new; refresh lastmod-stale newest-first, cap 100.
2. A snippet: daily stamp rewritten (README "Last verified:"), commit + push with rebase-retry; shared stamp files resolved `--ours`.

Manual run locally: `python3 update_incremental.py --concurrency 10` (or `guide_code/coder_update.py --run --concurrency 10`).

## 4. Recovery

`boot.sh` + `cloud-init.yaml` like the rest of the family; `/data` is the durable base, git is the secondary copy.

## 5. Gotchas

| Symptom | Fix |
|---|---|
| llms.txt advertises URLs that 404 | leave them recorded as failed; don't chase. |
| stamp conflict keeps failing the Action | verify the `--ours` checkout line lists exactly `docs/_last_verified.json docs/_manifest.json`. |
| devdocs-style client-side pages thin | crawl4ai fallback renders JS; check frontmatter `method`. |
