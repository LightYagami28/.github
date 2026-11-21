"""Verifica i file di documentazione e i template del repository."""

import pathlib
import re
import sys

root = pathlib.Path(".")
required = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "CITATION.cff",
]
mancanti = [f for f in required if not (root / f).is_file() or (root / f).stat().st_size == 0]
if mancanti:
    sys.exit("File mancanti o vuoti: " + ", ".join(mancanti))

cff = (root / "CITATION.cff").read_text(encoding="utf-8")
for chiave in ("cff-version:", "message:", "title:", "authors:"):
    if chiave not in cff:
        sys.exit("CITATION.cff: chiave mancante " + chiave)

errori = []
markdown = [p for p in sorted(root.rglob("*.md")) if ".git" not in p.parts]
for md in markdown:
    testo = md.read_text(encoding="utf-8")
    for n, riga in enumerate(testo.splitlines(), 1):
        if riga != riga.rstrip():
            errori.append(f"{md}:{n}: spazio finale")
    for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", testo):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        dest = link.split("#", 1)[0]
        if dest and not (md.parent / dest).exists():
            errori.append(f"{md}: link locale non risolto: {link}")

if errori:
    sys.exit("Errori:\n" + "\n".join(errori))
print(f"OK: {len(required)} file presenti, {len(markdown)} Markdown verificati")
