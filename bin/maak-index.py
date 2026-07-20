#!/usr/bin/env python3
"""Genereert index.html: een overzicht van alle projecten in projecten/.

Draai vanuit de repo-root:  python3 bin/maak-index.py
Of dubbelklik sync.command — die roept dit script automatisch aan.
"""

from __future__ import annotations

import html
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTEN = ROOT / "projecten"

# Bestandssoorten die we per project herkennen, in de volgorde waarin ze tonen.
SOORTEN = [
    ("html", "Lesmateriaal", "html"),
    ("pdf", "PDF", "pdf"),
    ("projectdocument.md", "Projectdocument", "doc"),
    ("rubric.md", "Rubric", "doc"),
    ("docentenhandleiding.md", "Docentenhandleiding", "doc"),
    ("csv", "Eindtermen", "csv"),
]


def mooi_label(stem: str) -> str:
    """Leesbaar label voor een opdracht-/werkblad-bestand, bijv.
    'opdracht-bedrijfsbezoek' -> 'Opdracht: Bedrijfsbezoek'."""
    for prefix, woord in (("opdracht-", "Opdracht"), ("werkblad-", "Werkblad")):
        if stem.startswith(prefix):
            rest = stem[len(prefix):].replace("-", " ")
            return f"{woord}: {rest.capitalize()}"
    return stem.replace("-", " ").capitalize()


def titel_uit(md: Path) -> str | None:
    """Eerste markdown-kop uit een projectdocument."""
    try:
        for regel in md.read_text(encoding="utf-8").splitlines():
            if regel.startswith("# "):
                return regel[2:].strip()
    except OSError:
        pass
    return None


def samenvatting_uit(md: Path) -> str:
    """Eerste echte alinea onder de titel, ingekort tot een tegelregel."""
    try:
        tekst = md.read_text(encoding="utf-8")
    except OSError:
        return ""
    # Sla koppen, lijsten, tabellen en losse metaregels over
    for blok in tekst.split("\n\n"):
        blok = blok.strip()
        if not blok or blok.startswith(("#", "-", "*", "|", ">")):
            continue
        blok = re.sub(r"[*_`\[\]]", "", blok).replace("\n", " ")
        return blok[:180] + ("…" if len(blok) > 180 else "")
    return ""


def bestanden_van(map_: Path) -> list[tuple[str, str, str]]:
    """(label, pad, soort) voor alles wat we in een projectmap herkennen."""
    gevonden = []
    for patroon, label, soort in SOORTEN:
        if patroon in ("html", "pdf", "csv"):
            # hoofdbestand (mapnaam) eerst, daarna de rest alfabetisch;
            # de docentenhandleiding heeft zijn eigen regel in SOORTEN
            treffers = sorted(
                (t for t in map_.glob(f"*.{patroon}") if t.stem != "docentenhandleiding"),
                key=lambda t: (t.stem != map_.name, t.stem),
            )
        elif patroon == "docentenhandleiding.md":
            treffers = sorted(map_.glob("docentenhandleiding.*"))
        else:
            kandidaat = map_ / patroon
            treffers = [kandidaat] if kandidaat.exists() else []
        for t in treffers:
            if len(treffers) == 1:
                naam = label
            elif patroon == "docentenhandleiding.md":
                naam = f"{label} ({t.suffix.lstrip('.')})"
            elif patroon == "html":
                naam = mooi_label(t.stem)
            else:
                naam = f"{label} — {t.stem}"
            gevonden.append((naam, t.relative_to(ROOT).as_posix(), soort))
    return gevonden


def projecten() -> list[dict]:
    if not PROJECTEN.is_dir():
        return []
    uit = []
    for map_ in sorted(p for p in PROJECTEN.iterdir() if p.is_dir()):
        doc = map_ / "projectdocument.md"
        animaties = sorted((map_ / "animaties").glob("*.html")) if (map_ / "animaties").is_dir() else []
        uit.append(
            {
                "map": map_.name,
                "titel": titel_uit(doc) or map_.name.replace("-", " ").capitalize(),
                "samenvatting": samenvatting_uit(doc),
                "bestanden": bestanden_van(map_),
                "eindtermen": bool(list(map_.glob("eindtermen-*-koppeling.csv"))),
                "animaties": [(a.stem.replace("-", " "), a.relative_to(ROOT).as_posix()) for a in animaties],
            }
        )
    return uit


