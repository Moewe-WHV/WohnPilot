# Programmierguide – WohnPilot

Das ist unser gemeinsamer Guide. Er soll helfen, dass unser Code überall ähnlich aussieht, auch wenn 10 Leute daran arbeiten. Er ist kurz, damit ihn auch jemand liest.

## 1. Grundsätze
- **Lesbar vor clever.** Wenn du den Code in 3 Monaten noch verstehst, ist er gut.
- **Klein anfangen.** Erst läuft es, dann wird es schön.
- **Nicht alles selbst bauen.** Django und Angular können vieles schon (Login, Datenbank, Admin, Routing). Erst nachschauen, dann bauen.
- **Fragen kostet nichts.** Nach 20 Minuten Festhängen holen wir Hilfe.

## 2. Namen
| Was | Schreibweise | Beispiel |
|---|---|---|
| Variablen, Funktionen | `kleinbuchstaben_mit_unterstrich` | `offene_zahlungen`, `berechne_summe()` |
| Klassen (Models, Views, Forms) | `GrossBuchstabenAmAnfang` | `Zahlung`, `ZahlungListView` |
| Konstanten | `GROSS_MIT_UNTERSTRICH` | `MAX_DATEIGROESSE` |
| Dateien (Python) | klein, mit Unterstrich | `test_views.py` |
| Dateien (Angular) | klein, mit Bindestrich | `zahlungen-liste.component.ts` |
| Klassen (Angular: Komponenten, Services) | `GrossBuchstabenAmAnfang` | `ZahlungenListeComponent`, `ZahlungService` |
| Variablen, Funktionen (TypeScript) | `kleinUndGrossInDerMitte` | `offeneZahlungen`, `holeZahlungen()` |

- **Sprache:** Namen im Projekt auf **Deutsch** (wie im Fachbegriff: `Mieter`, `Zahlung`), damit alle sie verstehen. Kommentare auch auf Deutsch.
- Namen sollen **aussagekräftig** sein: `zahlung` statt `z`, `mieter_liste` statt `liste1`.
- Python und TypeScript schreiben Variablen verschieden (Unterstrich oder Großbuchstabe in der Mitte). Das ist normal, jede Sprache hat ihre Regel. Felder, die aus der API kommen, behalten ihren Namen (`mietvertrag_id`), damit wir nicht umbauen müssen.

## 3. Ordnerstruktur
Unser Projekt hat zwei Teile: das **Backend** (Django, liefert die Daten und prüft alles) und das **Frontend** (Angular, das sieht der Mieter im Browser).

Ein Vergleich: Angular ist der Tresen im Laden, an dem Familie Beispiel fragt: „Zeig mir meine Zahlungen.“ Django ist das Lager dahinter. Es prüft, wer da fragt, und gibt nur heraus, was dieser Person gehört. Dazwischen läuft die **API**: Angular schickt eine Anfrage an eine Adresse wie `/api/zahlungen/`, Django antwortet mit den Daten als **JSON** (ein einfaches Textformat für Daten).

Im Backend ist jeder Bereich eine eigene Django-App im Ordner `backend/apps/`:

```text
WohnPilot/
├── backend/          Python und Django
│   ├── apps/         eine Django-App pro Bereich
│   │   ├── accounts/     Anmelden, Mieter-Profil
│   │   ├── wohnungen/    Wohnungen
│   │   ├── mietvertraege/
│   │   ├── zahlungen/
│   │   ├── nebenkosten/
│   │   ├── zaehlerstaende/
│   │   ├── dokumente/
│   │   ├── wartungsmeldungen/
│   │   └── nachrichten/
│   ├── config/       Einstellungen und Haupt-URLs (entsteht in T03)
│   ├── manage.py     (entsteht in T03)
│   ├── templates/    Django-Vorlagen (die Oberfläche baut Angular, hier liegt nur, was Django selbst braucht)
│   ├── static/       Dateien, die Django ausliefert
│   └── requirements.txt
├── frontend/         Angular (entsteht in T04)
└── docs/             unsere Dokumentation
```

Jede Django-App hat: `models.py` (Tabellen), `serializers.py` (macht aus Tabellen-Daten JSON und prüft Eingaben), `views.py` (was bei einer Anfrage passiert), `urls.py` (Adressen, alle unter `/api/`) und `tests.py` (Tests). Seiten und Formulare für den Mieter baut **Angular**, nicht Django.

