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
