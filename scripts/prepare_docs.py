#!/usr/bin/env python3
"""把 docs/zh-Hant 複製到 build/docs 供 MkDocs 使用。

兩件事：
1. LINE 的原始檔名都是 index.html.md，MkDocs 只認 .md，複製時改名成 index.md。
2. 站內互連：把指向官方英文站、且本地有對應頁的連結，改寫成 MkDocs
   相對 .md 連結（保留 #錨點）。沒有本地對應的（glossary/news/faq…）維持外部。

只複製/改寫，不刪除任何檔案（build/ 為 gitignore 的可重建產物）。
"""
from pathlib import Path
import os
import re

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "zh-Hant"
DST = ROOT / "build" / "docs"

# 只改寫 markdown 連結語法 ](url) 內的官方英文連結，避免動到程式碼區塊裡的裸網址
LINK_RE = re.compile(r"\]\((https://developers\.line\.biz/en/[^)\s]+)\)")
URL_PREFIX = "https://developers.line.biz/en/"

# 翻譯快照日期：對應的 LINE 官方文件版本（上游 repo 最新 commit 日）。
# 重新同步上游後請一併更新此處與 mkdocs.yml 的 copyright。
SNAPSHOT_DATE = "2026-06-03"

LANDING = f"""# LINE Developers 文件（繁體中文）

這是 [LINE Developers 官方文件](https://developers.line.biz/en/) 的繁體中文翻譯，
供個人學習參考使用。

!!! info "翻譯快照"
    本翻譯對應 LINE 官方文件 **{SNAPSHOT_DATE}** 的版本。
    LINE 之後的更新不會自動反映於此，最新內容請以
    [官方文件](https://developers.line.biz/en/) 為準。

> 譯文以英文版為來源，僅翻譯內文；本站已將指向官方文件的連結改寫為站內中文頁，
> 其餘（詞彙表、消息、FAQ 等未翻譯的頁面）仍指向官方網站。

請使用左側選單瀏覽各分類，或用右上角的搜尋功能查找。
"""


def build_page_set() -> set[str]:
    """所有本地頁面的 URL 路徑鍵，如 'docs/messaging-api/overview'、'reference/liff'。"""
    pages = set()
    for md in SRC.rglob("index.html.md"):
        rel = md.relative_to(SRC).parent  # 去掉 /index.html.md
        pages.add(rel.as_posix())
    return pages


def make_rewriter(current_key: str, pages: set[str], stats: dict):
    """current_key 是當前檔案的頁面鍵（如 'docs/basics/channel-access-token'）。"""
    current_dir = DST / current_key

    def repl(m: re.Match) -> str:
        url = m.group(1)
        rest = url[len(URL_PREFIX):]
        frag = ""
        if "#" in rest:
            rest, f = rest.split("#", 1)
            frag = "#" + f
        path = rest.rstrip("/")
        if path in pages:
            target = DST / path / "index.md"
            rel = os.path.relpath(target, start=current_dir)
            stats["rewritten"] += 1
            return f"]({rel}{frag})"
        stats["external"] += 1
        return m.group(0)  # 無本地對應，維持外部連結

    return repl


def main() -> None:
    pages = build_page_set()
    count = 0
    stats = {"rewritten": 0, "external": 0}
    for md in SRC.rglob("*.md"):
        rel = md.relative_to(SRC)
        key = rel.parent.as_posix()
        if rel.name == "index.html.md":
            rel = rel.with_name("index.md")
        out = DST / rel
        out.parent.mkdir(parents=True, exist_ok=True)

        text = md.read_text(encoding="utf-8")
        rewriter = make_rewriter(key, pages, stats)
        new_text = LINK_RE.sub(rewriter, text)
        out.write_text(new_text, encoding="utf-8")
        count += 1

    (DST / "index.md").write_text(LANDING, encoding="utf-8")
    print(
        f"Prepared {count} pages into {DST}; "
        f"rewrote {stats['rewritten']} links to internal, "
        f"left {stats['external']} external (no local page)"
    )


if __name__ == "__main__":
    main()
