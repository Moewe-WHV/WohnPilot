# Programmierguide – WohnPilot

Das ist unser gemeinsamer Guide. Er soll helfen, dass unser Code überall ähnlich aussieht, auch wenn 10 Leute daran arbeiten. Er ist kurz, damit ihn auch jemand liest.

## 1. Grundsätze
- **Lesbar vor clever.** Wenn du den Code in 3 Monaten noch verstehst, ist er gut.
- **Klein anfangen.** Erst läuft es, dann wird es schön.
- **Nicht alles selbst bauen.** Django kann vieles schon (Login, Formulare, Admin). Erst nachschauen, dann bauen.
- **Fragen kostet nichts.** Nach 20 Minuten Festhängen holen wir Hilfe.

## 2. Namen
| Was | Schreibweise | Beispiel |
|---|---|---|
| Variablen, Funktionen | `kleinbuchstaben_mit_unterstrich` | `offene_zahlungen`, `berechne_summe()` |
| Klassen (Models, Views, Forms) | `GrossBuchstabenAmAnfang` | `Zahlung`, `ZahlungListView` |
| Konstanten | `GROSS_MIT_UNTERSTRICH` | `MAX_DATEIGROESSE` |
| Dateien | klein, mit Unterstrich | `test_views.py` |

- **Sprache:** Namen im Projekt auf **Deutsch** (wie im Fachbegriff: `Mieter`, `Zahlung`), damit alle sie verstehen. Kommentare auch auf Deutsch.
- Namen sollen **aussagekräftig** sein: `zahlung` statt `z`, `mieter_liste` statt `liste1`.

## 3. Ordnerstruktur
Jeder Bereich ist eine eigene Django-App im Ordner `apps/`:

```text
wohnpilot/
├── config/           Einstellungen und Haupt-URLs
├── apps/
│   ├── accounts/     Anmelden, Mieter-Profil
│   ├── wohnungen/    Wohnungen
│   ├── mietvertraege/
│   ├── zahlungen/
│   ├── nebenkosten/
│   ├── zaehlerstaende/
│   ├── dokumente/
│   ├── wartungsmeldungen/
│   └── nachrichten/
├── templates/        gemeinsame Seitenvorlagen (base.html)
├── static/           CSS, Bilder
├── docs/             unsere Dokumentation
└── manage.py
```

Jede App hat: `models.py` (Tabellen), `views.py` (was passiert auf einer Seite), `urls.py` (Adressen), `forms.py` (Eingabeformulare), `tests.py` (Tests) und ihre Templates unter `templates/<appname>/`.

**Welche App ist wofür zuständig?**

| App | Zuständig für | Stories |
|---|---|---|
| `accounts` | Anmelden, Abmelden, Mieter-Profil | US09, US01 |
| `wohnungen` | Wohnungen (Grundlage für den Mietvertrag) | – |
| `mietvertraege` | Mietvertrag ansehen | US02 |
| `zahlungen` | Mietzahlungen, offene Beträge | US03 |
| `nebenkosten` | Nebenkostenabrechnung ansehen, als PDF laden | US04, US05 |
| `zaehlerstaende` | Zählerstände übermitteln | US06 |
| `dokumente` | Dokumente ansehen und herunterladen | US10 |
| `wartungsmeldungen` | Wartungs- und Schadensmeldung | US07 |
| `nachrichten` | Nachrichten der Hausverwaltung | US08 |

Die Ordner in `apps/` gibt es schon (jeweils mit einer leeren `.gitkeep`). `config/` und `manage.py` entstehen erst beim Anlegen des Django-Projekts (Sprint 1, Aufgabe T03).

**So legst du eine App an** (Beispiel `accounts`, einmal pro App, nicht jeder für sich):

```bash
python manage.py startapp accounts apps/accounts
```

Danach zwei Änderungen, sonst findet Django die App nicht:
1. In `apps/accounts/apps.py` den Namen ändern: `name = "apps.accounts"`
2. In `config/settings.py` bei `INSTALLED_APPS` eintragen: `"apps.accounts"`

