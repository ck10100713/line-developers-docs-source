#!/usr/bin/env python3
"""把 docs/zh-Hant 複製到 build/docs 供 MkDocs 使用。

LINE 的原始檔名都是 index.html.md，MkDocs 只認 .md，
因此複製時把 index.html.md 改名成 index.md。
只複製、不刪除任何檔案（build/ 為 gitignore 的可重建產物）。
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "zh-Hant"
DST = ROOT / "build" / "docs"

LANDING = """# LINE Developers 文件（繁體中文）

這是 [LINE Developers 官方文件](https://developers.line.biz/en/) 的繁體中文翻譯，
供個人學習參考使用。

> 譯文以英文版為來源，僅翻譯內文；文件中的連結與圖片仍指向官方網站。
> 內容若與官方有出入，請以 [官方文件](https://developers.line.biz/en/) 為準。

請使用左側選單瀏覽各分類，或用右上角的搜尋功能查找。
"""


def main() -> None:
    count = 0
    for md in SRC.rglob("*.md"):
        rel = md.relative_to(SRC)
        if rel.name == "index.html.md":
            rel = rel.with_name("index.md")
        out = DST / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md, out)
        count += 1
    (DST / "index.md").write_text(LANDING, encoding="utf-8")
    print(f"Prepared {count} pages into {DST}")


if __name__ == "__main__":
    main()
