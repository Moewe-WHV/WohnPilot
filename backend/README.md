# Backend (Python, Django)

Hier liegt alles, was im Hintergrund läuft: Datenbank, Regeln, Anmeldung und die API, die Angular abfragt.

- `apps/` – ein Ordner pro Bereich (Zahlungen, Nachrichten, ...)
- `config/` und `manage.py` – kommen in Aufgabe T03 dazu
- `requirements.txt` – die Python-Pakete, `requirements-dev.txt` zusätzlich flake8 und black

Alle Django-Befehle laufen **in diesem Ordner** (`cd backend`) und mit aktivierter `.venv`:

```bash
python manage.py runserver   # Backend starten, http://localhost:8000
python manage.py test        # Tests
```

Setup und Regeln: [README.md](../README.md) und [CONTRIBUTING.md](../CONTRIBUTING.md).
