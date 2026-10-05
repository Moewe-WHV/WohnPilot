# WohnPilot

WohnPilot ist ein kleines Mieterportal. Ein Mieter meldet sich an und sieht seine Daten, den Mietvertrag, die Mietzahlungen, die Nebenkostenabrechnung und seine Dokumente. Er kann außerdem Zählerstände abgeben und Schäden melden.

Wir bauen das erstmal als **Python-Programm im Terminal** mit einer **SQLite-Datenbank**. Eine Webseite oder andere Oberfläche (Frontend) lassen wir bewusst weg. Die kann später kommen, wenn die Grundlagen laufen.

Das ist unser Klassenprojekt (Umschulung FIAE, IBB). Wir sind 6 Leute und arbeiten mit Scrum in 5 Sprints à 1 Woche.

| Was | Womit |
|---|---|
| Programmiersprache | Python (ab 3.10) |
| Datenbank | SQLite (über das Modul `sqlite3`, SQL schreiben wir selbst) |
| Oberfläche | Terminal (Menü mit Eingaben) |
| Tests | pytest |
| Zusammenarbeit | Git und GitHub |V

## Wo finde ich was?

```text
WohnPilot/
├── README.md          hier startest du
├── CONTRIBUTING.md    unsere Regeln (Namen, Ordner, Git, Tests)
├── wohnpilot/         der Programmcode, ein Ordner pro Bereich
├── tests/             unsere Tests
├── requirements.txt   Pakete fürs Programm
├── requirements-dev.txt   Pakete zum Entwickeln (pytest, flake8, black)
└── docs/              Doku, Planung, Protokolle
```

| Ich will ... | Dann schaue ich in ... |
|---|---|
| wissen, worum es bei WohnPilot geht | [docs/readme/projektbeschreibung.md](docs/readme/projektbeschreibung.md) |
| wissen, wer welche Rolle hat | [docs/readme/rollen.md](docs/readme/rollen.md) |
| wissen, wie wir schätzen | [docs/readme/planning-poker.md](docs/readme/planning-poker.md) |
| wissen, was wir dokumentieren und entschieden haben | [docs/readme/dokumentation.md](docs/readme/dokumentation.md) |
| die Testfälle sehen | [docs/testing/testcases.md](docs/testing/testcases.md) |
| die Regeln für den Code nachlesen | [CONTRIBUTING.md](CONTRIBUTING.md) |
| alte Meetings nachlesen | [docs/meetings/](docs/meetings/) |

## Setup

Du brauchst Python ab Version 3.10 und Git. Prüfen kannst du das mit `python3 --version` (Mac) oder `py --version` (Windows).

Die Befehle laufen im Projektordner, also da, wo auch diese README liegt.

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

Wenn PowerShell wegen der Ausführungsrichtlinie meckert, gib einmal das hier ein und aktiviere danach nochmal:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

In der normalen Eingabeaufforderung (cmd) heißt der Befehl zum Aktivieren `.venv\Scripts\activate.bat`.

### Testen, ob es geklappt hat

```bash
pytest --version
```

Wenn eine Versionsnummer kommt, passt es. Vorne in der Zeile steht dann `(.venv)`.

### Programm starten

Die Startdatei legen wir in Sprint 1 an. Danach startest du das Programm mit:

```bash
python -m wohnpilot
```

### Tests starten

```bash
pytest
```

## Gut zu wissen

- Die `.venv` kommt nicht in Git, sie steht in der `.gitignore`. Die Datenbankdatei (`*.db`) auch nicht.
- In VS Code musst du nicht jedes Mal aktivieren. Einmal mit `Cmd+Shift+P` (Windows: `Strg+Shift+P`) **Python: Select Interpreter** öffnen und den Eintrag mit `.venv` nehmen. Neue Terminals aktivieren die Umgebung dann von selbst. Schon offene Terminals einmal schließen und neu öffnen.
- Im normalen Terminal (ohne VS Code) musst du nach jedem Neustart wieder aktivieren, also nur den zweiten Befehl von oben.
- Beenden geht mit `deactivate`.
- Die Hausverwaltung hat in Stufe 1 keine eigene Oberfläche. Die Daten (Wohnungen, Verträge, Zahlungen) legen wir mit einem Testdaten-Skript an. Es gibt nur erfundene Daten.
- Neu bei Git? Dann frag den Git-Wart, der hilft gern.
