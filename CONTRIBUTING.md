# Programmierguide WohnPilot

Das ist unser gemeinsamer Guide. Er soll dafür sorgen, dass unser Code überall ähnlich aussieht, auch wenn mehrere Paare daran arbeiten. Er ist extra kurz gehalten, damit ihn auch jemand liest.

## 1. Grundsätze
- Lesbar ist wichtiger als clever. Wenn du den Code in 3 Monaten noch verstehst, ist er gut.
- Erst mal klein anfangen. Erst läuft es, dann machen wir es schön.
- Python kann schon viel von selbst (z. B. `sqlite3`, `hashlib`, `datetime`). Erst in der Doku nachschauen, dann selber bauen.
- Fragen kostet nichts. Wenn du nach 20 Minuten nicht weiterkommst, holst du dir Hilfe.

## 2. Namen
| Was | Schreibweise | Beispiel |
|---|---|---|
| Variablen, Funktionen | `kleinbuchstaben_mit_unterstrich` | `offene_zahlungen`, `berechne_summe()` |
| Klassen | `GrossBuchstabenAmAnfang` | `Zahlung`, `Mieter` |
| Konstanten | `GROSS_MIT_UNTERSTRICH` | `MAX_DATEIGROESSE` |
| Dateien und Ordner | klein, mit Unterstrich | `test_zahlungen.py` |

- Die Namen schreiben wir auf Deutsch, so wie die Fachbegriffe (`mieter`, `zahlung`). Kommentare auch auf Deutsch.
- Namen sollen etwas aussagen: `zahlung` statt `z`, `mieter_liste` statt `liste1`.

## 3. Ordnerstruktur
Jeder Bereich hat einen eigenen Ordner in `wohnpilot/`:

```text
WohnPilot/
├── wohnpilot/
│   ├── konto/              Anmelden, Mieter-Profil
│   ├── wohnungen/          Wohnungen
│   ├── mietvertraege/
│   ├── zahlungen/
│   ├── nebenkosten/
│   ├── zaehlerstaende/
│   ├── dokumente/
│   ├── wartungsmeldungen/
│   └── nachrichten/
├── tests/                  Tests, eine Datei pro Bereich
└── docs/                   unsere Doku
```

Welcher Ordner für was zuständig ist:

| Ordner | Zuständig für | Stories |
|---|---|---|
| `konto` | Anmelden, Abmelden, Mieter-Profil | US09, US01 |
| `wohnungen` | Wohnungen (Grundlage für den Mietvertrag) | - |
| `mietvertraege` | Mietvertrag ansehen | US02 |
| `zahlungen` | Mietzahlungen, offene Beträge | US03 |
| `nebenkosten` | Nebenkostenabrechnung ansehen, als PDF laden | US04, US05 |
| `zaehlerstaende` | Zählerstände abgeben | US06 |
| `dokumente` | Dokumente ansehen und herunterladen | US10 |
| `wartungsmeldungen` | Wartungs- und Schadensmeldung | US07 |
| `nachrichten` | Nachrichten der Hausverwaltung | US08 |

Die Ordner gibt es schon, jeweils mit einer leeren `.gitkeep`. Sobald du die erste Datei in einen Ordner legst, kann die `.gitkeep` weg. Lege dann auch eine leere `__init__.py` an, damit Python den Ordner als Paket erkennt.

Pro Bereich teilen wir den Code in zwei Dateien:
- `daten.py`: alles mit SQL (speichern, lesen, ändern)
- `ansicht.py`: alles, was etwas im Terminal ausgibt oder abfragt (`print`, `input`)

So steht kein SQL mitten in der Ausgabe und wir können die Datenfunktionen einzeln testen.

Die Tabellen der Datenbank stehen an einer Stelle: `wohnpilot/schema.sql`. Die Datenbankdatei selbst (`wohnpilot.db`) liegt nicht in Git.

## 4. Regeln für Datenbank und Sicherheit
1. **Geld speichern wir in Cent als ganze Zahl (`INTEGER`),** nie als Kommazahl (`float`). 12,50 Euro sind also `1250`. Sonst gibt es Rundungsfehler. Angezeigt wird es erst bei der Ausgabe als Euro.
2. **Jeder Mieter sieht nur seine eigenen Daten.** Jede Abfrage muss auf den angemeldeten Mieter filtern:
   ```python
   def offene_zahlungen(verbindung, mieter_id):
       # Nur Zahlungen aus Verträgen des angemeldeten Mieters
       abfrage = """
           SELECT z.id, z.betrag_cent, z.faellig_am
           FROM zahlung z
           JOIN mietvertrag m ON m.id = z.mietvertrag_id
           WHERE m.mieter_id = ? AND z.status = 'offen'
       """
       return verbindung.execute(abfrage, (mieter_id,)).fetchall()
   ```
