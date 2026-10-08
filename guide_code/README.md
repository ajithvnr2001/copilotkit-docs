# CopilotKit docs — coder guide, end to end

Base: `/data/opencode/copilotkit/` · Docs: `docs/` (4,552 files / 4,554 urls, ~99M) · Status: sitemap 3992/3993 (1 origin-500), `update_incremental.py --check-only` → `new=1` (same known URL).

## 0. Map

```
copilotkit/
  crawl_copilotkit.py      # phase-1 full crawler (sitemap + llms + BFS)
  update_incremental.py    # steady-state updater: only NEW urls
  crawl_state.json         # {visited, failed} — resume + audit
  crawl.log                # full-crawl log
  docs/                    # output
    <area>/<path>.md       # e.g. quickstart.md, ag2/agent-config.md, _index.md
    _subdomains/<host>/…   # feature-viewer, dashboard, copilotkit.ai, www…
    _llms/                 # docs.copilotkit.ai_llms.txt + _llms-full.txt (7.9M)
    _meta/                 # 1 JSON per doc (url/file/title/method/sizes)
    _index.jsonl           # 1 JSON line per doc (url/file/title/method)
    _manifest.json         # counts, methods, hosts, timestamp
  tools/                   # symlinks → cloudflare/tools clones
  guide_code/
    README.md              # this file
    coder_scrape.py        # scrape ONE url (all 3 libs)
    coder_update.py        # minimal incremental updater
```

Prereqs: python3.10, `pip install crawl4ai scrapling scrapegraphai beautifulsoup4 lxml html2text httpx` (+ `crawl4ai` browsers present). No API keys — all conversions are local.

## 1. How each library is used

**Scrapling (primary)** — `guide_code/coder_scrape.py:19`, `crawl_copilotkit.py` via `scrapling_fetch_sync`.
`Fetcher.get(url, stealthy_headers=True, follow_redirects=True, timeout=25)` → `page.html_content`, `page.css("a")` for links, `page.css("title::text")`/`h1` for title. ~4304/4554 pages succeed here.

**Crawl4AI (JS fallback)** — `guide_code/coder_scrape.py:34`, `crawl_copilotkit.py:220`.
Only when Scrapling is thin (<500 chars) or non-200. `AsyncWebCrawler(BrowserConfig(headless=True))` + `CrawlerRunConfig(cache_mode=BYPASS)` → `res.html`, `res.markdown`, `res.links`. ~247 pages.

**ScrapeGraphAI (convert, no LLM)** — both files.
`scrapegraphai/utils/convert_to_md.py::convert_to_md(html, url)` turns the kept `<main>/<article>` into markdown; `cleanup_html` available same folder. Loaded by file path to dodge the broken `langchain.prompts` import in v1.36.0. Every page goes through it.

Per-page pipeline: Scrapling → (thin/fail?) Crawl4AI → (fail?) httpx+BeautifulSoup; markdown always via ScrapeGraphAI; saved with frontmatter `url/title/method/fetched_at` + `# title` + `> Source:` header.

## 2. Full crawl, reproducible

```bash
cd /data/opencode/copilotkit
python3 crawl_copilotkit.py --max-pages 8000 --concurrency 30
```

What happens: `load_sitemap_urls()` parses `sitemap.xml` (3993, single urlset) → `load_llms_urls()` saves `_llms/llms.txt` + `llms-full.txt`, extracts ~1045 links → seeds ≈4027 → BFS with `normalize_url()` (`crawl_copilotkit.py:78`: canonicalize `/index.md`→`/`, allow `*.copilotkit.ai`, drop binary/`.json`/backtick) → 15–30 workers → `docs/`, `_meta/`, `_index.jsonl`, `crawl_state.json`, `_manifest.json`. First run ≈49 min; rerun ≈5 s (all skipped, verified).

## 3. Incremental update (no recrawl)

```bash
python3 update_incremental.py --check-only     # expect new=1 (known origin-500)
python3 update_incremental.py                 # fetch only NEW
python3 update_incremental.py --force <URL>   # refetch one changed page
python3 guide_code/coder_update.py --check-only
python3 guide_code/coder_update.py --run --concurrency 10
```

Diff = live sitemap set − indexed set (encoding-aware `%40cf`/`@cf`); existing files never opened for write. State + index appended only for new pages. Proven: 2 sitemap redirects recovered + 6 blog i18n elsewhere via same path.

## 4. Verify (copy-paste)

```bash
cd /data/opencode/copilotkit
python3 update_incremental.py --check-only
find docs -name '*.md' | wc -l            # expect 4552
wc -l docs/_index.jsonl                   # expect 4554 lines (2 dup urls share a file)
grep -c '"method": "scrapling' docs/_index.jsonl
cat docs/_manifest.json
curl -s -o /dev/null -w '%{http_code}\n' https://docs.copilotkit.ai/ms-agent-harness-dotnet/tutorials/ai-powered-textarea/step-2-setup-copilotkit/  # expect 500 (origin bug)
```

Healthy = sitemap 3992/3993, junk (backtick/`.json`) 0, `failed` only contains 500/403/login-walled hosts.

## 5. Single-page recipe (coder)

```python
import asyncio, sys
sys.path.insert(0, "/data/opencode/copilotkit/guide_code")
from coder_scrape import scrape
md, title, method = asyncio.run(scrape("https://docs.copilotkit.ai/quickstart"))
print(title, method, len(md))  # Quickstart scrapling+scrapegraph ~10236
```

CLI equivalent: `python3 guide_code/coder_scrape.py <URL> [out.md]` (verified).

## 6. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `new=1` always for one URL | origin returns 500 | none — recorded in `failed`; confirm with curl |
| `403` on dashboard/* | login wall | expected; skipped |
| thin page → slow (20 s) | Crawl4AI fallback rendering JS | expected for ~5%; raise `--concurrency` |
| `langchain.prompts` ImportError | scrapegraphai 1.36 vs langchain 1.x | we bypass via file-load; do not `from scrapegraphai.graphs import …` |
| rerun slow | deleted `crawl_state.json` | keep it — it is the skip-list |

## 7. Cron

`0 3 * * * cd /data/opencode/copilotkit && python3 update_incremental.py >> update.log 2>&1`

## 8. FAQ

- *Rerun recrawls?* No — verified 5.1 s no-op, `visited` 4554→4554.
- *Where is reference/cookbook?* In-sitemap, e.g. `docs/reference.md`, `docs/cookbook.md` + per-framework folders (`ag2/`, `mastra/`, `agno/`…).
- *Subdomains?* `_subdomains/` (27 pages); `community/dash/support` login/anti-bot walled — failures logged, not silently dropped.
