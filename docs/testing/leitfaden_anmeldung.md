# Leitfaden: Anmeldung bauen und testen (US09)

Dieser Leitfaden ist eine Lernhilfe, keine Lösung. Er sagt dir, **was** du in welcher Reihenfolge tun kannst und **worüber du nachdenken solltest**. Den Code schreibst du selbst.

Grundlage sind die Testfälle `anmelden_01` und `anmelden_02` in [testcases.md](testcases.md) und die Regeln in [CONTRIBUTING.md](../../CONTRIBUTING.md).

---

## 1. Das große Bild

Die Anmeldung hat drei Schichten. Jede hat eine eigene Aufgabe und wird anders getestet.

| Schicht | Datei | Aufgabe | Wie testen? |
|---|---|---|---|
| Ein-/Ausgabe | `konto/ansicht.py` | `input()`, `getpass()`, `print()` | von Hand (siehe Abschnitt 8) |
| Logik | `konto/daten.py` | Passwort hashen und prüfen, Anmeldung entscheiden | **automatisch mit pytest** |
| Datenbank | `konto/daten.py` | Nutzerkonto per Nutzername holen | automatisch, mit Test-Datenbank |

Merksatz: **Ein Test kann nicht tippen und nicht auf den Bildschirm schauen.** Er ruft Funktionen auf und vergleicht das Ergebnis. Darum gehört alles, was entschieden werden muss, in Funktionen mit Parametern und Rückgabewert.

---

## 2. Vorbereitung (einmalig)

1. Branch aktualisieren: `git fetch`, dann `main` in deinen Branch holen (`git merge origin/main`). Sonst fehlen dir Dateien, und der Pull Request sieht aus, als hättest du sie gelöscht.
2. Virtuelle Umgebung aktivieren und `pip install -r requirements-dev.txt` ausführen (steht in der README).
3. Prüfen, dass `pytest` läuft: Es meldet „no tests ran". Das ist normal, weil es noch keine Tests gibt.

**Lernziel:** Du weißt, wie du pytest startest und wie die Ausgabe aussieht.

---

## 3. Erst entscheiden, dann bauen (Team klären)

Bevor du Code schreibst, brauchst du Antworten auf diese Fragen. Notiere sie im Entscheidungslog oder im PR, weil die anderen Stories davon abhängen:

- [ ] **Was ist ein „Nutzerkonto"?** Dictionary, Tupel, eigene Klasse oder `sqlite3.Row`? Mindestens sollten die Mieter-ID und der Passwort-Hash drinstehen. Die Mieter-ID brauchen alle anderen Stories, um nur eigene Daten zu zeigen.
- [ ] **Wie heißen die Tabelle und die Spalten für Nutzername und Passwort-Hash?** Frag den Datenbank-Wart und schau in `schema.sql` beziehungsweise `docs/readme/datenbankplan.md` auf `main`.
- [ ] **Welche Hash-Methode nehmen wir?** Klartext-Passwörter sind tabu. Schau dir zum Vergleich an: `hashlib` (Standardbibliothek, z. B. `pbkdf2_hmac`) und das Paket `bcrypt`. Finde heraus, was ein **Salt** ist und warum ein einfacher SHA-256-Hash allein nicht reicht. Ein Paket mehr bedeutet einen Eintrag in `requirements.txt`.
- [ ] **Wie geht der angemeldete Nutzer an die anderen Menüs?** Gibt `anmelden()` das Nutzerkonto zurück und das Hauptprogramm reicht es weiter, oder gibt es einen globalen Zustand? Ersteres ist leichter zu testen.
- [ ] **Groß- und Kleinschreibung beim Nutzernamen:** egal oder unterscheiden?

**Lernziel:** Du erkennst, dass Entscheidungen *vor* dem Code Arbeit sparen.

---

## 4. Schritt für Schritt (in dieser Reihenfolge)

Arbeite in kleinen Runden: **Test schreiben → rot sehen → Funktion schreiben → grün sehen → aufräumen.** Das nennt man testgetriebene Entwicklung (TDD).

### Runde A: Passwort hashen und prüfen (ohne Datenbank)

Funktionen: `passwort_hashen`, `passwort_pruefen`.

Denk-Fragen für deine Tests:
- Wenn ich ein Passwort hashe und danach mit demselben Passwort prüfe: Was muss herauskommen?
- Mit einem falschen Passwort?
- Mit einem leeren Passwort?
- Hashe ich dasselbe Passwort zweimal: Sind die Hashes gleich? Sollten sie es sein? (Hängt vom Salt ab.)
- Steht das Klartext-Passwort irgendwo im Hash?

Lege `tests/test_konto.py` an. Der erste Test darf banal sein, Hauptsache er läuft.

### Runde B: Nutzerkonto aus der Datenbank holen

Funktion: `hole_nutzerkonto_nach_nutzername`.

Hierfür brauchst du eine Test-Datenbank (Abschnitt 5). Denk-Fragen:
- Nutzer existiert: Was kommt zurück, und was steckt darin?
- Nutzer existiert nicht: Es soll `None` zurückkommen (so steht es in eurem Klassendiagramm).
- Was passiert bei einem leeren Nutzernamen?
- **Sicherheit:** Was passiert, wenn jemand `' OR '1'='1` als Nutzernamen eingibt? Wie schützen Platzhalter (`?`) in `sqlite3` davor? Schreib dazu einen eigenen Test. Das ist SQL-Injection und gehört in jeden Anfänger-Werkzeugkasten.

### Runde C: Die Anmeldung entscheiden

Hier fehlt in eurem Klassendiagramm noch eine Funktion, die Runde A und B verbindet. Gib ihr einen Namen in eurem Stil und lege fest: Parameter sind `verbindung`, Nutzername und Passwort; Rückgabe ist das Nutzerkonto oder `None`.

