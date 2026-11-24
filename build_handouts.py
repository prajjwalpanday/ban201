"""Write standalone, printable HTML for each BAN 201 week."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

import mistune

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
OUT = ROOT / "html"

md = mistune.create_markdown(plugins=["table", "url"])

PAGES = {
    "index.md": OUT / "index.html",
    "week-01-introduction.md": OUT / "week-01" / "week-01-introduction.html",
    "week-02-descriptive-analytics.md": OUT / "week-02" / "week-02-descriptive-analytics.html",
    "in-class-descriptive-analytics.md": OUT / "week-02" / "in-class-descriptive-analytics.html",
    "week-03-wrap-up.md": OUT / "week-03" / "week-03-wrap-up.html",
    "week-04-presenting-findings.md": OUT / "week-04" / "week-04-presenting-findings.html",
}


def inline(text: str) -> str:
    html = md(text.strip()).strip()
    if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
        return html[3:-4]
    return html


def block(text: str) -> str:
    return md(text.strip()) if text.strip() else ""


def parse(lines: list[str], i: int = 0, end_colons: int | None = None):
    body: list = []
    while i < len(lines):
        line = lines[i]
        if end_colons and line == ":" * end_colons:
            return body, i + 1
        match = re.match(r"^(:{3,})\{(\w+)\}(.*)$", line)
        if match:
            colons = len(match.group(1))
            kind = match.group(2)
            title = match.group(3).strip()
            inner, i = parse(lines, i + 1, colons)
            body.append(("directive", kind, title, inner))
            continue
        body.append(("line", line))
        i += 1
    return body, i


def render_nodes(nodes: list) -> str:
    chunks: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if buf:
            chunks.append(block("\n".join(buf)))
            buf.clear()

    for node in nodes:
        if node[0] == "line":
            buf.append(node[1])
            continue
        flush()
        _, kind, title, inner = node
        chunks.append(render_directive(kind, title, inner))
    flush()
    return "\n".join(chunks)


def render_directive(kind: str, title: str, inner: list) -> str:
    if kind == "grid":
        cards = [
            render_directive(node[1], node[2], node[3])
            for node in inner
            if node[0] == "directive"
        ]
        return '<div class="cards">\n' + "\n".join(cards) + "\n</div>"
    if kind == "card":
        header = footer = None
        rest = []
        for node in inner:
            if node[0] == "line" and node[1].startswith(":header:"):
                header = node[1][len(":header:") :].strip()
            elif node[0] == "line" and node[1].startswith(":footer:"):
                footer = node[1][len(":footer:") :].strip()
            else:
                rest.append(node)
        parts = ['<section class="card">']
        if header:
            parts.append(f'<h3>{inline(header)}</h3>')
        parts.append(render_nodes(rest))
        if footer:
            parts.append(f'<p class="card-foot">{inline(footer)}</p>')
        parts.append("</section>")
        return "\n".join(parts)
    label = title or kind.title()
    css = kind if kind in {"tip", "note", "seealso"} else "note"
    return (
        f'<aside class="callout {css}"><p class="callout-title">{label}</p>'
        f"{render_nodes(inner)}</aside>"
    )


def rewrite_links(text: str, source_name: str) -> str:
    here = PAGES[source_name].parent

    def repl(match: re.Match) -> str:
        label, target = match.group(1), match.group(2)
        if target.startswith("http"):
            return match.group(0)
        name = Path(target).name
        if name not in PAGES and not name.endswith(".csv"):
            return match.group(0)
        if name.endswith(".csv"):
            dest = OUT / "week-02" / "data" / name
        else:
            dest = PAGES[name]
        rel = Path(os_relpath(dest, here)).as_posix()
        return f"[{label}]({rel})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def os_relpath(dest: Path, start: Path) -> str:
    return Path(os_path_rel(dest, start))


def os_path_rel(dest: Path, start: Path) -> str:
    import os

    return os.path.relpath(dest, start)


NAV = [
    ("Home", "index.md"),
    ("Week 1", "week-01-introduction.md"),
    ("Week 2", "week-02-descriptive-analytics.md"),
    ("Week 2 lab", "in-class-descriptive-analytics.md"),
    ("Week 3", "week-03-wrap-up.md"),
    ("Week 4", "week-04-presenting-findings.md"),
]

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0 auto;
  max-width: 820px;
  padding: 2rem 1.4rem 4rem;
  color: #1c1917;
  background: #fafaf9;
  font: 17px/1.55 Georgia, "Iowan Old Style", "Palatino Linotype", serif;
}
header.top { margin-bottom: 1.5rem; }
.kicker {
  margin: 0;
  color: #7c2d12;
  font: 600 0.78rem/1.2 "Segoe UI", sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
h1 { font-size: 2rem; line-height: 1.2; margin: 0.3rem 0 1rem; }
h2 { font-size: 1.45rem; margin: 2rem 0 0.6rem; padding-top: 0.4rem; border-top: 1px solid #e7e5e4; }
h3 { font-size: 1.15rem; margin: 1.4rem 0 0.4rem; }
a { color: #9a3412; }
nav.weeks {
  display: flex; flex-wrap: wrap; gap: 0.4rem;
  margin: 0.8rem 0 0;
  font: 0.85rem/1.2 "Segoe UI", sans-serif;
}
nav.weeks a {
  text-decoration: none;
  border: 1px solid #e7e5e4;
  background: white;
  border-radius: 999px;
  padding: 0.25rem 0.7rem;
}
nav.weeks a[aria-current="page"] { background: #7c2d12; color: white; border-color: #7c2d12; }
p.screen-note { color: #57534e; font: 0.9rem/1.4 "Segoe UI", sans-serif; }
table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem; background: white; }
th, td { border: 1px solid #d6d3d1; padding: 0.4rem 0.55rem; text-align: left; vertical-align: top; }
th { background: #f5f5f4; }
code, pre { font-family: Consolas, "Courier New", monospace; font-size: 0.9rem; }
code { background: #f5f5f4; padding: 0.05rem 0.25rem; }
pre { background: #1c1917; color: #fafaf9; padding: 0.8rem 1rem; overflow: auto; }
.callout { border-left: 4px solid #c2410c; background: #fff7ed; padding: 0.7rem 1rem; margin: 1rem 0; }
.callout.note { border-color: #1d4ed8; background: #eff6ff; }
.callout.seealso { border-color: #047857; background: #ecfdf5; }
.callout-title { margin: 0 0 0.3rem; font: 700 0.82rem/1.2 "Segoe UI", sans-serif; letter-spacing: 0.04em; text-transform: uppercase; }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin: 1rem 0; }
.card { background: white; border: 1px solid #e7e5e4; border-radius: 8px; padding: 0.8rem 1rem; }
.card h3 { margin-top: 0; }
.card-foot { margin: 0.6rem 0 0; color: #57534e; font-style: italic; }
@media (max-width: 700px) { .cards { grid-template-columns: 1fr; } }
@media print {
  body { max-width: none; background: white; padding: 0; font-size: 11.5pt; }
  nav.weeks, .screen-note { display: none; }
  a { color: inherit; text-decoration: none; }
  h2 { break-before: page; border-top: 0; }
  h2:first-of-type { break-before: auto; }
  table, .callout, .card, pre { break-inside: avoid; }
  .cards { display: block; }
  .card { margin-bottom: 0.6rem; }
}
"""


