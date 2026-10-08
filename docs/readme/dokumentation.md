# Dokumentation

Gute Doku heißt: Ein neuer Kollege versteht in einer Stunde, was das Projekt ist und wie man startet. Der Doku-Wart achtet darauf, aber alle schreiben mit.

## Was wir dokumentieren
| Was | Wo | Wer pflegt |
|---|---|---|
| Was ist WohnPilot? Setup-Anleitung | `README.md` | Doku-Wart |
| Projektidee, Ausbaustufen | [projektbeschreibung.md](projektbeschreibung.md) | Doku-Wart, PO |
| Use-Case-Diagramm und Mockup | `docs/design/` | wer es ändert |
| Use-Case-Vorlage | `docs/templates/tmp_usecase.md` | wer einen Use Case schreibt |
| Datenbank (ER-Diagramm, `schema.sql`) | `docs/design/` (kommt in Sprint 2) | Datenbank-Wart |
| Rollen und Planung | [rollen.md](rollen.md), [planning-poker.md](planning-poker.md) | Teamleitung |
| Testfälle | [../testing/testcases.md](../testing/testcases.md) | Test-Wart |
| Programmierguide | [CONTRIBUTING.md](../../CONTRIBUTING.md) | alle |
| Meetings | `docs/meetings/` (eine Datei pro Meeting, Vorlage nutzen) | wer Protokoll führt |
| Entscheidungen | Entscheidungslog (unten) | Doku-Wart |
| Code | Kommentare und kurze Beschreibung in den Funktionen | jeder |

## Regeln
1. Doku gehört zu "Fertig". Wenn sich etwas ändert (neue Funktion, neuer Befehl), prüft das Paar, ob README oder Doku angepasst werden müssen.
2. Kurz und einfach. Lieber drei klare Sätze als eine Seite Fachchinesisch.
3. Wer neu im Projekt ist, geht die README durch und sagt, wo es hakt.
4. Alle Dateien sind Markdown und liegen im Repository, damit sie zusammen mit dem Code versioniert werden.

## Was ins README gehört
- Ein Absatz: Was ist das Projekt?
- Setup für Mac und Windows (Schritt für Schritt)
- Wie starte ich das Programm? Wie starte ich die Tests?
- Die Logins der Testnutzer (Anna und Ben)
- Wo finde ich die Doku?

## Entscheidungslog
Hier halten wir fest, was wir entschieden haben und warum. So müssen wir später nicht raten.

| Nr. | Entscheidung | Warum | Status |
|---|---|---|---|
| E01 | Neuer Start mit WohnPilot statt iSlave weiterzuführen | Aufräumen von iSlave war nicht schaffbar, Neue brauchen einen sauberen Einstieg | Zustimmung am 29.09. |
| E02 | Kein Django und kein Angular. Wir bauen ein reines Python-Programm | Wir sind nur noch 6 Leute und wollen erst die Grundlagen aus dem Unterricht (Python, SQL) sauber nutzen, bevor wir zwei große Frameworks dazunehmen | Vorschlag |
| E03 | SQLite als Datenbank, SQL direkt mit `sqlite3` | Kein Server nötig, jeder hat eine eigene Datei. Wechsel später möglich | Vorschlag |
| E04 | 5 Sprints à 1 Woche (Mi bis Di), Treffen am Dienstag | Passt zum Unterricht und zur Zeit des Dozenten | Vorschlag |
| E05 | Arbeiten nur über Branches und Pull Requests | Alle sehen, was in `main` kommt, weniger Konflikte | Vorschlag |
| E06 | Kein Frontend in Stufe 1, Bedienung im Terminal | Wir konzentrieren uns auf Logik und Daten. Eine Oberfläche kommt in Stufe 2 | Vorschlag |
| E07 | Hausverwaltung hat in Stufe 1 keine eigene Oberfläche, Daten kommen über ein Testdaten-Skript | Spart Zeit, Fokus auf das Mieterportal | Vorschlag |

Der Status "Vorschlag" wird nach der Abstimmung im Team auf "Beschlossen" mit Datum geändert.

Neue Einträge: nächste Nummer, ein kurzer Satz zur Entscheidung und ein kurzer Satz zum Grund.
