# WohnPilot

WohnPilot ist ein kleines **Mieterportal**. Mieter melden sich an und sehen dort ihre Daten, Mietzahlungen, den Mietvertrag, die Nebenkostenabrechnung und ihre Dokumente. Sie können Zählerstände übermitteln und Schäden melden. Die Hausverwaltung pflegt die Daten am Anfang im Django-Admin. Die Oberfläche für die Mieter bauen wir mit **Angular**. Dahinter arbeitet **Django** und liefert die Daten über eine Schnittstelle (API).

Das ist unser Klassenprojekt (Umschulung FIAE, IBB Wilhelmshaven). Wir arbeiten mit **Scrum** in 5 Sprints à 1 Woche.

| Was | Womit |
|---|---|
| Backend (Daten, Regeln, Sicherheit) | Python, Django 5.2, Django REST Framework |
| Frontend (Oberfläche) | Angular (TypeScript) |
| Datenbank | SQLite |
| Verwaltung | Git und GitHub |

## Wo finde ich was?

```text
WohnPilot/
├── README.md          Hier startest du
├── CONTRIBUTING.md    Regeln: Namen, Ordner, Git, Tests
├── backend/           Python und Django: Daten, Regeln, API
│   ├── apps/          ein Ordner pro Bereich (zahlungen, nachrichten, ...)
│   ├── requirements.txt
│   └── ...            config/ und manage.py kommen in Aufgabe T03
├── frontend/          Angular: was der Mieter im Browser sieht (kommt in Aufgabe T04)
└── docs/              Dokumentation, Plan, Protokolle (Einstieg: docs/README.md)
```

Merke: **backend = Python, frontend = Angular, docs = Dokumentation.** Was du selbst anlegst (`.venv`, `node_modules`, `db.sqlite3`), steht in der `.gitignore` und landet nicht in Git.

| Ich will ... | Dann öffne ... |
|---|---|
| verstehen, was WohnPilot ist | [Projektbeschreibung](docs/projekt/projektbeschreibung.md) |
| wissen, was diese Woche dran ist | [Sprint-1-Aufgaben](docs/scrum/sprint-1-aufgaben.md) |
| wissen, wann etwas „fertig“ ist | [Sprintplanung](docs/scrum/sprintplanung.md) (Fertig-Liste) |
| Code-Regeln nachlesen | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Git und GitHub nachschlagen | [Git-Spickzettel](docs/git-spickzettel.md) |
| wissen, wer welche Rolle hat | [Rollen](docs/projekt/rollen.md) |

## Setup

Du brauchst **Python ab Version 3.10**, **Node.js** (aktuelle LTS-Version von nodejs.org, ältere Versionen lehnt Angular ab) und Git. Prüfen mit `python3 --version` (Mac) oder `py --version` (Windows) und mit `node --version`.

Die Befehle laufen im **Projektordner** (dem obersten Ordner, in dem auch diese `README.md` liegt). Erst richtest du das **Backend** ein (Python, Mac oder Windows), danach das **Frontend** (Angular, für beide gleich).

### Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements-dev.txt
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r backend/requirements-dev.txt
```

Meldet PowerShell einen Fehler wegen der Ausführungsrichtlinie, gib **einmal** das ein (gilt dann dauerhaft für deinen Benutzer) und aktiviere dann nochmal:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

In der normalen Eingabeaufforderung (cmd) heißt der Aktivieren-Befehl `.venv\Scripts\activate.bat`.

### Testen, ob es geklappt hat

```bash
python -m django --version
```

Es muss eine Version `5.2.x` erscheinen. Vorne in der Zeile steht dann `(.venv)`.

### Frontend einrichten (Angular)

Das Frontend liegt im Ordner `frontend/`. Er wird in Sprint 1 (Aufgabe T04) angelegt. Sobald er da ist, machen alle das Gleiche (Mac und Windows):

```bash
cd frontend
npm install
```

`npm install` lädt alles Nötige (auch Angular selbst) in den Ordner `node_modules/`. Der wird **nicht** eingecheckt, er steht schon in der `.gitignore`.

### Testen, ob das Frontend läuft

```bash
npm start
```

Im Browser unter `http://localhost:4200` muss die Angular-Startseite erscheinen. Beenden mit `Strg+C`.

### So startest du das ganze Projekt (zwei Terminals)

| Terminal | Befehl | Adresse |
|---|---|---|
| 1 – Backend (Django) | `cd backend` und dann `python manage.py runserver` (mit aktivierter `.venv`) | http://localhost:8000 |
| 2 – Frontend (Angular) | `cd frontend` und dann `npm start` | http://localhost:4200 |

Im Browser öffnest du immer **Angular** (Port 4200). Angular leitet alle Anfragen an `/api/...` über einen Proxy an Django (Port 8000) weiter. Den Django-Admin für die Hausverwaltung erreichst du direkt unter http://localhost:8000/admin.

## Wichtig

- Die virtuelle Umgebung `.venv` wird **nicht** eingecheckt. Sie steht in der `.gitignore`.
- **In VS Code musst du nicht jedes Mal aktivieren.** Einmal einstellen: `Cmd+Shift+P` (Windows: `Strg+Shift+P`), **Python: Select Interpreter** wählen und den Eintrag mit `.venv` nehmen. Jedes **neue** Terminal in VS Code aktiviert die Umgebung danach von selbst (vorne steht `(.venv)`). Schon offene Terminals einmal schließen und neu öffnen.
- In einem normalen Terminal (ohne VS Code) musst du `.venv` nach jedem Neustart wieder aktivieren (nur der zweite Befehl).
- Ohne Aktivieren geht es auch, wenn du den Python-Pfad direkt nimmst (im Ordner `backend`): `../.venv/bin/python manage.py runserver` (Mac) oder `..\.venv\Scripts\python manage.py runserver` (Windows).
- Beenden geht mit `deactivate`.
- Backend und Frontend laufen **gleichzeitig** in zwei Terminals. In VS Code öffnest du ein zweites Terminal mit dem `+` im Terminal-Fenster. Die `.venv` brauchst du nur im Backend-Terminal.
- `backend/requirements.txt` enthält Django und Django REST Framework, `backend/requirements-dev.txt` enthält zusätzlich flake8 und black.
- Die Doku liegt im Ordner `docs/` (Einstieg: [docs/README.md](docs/README.md)). Neu bei Git? Der [Git-Spickzettel](docs/git-spickzettel.md) hilft.
- Ordnerstruktur und Regeln stehen in [CONTRIBUTING.md](CONTRIBUTING.md).