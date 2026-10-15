#!/usr/bin/env python3
"""
Confere toda citação de uma sessão d'O Conselho contra os cérebros das cadeiras.

Uso:
  python3 .claude/skills/o-conselho/scripts/check_quotes.py <pasta da sessão>

Varre rodada-*.md e veredito.md atrás de citações atribuídas a um id de fonte,
como "..." (S095), e procura cada uma nos arquivos dos cérebros. Uma citação que
não está em nenhum cérebro é ou citação de outra cadeira/do fundador (ok se
aparece numa rodada anterior ou no briefing) ou citação inventada (marque e
remova do veredito). Sai com código 1 se alguma citação não for encontrada.

Adaptado de roast-room (MIT, AI Automation Society).
"""
import re
import sys
import unicodedata
from pathlib import Path

BRAINS = Path(__file__).resolve().parents[1] / "brains"


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[^a-z0-9' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    session = Path(sys.argv[1])
    brain_text = norm(" ".join(p.read_text(encoding="utf-8", errors="replace") for p in BRAINS.rglob("*.md")))
    session_files = sorted(session.glob("rodada-*.md")) + [p for p in [session / "veredito.md"] if p.exists()]
    brief = norm((session / "briefing.md").read_text(encoding="utf-8")) if (session / "briefing.md").exists() else ""
    bad, ok, internal = [], 0, 0
    seen_session = ""
    for f in session_files:
        text = f.read_text(encoding="utf-8", errors="replace")
        for q in re.findall(r"[\"“]([^\"“”\n]{20,400})[\"”][^\n\"]{0,40}?[\(\[]S\d{3}", text):
            nq = norm(q)
            if len(nq.split()) < 6:
                continue
            if nq in brain_text:
                ok += 1
            elif nq in seen_session or nq in brief:
                internal += 1
            else:
                bad.append((f.name, q))
        seen_session += " " + norm(text)
    print(f"citações verificadas nos cérebros: {ok}; citações de rodadas anteriores ou do briefing: {internal}; não verificadas: {len(bad)}")
    for name, q in bad:
        print(f"  NÃO VERIFICADA [{name}] \"{q[:160]}\"")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