Im Frontend (`frontend/src/app/`) bekommt jeder Bereich wie im Backend einen eigenen Ordner, z. B. `zahlungen/` mit `zahlungen-liste.component.ts` und `zahlung.service.ts`. Gemeinsames (Menü, Login, Sperre für nicht angemeldete Besucher) liegt in `kern/`. Die Ordner legen wir an, wenn die Story dran ist, nicht alle im Voraus.

**Merkregel:** Django-Befehle (`python manage.py ...`) laufen immer im Ordner `backend/`, Angular-Befehle (`npm ...`, `npx ng ...`) immer im Ordner `frontend/`. Git-Befehle laufen im Projektordner (oder einem Unterordner, das ist egal).

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

**Jede Story hat zwei Teile:** die API (in der Django-App) und die Seite (in Angular). Wer die Story baut, macht beides, oder das Paar teilt sich die Arbeit (einer API, einer Angular). Abgesprochen wird über die Endpunkt-Liste in [api.md](docs/design/api.md).

Die Ordner in `backend/apps/` gibt es schon (jeweils mit einer leeren `.gitkeep`). `backend/config/` und `backend/manage.py` entstehen erst beim Anlegen des Django-Projekts (Sprint 1, Aufgabe T03). Der Ordner `frontend/` entsteht mit dem Angular-Projekt (Sprint 1, Aufgabe T04).

**So legst du eine App an** (Beispiel `accounts`, einmal pro App, nicht jeder für sich):

```bash
cd backend
python manage.py startapp accounts apps/accounts
```

Danach zwei Änderungen, sonst findet Django die App nicht:
1. In `backend/apps/accounts/apps.py` den Namen ändern: `name = "apps.accounts"`
2. In `backend/config/settings.py` bei `INSTALLED_APPS` eintragen: `"apps.accounts"`

Einmalig für das ganze Projekt (macht T03): `"rest_framework"` ebenfalls bei `INSTALLED_APPS` eintragen.

## 4. Regeln für Django und die API
1. **Geld immer mit `DecimalField`,** nie mit Kommazahlen (`float`). Sonst gibt es Rundungsfehler.
2. **Jeder Mieter sieht nur seine eigenen Daten.** Jede Abfrage muss auf den angemeldeten Benutzer filtern:
   ```python
   class ZahlungListView(ListAPIView):
       serializer_class = ZahlungSerializer

       def get_queryset(self):
           # Nur Zahlungen aus Verträgen des angemeldeten Mieters
           return Zahlung.objects.filter(mietvertrag__mieter__user=self.request.user)
   ```
3. **Nie nur die ID aus der Adresse nehmen.** Sonst kann Ben die API-Adresse von Annas Dokument aufrufen (das geht auch ohne Angular, direkt im Browser). Immer prüfen, ob es dem angemeldeten Benutzer gehört (bei Fremden: Fehler 404).
4. **Die Sicherheit sitzt im Backend.** Jede API-Adresse außer der Anmeldung verlangt eine Anmeldung. Das stellen wir einmal zentral in den Einstellungen ein (Aufgabe T11). Was Angular versteckt, ist dadurch noch nicht geschützt.
5. **Schreibende Anfragen (Anlegen, Ändern, Löschen) brauchen CSRF-Schutz,** wenn wir die Anmeldung per Cookie machen. Wie Angular und Django das zusammen erledigen, richten wir **einmal zentral** ein (Aufgabe T10), nicht in jeder Komponente.
6. **Eingaben im Serializer prüfen** (z. B. Zählerstand nicht negativ), nicht per Hand. Angular prüft zusätzlich, damit der Mieter sofort eine Meldung sieht. Das Backend verlässt sich darauf aber nie.
7. **Rechnen und Logik gehören ins Backend.** Angular zeigt nur an.
8. **Tabellen ändern nur nach Absprache mit dem Datenbank-Wart.** Danach `python manage.py makemigrations` und die neue Migrationsdatei mit in den Pull Request nehmen.
9. **Jeder Endpunkt steht in [api.md](docs/design/api.md).** Wer einen baut oder ändert, trägt ihn dort ein. Sonst muss das Frontend raten.

