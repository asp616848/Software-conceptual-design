#!/usr/bin/env python3
"""SCD_Notes.md -> SCD_Notes.pdf (images + mermaid), via markdown + headless Chrome.

Run from the project root:  /path/to/python scripts/build_pdf.py
Needs: `markdown` (pip), Google Chrome / Chromium. mermaid.min.js sits next to this script.
"""
import re, shutil, subprocess, sys, tempfile
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[1]
MERMAID = Path(__file__).with_name("mermaid.min.js")
CHROME = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
          "/Applications/Chromium.app/Contents/MacOS/Chromium"]
CSS = """
@page { size: A4; margin: 14mm 13mm; }
body { font: 10.5pt/1.5 -apple-system, "Helvetica Neue", Arial, sans-serif; color: #1a1a1a; }
h1 { font-size: 21pt; border-bottom: 2px solid #333; padding-bottom: 4px; break-after: avoid; }
h1:not(:first-of-type) { break-before: page; }
h2 { font-size: 15pt; margin-top: 1.4em; border-bottom: 1px solid #bbb; break-after: avoid; }
h3, h4 { break-after: avoid; }
img { max-width: 100%; max-height: 95mm; display: block; margin: 6px auto; border: 1px solid #ddd; break-inside: avoid; }
table { border-collapse: collapse; margin: 8px 0; break-inside: avoid; font-size: 9.5pt; }
th, td { border: 1px solid #999; padding: 3px 7px; vertical-align: top; }
th { background: #eee; }
code { font: 9pt Menlo, monospace; background: #f3f3f3; padding: 0 3px; border-radius: 3px; }
pre { background: #f6f6f6; padding: 8px; white-space: pre-wrap; break-inside: avoid; }
pre.mermaid { background: none; text-align: center; white-space: pre; }
pre.mermaid svg { max-width: 100%; height: auto; max-height: 120mm; }
blockquote { border-left: 3px solid #999; margin-left: 0; padding-left: 10px; color: #333; background: #fafafa; }
hr { border: 0; border-top: 1px solid #ccc; }
"""

def main():
    chrome = next((c for c in CHROME if Path(c).exists()), shutil.which("google-chrome") or shutil.which("chromium"))
    if not chrome:
        sys.exit("Chrome/Chromium not found")
    md = (ROOT / "SCD_Notes.md").read_text(encoding="utf-8")
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
    body = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>', r'<pre class="mermaid">\1</pre>', body, flags=re.S)
    page = (f'<!doctype html><html><head><meta charset="utf-8"><base href="{ROOT.as_uri()}/"><style>{CSS}</style></head>'
            f'<body>{body}<script src="{MERMAID.as_uri()}"></script>'
            '<script>mermaid.initialize({startOnLoad:true,theme:"neutral",flowchart:{useMaxWidth:true}});</script></body></html>')
    out = ROOT / "SCD_Notes.pdf"
    with tempfile.TemporaryDirectory() as tmp:
        h = Path(tmp) / "n.html"; h.write_text(page, encoding="utf-8")
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files",
                        "--no-pdf-header-footer", "--virtual-time-budget=40000", f"--user-data-dir={Path(tmp)/'p'}",
                        f"--print-to-pdf={out}", h.as_uri()], check=True, capture_output=True, timeout=300)
    print("wrote", out, out.stat().st_size // 1024, "KB")

main()