## 4. Regeln für Django
1. **Geld immer mit `DecimalField`,** nie mit Kommazahlen (`float`). Sonst gibt es Rundungsfehler.
2. **Jeder Mieter sieht nur seine eigenen Daten.** Jede Abfrage muss auf den angemeldeten Benutzer filtern:
   ```python
   class ZahlungListView(ListView):
       model = Zahlung

       def get_queryset(self):
           # Nur Zahlungen aus Verträgen des angemeldeten Mieters
           return Zahlung.objects.filter(mietvertrag__mieter__user=self.request.user)
   ```
3. **Nie nur die ID aus der Adresse nehmen.** Sonst kann Ben die Adresse von Annas Dokument aufrufen. Immer prüfen, ob es dem angemeldeten Benutzer gehört (bei Fremden: Fehler 404).
4. **Jedes Formular braucht `{% csrf_token %}`.**
5. **Eingaben prüfen** (z. B. Zählerstand nicht negativ) im Formular, nicht per Hand.
6. **Rechnen und Logik nicht ins Template.** Templates zeigen nur an.
7. **Tabellen ändern nur nach Absprache mit dem Datenbank-Wart.** Danach `python manage.py makemigrations` und die neue Migrationsdatei mit in den Pull Request nehmen.

## 5. Kommentare
- Kommentiere das **Warum**, nicht das Offensichtliche.
- Schlecht: `# Datum prüfen`
- Besser: `# Zählerstände dürfen nicht in der Zukunft liegen, sonst stimmt die Abrechnung nicht`
- Jede Funktion mit etwas Logik bekommt einen kurzen Satz als Beschreibung (Docstring).

## 6. Git-Regeln
- **Nie direkt auf `main` arbeiten.**
- **Branch-Name:** `feature/<aufgabe>-<thema>`, z. B. `feature/t08-login`. Für Fehler: `bugfix/<thema>`.
- **Commit-Nachricht:** Anfangswort + Doppelpunkt + kurzer Satz.

| Anfang | Bedeutung | Beispiel |
|---|---|---|
| `feat:` | neue Funktion | `feat: Zahlungsliste zeigt Betrag und Status` |
| `fix:` | Fehler behoben | `fix: Überfällig wird richtig erkannt` |
| `test:` | Test dazu | `test: Ben sieht keine Zahlungen von Anna` |
| `docs:` | nur Doku | `docs: Setup im README ergänzt` |

- **Kleine Commits** sind besser als ein riesiger am Ende.
- **Pull Request (PR):** Titel mit Aufgabe, kurze Beschreibung: *Was ist neu? Wie habe ich es getestet?* Ein anderes Paar prüft ihn. Erst nach dem OK wird gemergt.
- Nach dem Merge: `git checkout main` und `git pull`.

## 7. Tests
- **Pro Story mindestens ein Test.**
- Immer auch testen: *Sieht Ben nichts von Annas Daten?*
- Tests starten mit `python manage.py test`.
- Ein Test besteht aus: **Vorbereiten** (Anna und Ben anlegen), **Ausführen** (Seite aufrufen), **Prüfen** (stimmt das Ergebnis?).

## 8. Code-Stil
- Wir nutzen `flake8` (prüft) und `black` (formatiert).
- Vor jedem Pull Request laufen lassen:
  ```bash
  black .
  flake8
  python manage.py test
  ```
- Zeilen sind höchstens 88 Zeichen lang.

## 9. Datenschutz und Sicherheit
- **Nur erfundene Testdaten.** Keine echten Namen, Adressen oder Vertragsdaten.
- **Keine Passwörter im Code** und keine Zugangsdaten im GitHub.
- Diese Dateien gehören **nicht** ins Git: `db.sqlite3`, `.venv`, hochgeladene Dateien.
- Passwörter speichert Django gesichert (verschlüsselt) ab. Wir bauen dafür nichts Eigenes.
- Dateien der Mieter werden nur über eine Seite ausgeliefert, die vorher prüft, wem sie gehört.

## 10. Wann ist etwas fertig?
Wir nutzen die **Fertig-Liste** aus [sprintplanung.md](docs/teamleitung/sprintplanung.md). Kurz: Kriterien erfüllt, selbst ausprobiert, nur eigene Daten sichtbar, Test grün, Stil geprüft, Pull Request freigegeben, Doku angepasst.

## 11. Wenn ich unsicher bin
1. Ins Glossar oder in die Django-Doku schauen.
2. Partner fragen.
3. Nachbarpaar oder den passenden Hut fragen (Git-Wart, Test-Wart, ...).
4. Teamleitung fragen.
