---
name: ICTRSearcher
description: 独立检索卢旺达问题国际刑事法庭（ICTR）官网，查找案件页、新闻稿和公开遗产文书；支持站点原生 search、页面正文读取和 PDF 文本提取。
---

# ICTRSearcher

> **`<skill-dir>`** = 本 SKILL.md 所在目录。核心脚本为 `<skill-dir>/scripts/ictr_search.py`；Windows 用 `<skill-dir>/run.ps1`，macOS/Linux 用 `<skill-dir>/run.sh`。部署与排错见 [README.md](README.md)。

这个 skill 只做 `unictr.irmct.org` 一个站点：

- `search`：调用站点原生 `search?keys=`，返回案件页、新闻稿和其他公开页面；
- `fetch`：读取页面正文，或下载并提取 PDF；
- `doctor`：探测站点搜索。

## 命令

```powershell
& '<skill-dir>/run.ps1' search 'Akayesu' --limit 10 --out './ictr-search.json'
& '<skill-dir>/run.ps1' search 'genocide' --limit 10
& '<skill-dir>/run.ps1' fetch 'https://unictr.irmct.org/en/news/...' --out './ictr-page.json' --text-out './ictr-page.txt'
& '<skill-dir>/run.ps1' fetch 'https://unictr.irmct.org/...pdf' --pdf-out './ictr.pdf' --text-out './ictr.txt'
& '<skill-dir>/run.ps1' doctor
```

通用参数：`--out`、`--cache`、`--cache-ttl`、`--offline`、`--timeout`。`search` 另有 `--limit`（1..50）、`--offset`；`fetch` 另有 `--text-out`、`--pdf-out`、`--max-mb`。

## 结果边界

- 站内搜索返回官网页面（案件页、新闻稿、公开遗产页面），不是判例全文数据库；`total` 是当前结果页的条目数。
- 判例全文、书状和法庭文件请优先用 `LegalToolsSearcher` 检索 Legal Tools 的 ICTR 馆藏；本 skill 负责官方站点的页面级材料。
- `fetch` 的 PDF 页号是 PDF 位置，不是印刷页码；扫描件可能 `needs_ocr=true`。
- 新闻稿不是裁判文书；引用案件结论时回到判决/裁定原文。

## 参考

- 2026-11-09 实测：`search?keys=`、20 条/页、新闻页选择器：[references/ictr-search.md](references/ictr-search.md)
- 部署、环境与排错：[README.md](README.md)