## 5. Regeln für Angular
1. **Anlegen mit `ng generate`,** nicht von Hand kopieren: `npx ng generate component zahlungen/zahlungen-liste`.
2. **Daten holen nur in einem Service** (mit `HttpClient`). Die Komponente ruft den Service auf und zeigt an. Beispiel:
   ```ts
   @Injectable({ providedIn: 'root' })
   export class ZahlungService {
     private http = inject(HttpClient);

     holeZahlungen() {
       return this.http.get<Zahlung[]>('/api/zahlungen/');
     }
   }
   ```
3. **Für jede API-Antwort ein Interface** (z. B. `Zahlung`), kein `any`. Die Feldnamen bleiben so, wie die API sie liefert.
4. **Geldbeträge kommen als Text** (`"12.50"`) aus der API. In Angular nur anzeigen (z. B. mit der `currency`-Pipe), **nicht** damit rechnen. Summen rechnet das Backend.
5. **Ein Guard versteckt nur eine Seite,** er schützt keine Daten. Geschützt wird im Backend (Abschnitt 4).
6. **Fehler und Warten zeigen.** Schlägt eine Anfrage fehl oder dauert sie, sieht der Mieter eine verständliche Meldung statt einer leeren Seite.
7. **Nichts Geheimes im Angular-Code.** Alles, was im Browser läuft, kann jeder ansehen. Keine Passwörter oder Schlüssel, auch nicht in `environment`-Dateien.
8. **Klein halten.** Eine Komponente macht eine Sache (Liste, Detail oder Formular). Die Logik gehört in den Service, das Aussehen in `.html` und `.css`.

## 6. Kommentare
- Kommentiere das **Warum**, nicht das Offensichtliche.
- Schlecht: `# Datum prüfen`
- Besser: `# Zählerstände dürfen nicht in der Zukunft liegen, sonst stimmt die Abrechnung nicht`
- Jede Funktion mit etwas Logik bekommt einen kurzen Satz als Beschreibung (Docstring).

## 7. Git-Regeln
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

## 8. Tests
- **Pro Story mindestens ein Test.**
- Immer auch testen: *Sieht Ben nichts von Annas Daten?* Das testen wir an der **API** (Backend-Test), denn dort sitzt die Sicherheit.
- Backend-Tests starten mit `python manage.py test` (im Ordner `backend`).
- Frontend-Tests starten mit `npm test` (im Ordner `frontend`). Jede neue Angular-Komponente behält mindestens den Test, den `ng generate` anlegt, und er muss grün sein.
- Ein Test besteht aus: **Vorbereiten** (Anna und Ben anlegen), **Ausführen** (Seite aufrufen), **Prüfen** (stimmt das Ergebnis?).

## 9. Code-Stil
- Python: `flake8` (prüft) und `black` (formatiert). Angular und TypeScript: `prettier` (formatiert).
- Vor jedem Pull Request laufen lassen:
  ```bash
  cd backend
  black .
  flake8
  python manage.py test
  cd ../frontend
  npx prettier --write src
  npm test
  ```
- Python-Zeilen sind höchstens 88 Zeichen lang. Für Angular gelten die Prettier-Einstellungen aus dem Projekt (`ng new` bringt sie mit).

## 10. Datenschutz und Sicherheit
- **Nur erfundene Testdaten.** Keine echten Namen, Adressen oder Vertragsdaten.
- **Keine Passwörter im Code** und keine Zugangsdaten im GitHub.
- Diese Dateien gehören **nicht** ins Git: `db.sqlite3`, `.venv`, `node_modules`, hochgeladene Dateien.
- Passwörter speichert Django gesichert (verschlüsselt) ab. Wir bauen dafür nichts Eigenes.
- Dateien der Mieter werden nur über einen API-Endpunkt ausgeliefert, der vorher prüft, wem sie gehören.
- Nichts Geheimes im Angular-Code (siehe Abschnitt 5).

## 11. Wann ist etwas fertig?
Wir nutzen die **Fertig-Liste** aus [sprintplanung.md](docs/scrum/sprintplanung.md). Kurz: Kriterien erfüllt, selbst ausprobiert, nur eigene Daten sichtbar, Test grün, Stil geprüft, Pull Request freigegeben, Doku angepasst.

## 12. Wenn ich unsicher bin
1. Ins Glossar oder in die Doku schauen (Django, Django REST Framework, Angular: angular.dev).
2. Partner fragen.
3. Nachbarpaar oder den passenden Hut fragen (Git-Wart, Test-Wart, ...).
4. Teamleitung fragen.
