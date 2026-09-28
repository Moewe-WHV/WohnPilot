# WohnPilot

WohnPilot ist ein kleines **Mieterportal**. Mieter melden sich an und sehen dort ihre Daten, Mietzahlungen, den Mietvertrag, die Nebenkostenabrechnung und ihre Dokumente. Sie können Zählerstände übermitteln und Schäden melden. Die Hausverwaltung pflegt die Daten am Anfang im Django-Admin.

Das ist unser Klassenprojekt (Umschulung FIAE, IBB Wilhelmshaven). Wir arbeiten mit **Scrum** in 5 Sprints à 1 Woche.

| Was | Womit |
|---|---|
| Sprache | Python |
| Framework | Django 5.2 |
| Datenbank | SQLite |
| Verwaltung | Git und GitHub |

## Setup

Du brauchst **Python ab Version 3.10** und Git. Prüfen mit `python3 --version` (Mac) oder `py --version` (Windows).

Die Befehle laufen im Projektordner, also dort, wo `requirements.txt` liegt.

### Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
```

Meldet PowerShell einen Fehler wegen der Ausführungsrichtlinie, gib einmal das ein und aktiviere dann nochmal:

```powershell
Set-ExecutionPolicy -Scope Process RemoteSigned
```

In der normalen Eingabeaufforderung (cmd) heißt der Aktivieren-Befehl `.venv\Scripts\activate.bat`.

### Testen, ob es geklappt hat

```bash
python -m django --version
```

Es muss eine Version `5.2.x` erscheinen. Vorne in der Zeile steht dann `(.venv)`.

## Wichtig

- Die virtuelle Umgebung `.venv` wird **nicht** eingecheckt. Sie steht in der `.gitignore`.
- Nach jedem Neustart des Terminals musst du `.venv` wieder aktivieren (nur der zweite Befehl).
- Beenden geht mit `deactivate`.
- `requirements.txt` enthält Django, `requirements-dev.txt` enthält zusätzlich flake8 und black.
- Die Doku liegt im Ordner `docs/`.
- Ordnerstruktur und Regeln stehen in [CONTRIBUTING.md](CONTRIBUTING.md).