def tegel(p: dict) -> str:
    e = html.escape
    links = "".join(
        f'<a class="f f-{soort}" href="{e(pad)}">{e(label)}</a>' for label, pad, soort in p["bestanden"]
    ) or '<span class="leeg">nog geen bestanden</span>'
    animaties = ""
    if p["animaties"]:
        rijen = "".join(f'<a href="{e(pad)}">{e(naam)}</a>' for naam, pad in p["animaties"])
        animaties = f'<div class="anim"><span class="lbl">Animaties</span>{rijen}</div>'
    waarschuwing = (
        ""
        if p["eindtermen"]
        else '<div class="mist">Geen eindtermenkoppeling — telt niet mee in het '
        f'dekkingsoverzicht. Typ <code>/eindtermen {html.escape(p["map"])}</code>.</div>'
    )
    return f"""
    <article class="kaart">
      <div class="kaart-kop">
        <h2>{e(p["titel"])}</h2>
        <span class="map mono">projecten/{e(p["map"])}/</span>
      </div>
      {waarschuwing}
      <p class="sam">{e(p["samenvatting"])}</p>
      <div class="files">{links}</div>
      {animaties}
    </article>"""


def bouw() -> str:
    lijst = projecten()
    kaarten = "\n".join(tegel(p) for p in lijst) or (
        '<article class="kaart leeg-kaart"><h2>Nog geen projecten</h2>'
        "<p class=\"sam\">Typ <code>/nieuw-project</code> in Claude Code om te beginnen.</p></article>"
    )
    return TEMPLATE.format(
        aantal=len(lijst),
        datum=date.today().strftime("%d-%m-%Y"),
        kaarten=kaarten,
    )