3. **Nie nur die ID nehmen, die der Benutzer eintippt.** Sonst kann Ben die Nummer von Annas Dokument eingeben und es öffnen. Immer prüfen, ob der Datensatz dem angemeldeten Mieter gehört. Wenn nicht, sagen wir nur "nicht gefunden".
4. **SQL nur mit Platzhaltern (`?`) schreiben,** nie Eingaben mit f-Strings oder `+` in die Abfrage kleben. Sonst ist unser Programm offen für SQL-Injection.
   ```python
   # Falsch
   verbindung.execute(f"SELECT * FROM mieter WHERE name = '{name}'")
   # Richtig
   verbindung.execute("SELECT * FROM mieter WHERE name = ?", (name,))
   ```
5. **Passwörter nie im Klartext speichern.** Wir speichern nur einen Hash mit Salt (Modul `hashlib`, Funktion `pbkdf2_hmac`) und vergleichen beim Anmelden die Hashes. Das bauen wir einmal im Bereich `konto` und alle anderen nutzen es.
6. **Eingaben prüfen,** bevor sie in die Datenbank gehen (z. B. Zählerstand nicht negativ, Datum nicht in der Zukunft). Die Prüfung steht in einer eigenen Funktion, die man testen kann.
7. **Anzeige und Rechnen trennen.** Eine Funktion rechnet oder holt Daten, eine andere gibt aus.
8. **Tabellen ändern nur nach Absprache mit dem Datenbank-Wart.** Sonst haben wir plötzlich zwei verschiedene Datenbanken. Die Änderung kommt in `schema.sql` und wird im Pull Request erklärt.
9. **Die Datenbankverbindung immer wieder schließen.** Am einfachsten geht das mit `with`.

## 5. Kommentare
- Kommentiere das Warum, nicht das Offensichtliche.
- Schlecht: `# Datum prüfen`
- Besser: `# Zählerstände dürfen nicht in der Zukunft liegen, sonst stimmt die Abrechnung nicht`
- Jede Funktion mit etwas Logik bekommt einen kurzen Satz als Beschreibung (Docstring).

## 6. Git-Regeln
- Nie direkt auf `main` arbeiten.
- Branch-Name: `feature/<aufgabe>-<thema>`, z. B. `feature/t08-login`. Für Fehler: `bugfix/<thema>`.
- Commit-Nachricht: Anfangswort, Doppelpunkt, kurzer Satz.

| Anfang | Bedeutung | Beispiel |
|---|---|---|
| `feat:` | neue Funktion | `feat: Zahlungsliste zeigt Betrag und Status` |
| `fix:` | Fehler behoben | `fix: Überfällig wird richtig erkannt` |
| `test:` | Test dazu | `test: Ben sieht keine Zahlungen von Anna` |
| `docs:` | nur Doku | `docs: Setup im README ergänzt` |

- Lieber viele kleine Commits als einen riesigen am Ende.
- Pull Request (PR): Titel mit der Aufgabe und eine kurze Beschreibung: Was ist neu? Wie habe ich es getestet? Ein anderes Paar schaut drüber. Erst nach dem OK wird gemergt.
- Nach dem Merge: `git checkout main` und `git pull`.

## 7. Tests
- Pro Story mindestens ein Test.
- Immer auch prüfen: Sieht Ben nichts von Annas Daten?
- Tests starten mit `pytest`.
- Die Testdateien liegen in `tests/` und heißen `test_<bereich>.py`.
- Tests nutzen eine eigene Datenbank im Speicher (`sqlite3.connect(":memory:")`). Die echte Datenbankdatei fassen wir in Tests nicht an.
- Ein Test hat drei Teile: Vorbereiten (Anna und Ben anlegen), Ausführen (Funktion aufrufen), Prüfen (stimmt das Ergebnis?).

## 8. Code-Stil
- Wir nutzen `flake8` (prüft) und `black` (formatiert).
- Vor jedem Pull Request laufen lassen:
  ```bash
  black .
  flake8
  pytest
  ```
- Zeilen sind höchstens 88 Zeichen lang.

## 9. Datenschutz
- Wir nehmen nur erfundene Testdaten. Keine echten Namen, Adressen oder Vertragsdaten.
- Keine Passwörter im Code und keine Zugangsdaten im GitHub.
- Diese Dateien kommen nicht ins Git: `*.db`, `.venv`, hochgeladene oder erzeugte Dateien.
- Dateien von Mietern geben wir nur heraus, wenn vorher geprüft wurde, wem sie gehören.

## 10. Wann ist etwas fertig?
Eine Story ist fertig, wenn:
- die Kriterien der Story erfüllt sind,
- wir es selbst ausprobiert haben,
- nur die eigenen Daten des Mieters sichtbar sind,
- die Tests grün sind,
- `black` und `flake8` nichts mehr melden,
- der Pull Request von einem anderen Paar freigegeben ist,
- und die Doku angepasst ist, falls sich etwas geändert hat.

## 11. Wenn ich nicht weiter weiß
1. In der Python-Doku oder im Glossar nachschauen.
2. Den Partner fragen.
3. Das andere Paar oder den passenden Hut fragen (Git-Wart, Test-Wart, ...).
4. Die Teamleitung fragen.
