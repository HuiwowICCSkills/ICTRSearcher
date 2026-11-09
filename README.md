# ICTRSearcher 部署指引

独立检索 ICTR 官网的案件页、新闻稿和公开遗产页面。只访问 `unictr.irmct.org`。

仓库：<https://github.com/HuiwowICCSkills/ICTRSearcher>（公开）。

## 1. 环境

Python 3.10+，依赖 `requests`、`beautifulsoup4`、`pypdf`；无需登录。

## 2. 安装

```powershell
git clone https://github.com/HuiwowICCSkills/ICTRSearcher.git "$env:USERPROFILE\.codex\skills\ICTRSearcher"
python -m pip install -r "$env:USERPROFILE\.codex\skills\ICTRSearcher\requirements.txt"
```

## 3. 自检

```powershell
& "$env:USERPROFILE\.codex\skills\ICTRSearcher\run.ps1" doctor
```

## 4. 使用

```powershell
$ictr = "$env:USERPROFILE\.codex\skills\ICTRSearcher\run.ps1"
& $ictr search 'Akayesu' --limit 10 --out './ictr.json'
& $ictr fetch 'https://unictr.irmct.org/en/news/...' --out './page.json' --text-out './page.txt'
```

## 5. 排错

| 现象 | 处理 |
| --- | --- |
| 搜索返回新闻稿多 | 站内搜索覆盖新闻/案件/遗产页面；按 `section` 过滤或改用 LegalTools |
| `Insufficient ICTR page text` | 页面选择器变化；检查 `article`/`#content` 结构 |

## 6. 边界

本 skill 不是判例全文数据库；判例、书状和法庭文件优先用 `LegalToolsSearcher`。

## 实测效果（2026-11-09）

以下命令与结果来自本机 `~/.codex/skills/ICTRSearcher` 的实网运行；检索日期 2026-11-09（Asia/Shanghai），输出为该次运行实际返回的 JSON 报告。

```powershell
& .\run.ps1 search 'Akayesu' --limit 5
```

- 状态：`ok`；服务端/索引报告 `total = 20`；本次返回 5 条。
- 代表性结果：

| 题名 | 类型 / 日期 | 链接 |
| --- | --- | --- |
| The six lawyers of Jean-Paul Akayesu, former Bourgmestre of Taba | retrieved_metadata / news-or-press；无日期字段 | https://unictr.irmct.org/en/news/six-lawyers-jean-paul-akayesu-former-bourgmestre-taba |
| Historic judgement finds Akayesu guilty of genocide | retrieved_metadata / news-or-press；无日期字段 | https://unictr.irmct.org/en/news/historic-judgement-finds-akayesu-guilty-genocide |
| Closing arguments of Defence Counsel in the trial of Jean-Paul Akayesu | retrieved_metadata / news-or-press；无日期字段 | https://unictr.irmct.org/en/news/closing-arguments-defence-counsel-trial-jean-paul-akayesu |

> 说明：`total = 20` 是 ICTR 官网站内搜索对 `Akayesu` 的命中数（`scope`：Official ICTR site search (cases, news and legacy pages); not a full-text judgment database），覆盖案件页、新闻稿与遗产页面，本轮返回的 5 条 `section` 均为 `news-or-press`，且 JSON 中没有日期字段（本表不补写日期）。结果行是站点页面元数据（`result_type = retrieved_metadata`，`content_scope`：site search record, not the linked judgment or news text），只能证明该页面在此关键词下被站内检索命中；判决全文须用 `LegalToolsSearcher` 或 `fetch` 另行取得，引用前不得把新闻标题当作裁判结论。