def nav_html(source_name: str) -> str:
    here = PAGES[source_name].parent
    links = []
    for label, name in NAV:
        dest = PAGES[name]
        rel = Path(os_path_rel(dest, here)).as_posix()
        current = ' aria-current="page"' if name == source_name else ""
        links.append(f'<a href="{rel}"{current}>{label}</a>')
    return '<nav class="weeks">' + "".join(links) + "</nav>"


def build_one(source: Path, source_name: str) -> None:
    text = source.read_text(encoding="utf-8").replace(r"\$", "$")
    text = rewrite_links(text, source_name)
    nodes, _ = parse(text.splitlines())
    body = render_nodes(nodes)
    title_match = re.search(r"<h1>(.*?)</h1>", body)
    title = re.sub("<[^>]+>", "", title_match.group(1)) if title_match else "BAN 201"
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — BAN 201</title>
<style>{CSS}</style>
</head>
<body>
<header class="top">
<p class="kicker">BAN 201 · Introduction to Business Analytics · Nichols College · Fall 2026</p>
{nav_html(source_name)}
<p class="screen-note">To print this lecture, press Ctrl+P. The week links above stay off the printed page.</p>
</header>
{body}
</body>
</html>
"""
    dest = PAGES[source_name]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page, encoding="utf-8")
    print(dest.relative_to(ROOT))


def main() -> None:
    sources = {
        "index.md": CONTENT / "index.md",
        "week-01-introduction.md": CONTENT / "week-01-introduction.md",
        "week-02-descriptive-analytics.md": CONTENT / "week-02-descriptive-analytics.md",
        "in-class-descriptive-analytics.md": CONTENT / "assignments" / "in-class-descriptive-analytics.md",
        "week-03-wrap-up.md": CONTENT / "week-03-wrap-up.md",
        "week-04-presenting-findings.md": CONTENT / "week-04-presenting-findings.md",
    }
    for name, path in sources.items():
        build_one(path, name)
    data_out = OUT / "week-02" / "data"
    data_out.mkdir(parents=True, exist_ok=True)
    for csv_name in ("bison-beans-daily.csv", "bison-beans-orders.csv"):
        shutil.copyfile(CONTENT / "data" / csv_name, data_out / csv_name)
        print((data_out / csv_name).relative_to(ROOT))


if __name__ == "__main__":
    main()