Denk-Fragen, direkt aus den Testfällen:
- `anmelden_01`: richtige Daten → welches Ergebnis?
- `anmelden_02`: falsche Daten → welches Ergebnis?
- Die Unterfälle: falscher Nutzername, falsches Passwort, beides falsch, leere Felder.
- **Sicherheit:** Soll der Aufrufer unterscheiden können, ob der Nutzername oder das Passwort falsch war? (Tipp: Für Angreifer ist das eine Information, die sie nicht bekommen sollen. Eure Fehlermeldung „Anmeldung nicht möglich – falsche Eingaben." ist bewusst allgemein.)

### Runde D: Die Ansicht

`anmelden()`, `abmelden()`, `zeige_hauptmenue()` in `ansicht.py`. Halte sie **so dünn wie möglich**: Eingaben holen, die Logikfunktion aufrufen, Meldung ausgeben. Je weniger Entscheidungen hier stecken, desto weniger musst du von Hand prüfen.

---

## 5. Eine Test-Datenbank bauen

Teste **nie** gegen die echte `wohnpilot.db`. Das brauchst du zum Lernen:

- SQLite kann eine Datenbank nur im Arbeitsspeicher anlegen, die nach dem Test verschwindet. Suche in der Python-Doku zu `sqlite3` nach dem Stichwort `:memory:`.
- Die Tabellen kommen aus eurer `schema.sql`. Überlege, wie du die Datei einliest und ausführst (Stichwort `executescript`).
- Lege danach einen Testnutzer an, mit **gehashtem** Passwort.
- In pytest packst du das Aufbauen in eine **Fixture** (`@pytest.fixture`). Lies dazu in der pytest-Doku das Kapitel „Fixtures". Jeder Test bekommt damit eine frische Datenbank, und Tests beeinflussen sich nicht gegenseitig.

Frage dich: Warum muss `verbindung` ein Parameter sein und darf nicht in der Funktion geöffnet werden? (Antwort: weil du sonst keine Test-Datenbank hineinreichen kannst.)

---

## 6. So ist ein guter Test aufgebaut

Merke dir drei Teile, am besten als Kommentare im Test:

1. **Gegeben:** Ausgangslage (Testnutzer existiert)
2. **Wenn:** eine Aktion (Funktion mit bestimmten Werten aufrufen)
3. **Dann:** Erwartung (Ergebnis mit `assert` prüfen)

Regeln, die dir später viel Ärger ersparen:
- **Ein Test prüft eine Sache.** Dann siehst du bei einem roten Test sofort, was kaputt ist.
- **Der Name sagt, was erwartet wird**, auf Deutsch, z. B. `test_anmelden_falsches_passwort_wird_abgelehnt`.
- **Tests sind unabhängig.** Keiner darf voraussetzen, dass ein anderer vorher lief.
- **Teste auch das Unerwünschte** (Fehlerfälle). Die meisten Fehler stecken dort.

---

## 7. Dein Werkzeugkasten

| Wozu | Befehl |
|---|---|
| alle Tests ausführen | `pytest` |
| ausführlicher | `pytest -v` |
| nur eine Datei | `pytest tests/test_konto.py` |
| nur ein Test (nach Namen) | `pytest -k falsches_passwort` |
| beim ersten Fehler anhalten | `pytest -x` |
| Stil prüfen | `flake8` |
| Formatierung automatisch | `black .` |

**Übung:** Lass einen Test absichtlich fehlschlagen und lies die Ausgabe in Ruhe. pytest zeigt dir, welcher Wert erwartet war und welcher kam. Dieses Lesen ist die wichtigste Fähigkeit.

---

## 8. Von Hand prüfen, was pytest nicht kann

Diese Punkte aus den Testfällen testest du im Terminal selbst und trägst das Ergebnis in `testcases.md` ein (Spalten „Ausgeführt am" und „Status"):

- Das Passwort ist bei der Eingabe nicht sichtbar (Stichwort `getpass`).
- Der Text der Fehlermeldung stimmt.
- Das Menü sieht sinnvoll aus.

---

## 9. Fertig? Checkliste vor dem Pull Request

- [ ] `main` ist in den Branch eingearbeitet
- [ ] `pytest` ist grün
- [ ] `flake8` meldet nichts, `black` ist gelaufen
- [ ] Testfälle `anmelden_01` und `anmelden_02` sind in `testcases.md` ausgefüllt
- [ ] Kein Klartext-Passwort in Code, Testdaten oder Commit
- [ ] SQL nutzt Platzhalter, keine zusammengesetzten Strings
- [ ] Die Entscheidungen aus Abschnitt 3 sind notiert
- [ ] Jede Funktion hat einen kurzen Docstring (ein Satz)
- [ ] Im PR steht, was du gebaut hast und wie man es prüft

---

## 10. Wenn du hängst

- Einen **kleineren** Test schreiben. Oft ist die Aufgabe zu groß gedacht.
- Die Fehlermeldung von oben nach unten lesen. Die letzte Zeile sagt, was schiefging.
- Mit `print()` oder `pytest -s` nachsehen, was wirklich in einer Variable steht.
- Im Team fragen. Das ist in Scrum ausdrücklich erwünscht.

## Zum Weiterlesen (Suchbegriffe)

- pytest „Get started" und „How to use fixtures"
- Python `sqlite3`: Platzhalter, `:memory:`, `executescript`
- `hashlib.pbkdf2_hmac`, `bcrypt`, „Salt und Pepper"
- OWASP „Password Storage Cheat Sheet"
- Arrange, Act, Assert (Muster für Tests)