TEMPLATE = """<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lesmateriaal HAVO-P — Projecten</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root{{
    --board:#b9b1a1; --sheet:#fbfaf7; --ink:#22262b; --steel:#767e87;
    --blue:#1e5f8c; --red:#c43b2e; --amber:#b07a12; --line:#d7d3ca;
    --grid:rgba(30,95,140,.07);
  }}
  *{{box-sizing:border-box;}}
  body{{margin:0;background:var(--board);color:var(--ink);
    font-family:'Source Serif 4',Georgia,serif;font-size:17px;line-height:1.6;
    -webkit-font-smoothing:antialiased;}}
  .sheet{{max-width:1100px;margin:22px auto 44px;background:var(--sheet);
    background-image:linear-gradient(var(--grid) 1px,transparent 1px),
                     linear-gradient(90deg,var(--grid) 1px,transparent 1px);
    background-size:26px 26px;border:1px solid #8f8778;
    box-shadow:0 14px 40px rgba(0,0,0,.22);padding:14px;}}
  .frame{{border:1px solid var(--steel);padding:0 clamp(16px,4vw,40px) 40px;}}
  h1,h2{{font-family:'Archivo',system-ui,sans-serif;font-weight:700;line-height:1.15;margin:0;}}
  .mono{{font-family:'Space Mono',ui-monospace,monospace;}}
  a{{color:var(--blue);}}
  :focus-visible{{outline:2px solid var(--red);outline-offset:2px;}}

  .tb-top{{display:flex;justify-content:space-between;align-items:baseline;gap:16px;
    flex-wrap:wrap;border-bottom:2px solid var(--ink);padding:26px 0 14px;}}
  .eyebrow{{font-family:'Space Mono',monospace;font-size:.72rem;letter-spacing:.16em;
    text-transform:uppercase;color:var(--blue);}}
  .tb-top h1{{font-size:clamp(1.7rem,4.6vw,2.8rem);letter-spacing:-.02em;text-transform:uppercase;}}
  .tb-top .meta{{font-family:'Space Mono',monospace;font-size:.68rem;letter-spacing:.12em;
    text-transform:uppercase;color:var(--steel);text-align:right;}}

  .hoe{{border:1px solid var(--line);border-left:5px solid var(--blue);background:#eef4f8;
    padding:14px 18px;margin:22px 0 28px;}}
  .hoe h2{{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);
    font-family:'Space Mono',monospace;margin-bottom:8px;}}
  .hoe code{{font-family:'Space Mono',monospace;font-weight:700;background:#fff;
    border:1px solid var(--line);padding:1px 6px;font-size:.86rem;}}
  .hoe p{{margin:0 0 .4em;font-size:.97rem;}}
  .hoe p:last-child{{margin:0;}}

  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px;}}
  .kaart{{border:1px solid var(--line);background:var(--sheet);padding:0 0 14px;
    display:flex;flex-direction:column;animation:fadeUp .55s cubic-bezier(.2,.7,.3,1) both;}}
  .kaart-kop{{border-bottom:1px solid var(--line);background:#f4f2ec;padding:13px 16px;}}
  .kaart-kop h2{{font-size:1.14rem;margin-bottom:4px;}}
  .map{{font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--steel);}}
  .sam{{padding:12px 16px 4px;margin:0;font-size:.95rem;color:#3c434a;flex:1;}}
  .files{{display:flex;flex-wrap:wrap;gap:6px;padding:10px 16px 0;}}
  .f{{font-family:'Archivo',sans-serif;font-weight:600;font-size:.72rem;letter-spacing:.04em;
    text-transform:uppercase;text-decoration:none;padding:5px 10px;border:1px solid var(--line);
    color:var(--ink);background:#fff;}}
  .f:hover{{background:var(--blue);color:#fff;border-color:var(--blue);}}
  .f-html{{border-color:var(--blue);color:var(--blue);}}
  .f-pdf{{border-color:var(--red);color:var(--red);}}
  .f-pdf:hover{{background:var(--red);border-color:var(--red);}}
  .f-csv{{border-color:var(--amber);color:var(--amber);}}
  .f-csv:hover{{background:var(--amber);border-color:var(--amber);}}
  .anim{{padding:12px 16px 0;display:flex;flex-wrap:wrap;gap:8px;align-items:baseline;}}
  .anim .lbl{{font-family:'Space Mono',monospace;font-size:.6rem;letter-spacing:.14em;
    text-transform:uppercase;color:var(--steel);}}
  .anim a{{font-size:.86rem;}}
  .mist{{margin:0;padding:9px 16px;background:#fdf8ec;border-bottom:1px solid var(--line);
    font-size:.82rem;color:#7a5a10;}}
  .mist code{{font-family:'Space Mono',monospace;font-size:.78rem;background:#fff;
    border:1px solid var(--line);padding:0 4px;}}
  .leeg{{padding:0 16px;font-size:.86rem;color:var(--steel);font-style:italic;}}
  .leeg-kaart{{padding-bottom:18px;}}

  footer{{border-top:2px solid var(--ink);margin-top:46px;padding-top:14px;
    display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;
    font-family:'Space Mono',monospace;font-size:.66rem;letter-spacing:.1em;
    text-transform:uppercase;color:var(--steel);}}

  @keyframes fadeUp{{from{{opacity:0;transform:translateY(12px);}}to{{opacity:1;transform:none;}}}}
  @media (prefers-reduced-motion:reduce){{.kaart{{animation:none;}}}}
  @media (max-width:560px){{
    body{{font-size:16px;}}
    .sheet{{margin:0;border:none;padding:8px;}}
    .frame{{padding:0 14px 28px;}}
    .tb-top .meta{{text-align:left;}}
  }}
</style>
</head>
<body>
<div class="sheet"><div class="frame">

  <div class="tb-top">
    <div>
      <div class="eyebrow">HAVO-P · Techniek</div>
      <h1>Projecten</h1>
    </div>
    <div class="meta">{aantal} projecten<br>bijgewerkt {datum}</div>
  </div>

  <div class="hoe">
    <h2>Lesmateriaal HAVO-P</h2>
    <p>Dit is het publieke lesmateriaal bij het HAVO-P Profielproject. Open een project
       hieronder voor het volledige leerlingmateriaal, de opdrachtbladen en de rubric.</p>
    <p>Werk je aan een project zelf? Vul de bladen in — je antwoorden worden bewaard in
       je eigen browser, download je werk als PDF om in te leveren.</p>
  </div>

  <div class="grid">{kaarten}
  </div>

  <footer>
    <span>Lesmateriaal HAVO-P</span>
    <span>Techniek</span>
    <span>Gegenereerd {datum}</span>
  </footer>

</div></div>
</body>
</html>
"""


if __name__ == "__main__":
    doel = ROOT / "index.html"
    doel.write_text(bouw(), encoding="utf-8")
    n = len(projecten())
    print(f"index.html bijgewerkt — {n} project{'en' if n != 1 else ''}")
