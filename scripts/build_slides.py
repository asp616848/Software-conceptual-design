#!/usr/bin/env python3
"""SCD_Notes.md -> SCD_Slides.pdf (16:9 slides, mermaid rendered), via markdown + headless Chrome.

Run from the project root:  python scripts/build_slides.py
Slides: one per `###` section, plus a divider per `##` (and its intro text, if any).
Content that overflows a slide is scaled down to fit.
"""
import re, shutil, subprocess, sys, tempfile
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[1]
MERMAID = Path(__file__).with_name("mermaid.min.js")
CHROME = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
          "/Applications/Chromium.app/Contents/MacOS/Chromium"]
CSS = """
@page { size: 13.333in 7.5in; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font: 17pt/1.4 -apple-system, "Helvetica Neue", Arial, sans-serif; color: #1a1a1a; }
.slide { width: 13.333in; height: 7.5in; padding: 0.5in 0.7in; overflow: hidden; break-after: page; position: relative; background: #fff; }
.slide h1.t { font-size: 28pt; margin: 0 0 0.15in; padding-bottom: 6px; border-bottom: 3px solid #2b5cab; color: #14305e; }
.slide.divider { display: flex; flex-direction: column; justify-content: center; background: #14305e; color: #fff; }
.slide.divider h1.t { font-size: 40pt; border: 0; color: #fff; }
.slide.divider .body { color: #dbe5f5; }
.slide.cover { display: flex; flex-direction: column; justify-content: center; background: #14305e; color: #fff; }
.slide.cover h1.t { font-size: 38pt; border: 0; color: #fff; }
.body { transform-origin: top left; }
table { border-collapse: collapse; margin: 8px 0; font-size: 0.85em; }
th, td { border: 1px solid #999; padding: 3px 8px; vertical-align: top; }
th { background: #e6edf8; color: #1a1a1a; }
code { font: 0.85em Menlo, monospace; background: #f1f1f1; color: #1a1a1a; padding: 0 3px; border-radius: 3px; }
pre.mermaid { text-align: center; background: none; color: #1a1a1a; }
pre.mermaid svg { max-width: 100%; height: auto; max-height: 3.6in; }
ul, ol { margin: 0.3em 0; padding-left: 1.3em; }
p { margin: 0.4em 0; }
"""
JS = """
mermaid.initialize({startOnLoad:false,theme:"neutral",flowchart:{useMaxWidth:true}});
mermaid.run().then(() => {
  document.querySelectorAll('.slide').forEach(s => {
    const b = s.querySelector('.body'); if (!b) return;
    const avail = s.clientHeight - b.offsetTop - 30;
    if (b.scrollHeight > avail) { const k = avail / b.scrollHeight; b.style.transform = 'scale(' + k + ')'; b.style.width = (100 / k) + '%'; }
  });
  document.title = 'done';
});
"""

def split_slides(md):
    slides, cur, fence = [], None, False
    def start(kind, title):
        nonlocal cur
        cur = {"kind": kind, "title": title, "lines": []}; slides.append(cur)
    for line in md.splitlines():
        if line.startswith("```"): fence = not fence
        m = None if fence else re.match(r"(#{1,3}) (.*)", line)
        if m:
            n, t = len(m.group(1)), m.group(2)
            start("cover" if n == 1 else "divider" if n == 2 else "slide", t)
        elif cur is not None and line.strip() != "---":
            cur["lines"].append(line)
    return slides

def main():
    chrome = next((c for c in CHROME if Path(c).exists()), shutil.which("google-chrome") or shutil.which("chromium"))
    if not chrome: sys.exit("Chrome/Chromium not found")
    html = []
    for s in split_slides((ROOT / "SCD_Notes.md").read_text(encoding="utf-8")):
        body = markdown.markdown("\n".join(s["lines"]), extensions=["tables", "fenced_code", "sane_lists"])
        body = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>', r'<pre class="mermaid">\1</pre>', body, flags=re.S)
        title = re.sub(r"[*`]", "", s["title"])
        if s["kind"] == "divider" and s["lines"] and "".join(s["lines"]).strip():
            s["kind"] = "slide"  # a ## with its own content is a normal slide
        html.append(f'<section class="slide {s["kind"]}"><h1 class="t">{title}</h1><div class="body">{body}</div></section>')
    page = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(html)}'
            f'<script src="{MERMAID.as_uri()}"></script><script>{JS}</script></body></html>')
    out = ROOT / "SCD_Slides.pdf"
    with tempfile.TemporaryDirectory() as tmp:
        h = Path(tmp) / "s.html"; h.write_text(page, encoding="utf-8")
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files",
                        "--no-pdf-header-footer", "--virtual-time-budget=40000", f"--user-data-dir={Path(tmp)/'p'}",
                        f"--print-to-pdf={out}", h.as_uri()], check=True, capture_output=True, timeout=300)
    print("wrote", out, out.stat().st_size // 1024, "KB")

main()
