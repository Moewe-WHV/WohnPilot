# Dokumentation

Gute Doku bedeutet: Ein neuer Kollege versteht in einer Stunde, was das Projekt ist und wie man startet. Der **Doku-Wart** achtet darauf, aber alle schreiben mit.

## Was wir dokumentieren
| Was | Wo | Wer pflegt |
|---|---|---|
| Was ist WohnPilot? Setup-Anleitung | `README.md` | Doku-Wart |
| Wo liegt was? (Inhaltsverzeichnis der Doku) | [docs/README.md](../README.md) | Doku-Wart |
| Projektidee, Ausbaustufen | [projektbeschreibung.md](projektbeschreibung.md) | Doku-Wart, PO |
| User Stories | [user-stories.md](user-stories.md) | PO |
| Use-Case-Diagramm | `docs/design/` | wer es ändert |
| Datenbank (ER-Diagramm) | `docs/design/` (kommt in Sprint 2) | Datenbank-Wart |
| API (alle Endpunkte) | [api.md](../design/api.md) | wer den Endpunkt baut |
| Rollen, Sprintplanung, Gantt | [rollen.md](rollen.md), [sprintplanung.md](../scrum/sprintplanung.md), [gantt.md](../scrum/gantt.md) | Teamleitung |
| Programmierguide | [CONTRIBUTING.md](../../CONTRIBUTING.md) | alle |
| Meetings | `docs/meetings/` (eine Datei pro Meeting) | wer Protokoll führt |
| Entscheidungen | Entscheidungslog (unten) | Doku-Wart |
| Code | Kommentare und kurze Beschreibung in Funktionen | jeder |

## Regeln
1. **Doku gehört zu „Fertig".** Wenn sich etwas ändert (neue Seite, neuer Befehl), prüft das Paar, ob README oder Doku angepasst werden müssen.
2. **Kurz und einfach.** Lieber drei klare Sätze als eine Seite Fachchinesisch.
3. **Neuer testet das Setup.** Wer neu im Projekt ist, geht die README durch und meldet, wo es hakt.
4. **Alle Dateien sind Markdown** und liegen im Repository, damit sie mit dem Code zusammen versioniert werden.

## Was ins README gehört
- Ein Absatz: Was ist das Projekt?
- Setup für Mac und Windows (Schritt für Schritt)
- Wie starte ich Backend **und** Frontend? Wie starte ich die Tests (Backend und Frontend)?
- Die Logins der Testnutzer (Anna und Ben)
- Wo finde ich die Doku?

## Entscheidungslog
Hier halten wir fest, **was** wir entschieden haben und **warum**. So müssen wir später nicht raten.

| Nr. | Entscheidung | Warum | Status |
|---|---|---|---|
| E01 | Neuer Start mit WohnPilot statt iSlave weiterzuführen | Aufräumen von iSlave war nicht schaffbar, Neue brauchen einen sauberen Einstieg | Vorschlag, Zustimmung am 29.09. |
| E02 | Django mit Django REST Framework als Backend (API) | Einige im Team kennen Django, es bringt Login, Admin und Datenbank mit. Das REST Framework macht daraus die Schnittstelle für Angular | Vorschlag |
| E03 | SQLite als Datenbank | Kein Server nötig, jeder hat eine eigene Datei. Wechsel später möglich | Vorschlag |
| E04 | 5 Sprints à 1 Woche (Mi bis Di), Treffen am Dienstag | Passt zum Unterricht und zur Zeit des Dozenten | Vorschlag |
| E05 | Arbeiten nur über Branches und Pull Requests | Alle sehen, was in `main` kommt, weniger Konflikte | Vorschlag |
| E06 | Hausverwaltung nutzt in Stufe 1 den Django-Admin | Spart Zeit, Fokus auf das Mieterportal | Vorschlag |
| E07 | Angular als Frontend (Oberfläche der Mieter) im Ordner `frontend/` | Mehrere im Team wollen Angular nutzen. Backend und Frontend lassen sich sauber trennen und auf Paare aufteilen | Vorschlag |
| E08 | Anmeldung zwischen Angular und Django: Cookie (Session) oder Token | Wird nach der Angular/DRF-Einführung am 01.10. entschieden, vor Aufgabe T09 | offen |
| E09 | Ordnerstruktur: `backend/` (Django), `frontend/` (Angular) und `docs/` mit den Unterordnern `projekt/`, `scrum/`, `meetings/`, `design/`, `testing/`. `docs/teamleitung/` bleibt privat (steht in der `.gitignore`) | Neue im Team finden sich schneller zurecht: Ein Blick auf die Ordner zeigt, wo was liegt | Vorschlag |

*Status „Vorschlag" wird nach dem Kickoff auf „Beschlossen" mit Datum geändert.*

Neue Einträge: nächste Nummer, kurzer Satz zur Entscheidung, kurzer Satz zum Grund.
