"""Verifica i file di documentazione e i template del repository."""

import pathlib
import re
import sys
import urllib.parse

root = pathlib.Path(".")
required = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "CITATION.cff",
]
mancanti = [f for f in required if not (root / f).is_file() or not (root / f).stat().st_size]
if mancanti:
    sys.exit("File mancanti o vuoti: " + ", ".join(mancanti))

cff = (root / "CITATION.cff").read_text(encoding="utf-8")
for chiave in ("cff-version:", "message:", "title:", "authors:"):
    if chiave not in cff:
        sys.exit("CITATION.cff: chiave mancante " + chiave)

errori = []
markdown = [p for p in sorted(root.rglob("*.md")) if ".git" not in p.parts]
link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
fence_re = re.compile(r"```.*?```", re.DOTALL)
inline_re = re.compile(r"`[^`]+`")
scheme_re = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")
drive_re = re.compile(r"^[a-zA-Z]:[\\/]")
for md in markdown:
    testo = md.read_text(encoding="utf-8")
    for n, riga in enumerate(testo.splitlines(), 1):
        if riga != riga.rstrip():
            errori.append(f"{md}:{n}: spazio finale")
    cercabile = inline_re.sub("", fence_re.sub("", testo))
    for link in link_re.findall(cercabile):
        link = link.strip()
        if not link or link.startswith("#"):
            continue
        if link.startswith("<"):
            end = link.find(">")
            link = link[1:end] if end != -1 else link[1:]
        else:
            link = link.split()[0] if link.split() else link
        if not link or link.startswith("#"):
            continue
        if scheme_re.match(link) and not drive_re.match(link):
            continue
        dest = urllib.parse.unquote(link.split("#", 1)[0].split("?", 1)[0]).strip()
        if not dest:
            continue
        target = (root / dest.lstrip("/")) if dest.startswith("/") else (md.parent / dest)
        if not target.exists():
            errori.append(f"{md}: link locale non risolto: {link}")

if errori:
    sys.exit("Errori:\n" + "\n".join(errori))
print(f"OK: {len(required)} file presenti, {len(markdown)} Markdown verificati")
