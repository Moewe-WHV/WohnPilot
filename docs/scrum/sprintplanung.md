# Sprintplanung

## Rahmen
- **5 Sprints**, jeder dauert **1 Woche** (Mittwoch bis Dienstag)
- Jeder Entwickler arbeitet ca. **1 Stunde pro Tag** (5 Tage, Mo–Fr) = etwa 40 Std. Team-Arbeitszeit pro Sprint
- Wir planen vorsichtig mit **etwa 35 Stunden**, weil wir Anfänger sind und nebenher Unterricht haben
- Einmal pro Woche das **Treffen mit dem Dozenten (1,5 Std.)**, immer am Dienstag: Review, Retro und Planning

| Sprint | Zeitraum | Treffen am Ende |
|---|---|---|
| Kickoff | Di 29.09.2026 | Rollen, Planning Poker, Aufgaben verteilen |
| 1 | Mi 30.09. – Di 06.10. | Di 06.10. |
| 2 | Mi 07.10. – Di 13.10. | Di 13.10. |
| 3 | Mi 14.10. – Di 20.10. | Di 20.10. |
| 4 | Mi 21.10. – Di 27.10. | Di 27.10. |
| 5 | Mi 28.10. – Di 03.11. | Di 03.11. (Abschluss) |

## Was wir in welchem Sprint machen

### Sprint 1: Wir starten
**Ziel:** Das Projekt läuft bei allen (Django-API und Angular-Oberfläche). Man kann sich anmelden und sieht sein Profil.
- Projekt-Setup (Django mit REST Framework, Angular, Tabellen, Testdaten)
- Einführung in Angular und Django REST Framework im Team (Do 01.10.)
- US09 Anmelden, US01 Eigene Daten
- Board, Issues, Git-Übung, README
- US08 Nachrichten rutscht nach Sprint 2, weil das Setup mit Angular Zeit braucht.
- **Mindestziel**, falls es knapp wird: Backend und Frontend laufen + Anmelden funktioniert.

### Sprint 2: Mieter-Grundlagen
**Ziel:** Der Mieter sieht Nachrichten, Zahlungen und seinen Mietvertrag.
- US08 Nachrichten, US03 Zahlungen, US02 Mietvertrag (drei ähnliche Seiten: API in Django, Liste oder Detail in Angular. Wenn das Muster aus Sprint 1 einmal steht, geht es schneller)
- ER-Diagramm der Datenbank (Doku-Wart und Datenbank-Wart)
- API-Übersicht ([api.md](../design/api.md)) auf dem Stand halten

### Sprint 3: Nebenkosten und Zählerstände
**Ziel:** Der Mieter sieht seine Nebenkostenabrechnung und kann Zählerstände melden.
- US04 Nebenkostenabrechnung, US06 Zählerstände
- Erster Datenschutz-Check (Datenschutz-Wart)
- Hüte rotieren

### Sprint 4: PDF, Dokumente und Meldungen
**Ziel:** Dateien lassen sich herunterladen und Schadensmeldungen funktionieren.
- US05 PDF (baut auf US04 auf), US10 Dokumente (liefert Dateien aus, gleiche Technik wie das PDF), US07 Wartungsmeldung
- Was aus früheren Sprints liegen geblieben ist, wird hier nachgeholt

### Sprint 5: Aufräumen und Abschluss
**Ziel:** Alles läuft, ist getestet und dokumentiert. Wir präsentieren.
- Feature-Stopp, nur noch Fehler beheben
- Tests ergänzen, Doku fertigstellen, Programmierguide prüfen
- Abschlusspräsentation vorbereiten
- Wenn Zeit bleibt: Ausblick auf Stufe 2

## Grobe Stundenplanung
| Sprint | Stories | ca. Stunden | Puffer |
|---|---|---|---|
| 1 | Setup (Django + Angular) + US09 + US01 + Doku | 35 | kaum, bewusst klein halten |
| 2 | US08 + US03 + US02 + Doku/Tests | 32 | ca. 3 |
| 3 | US04 + US06 + Check + Doku | 32 | ca. 3 |
| 4 | US05 + US10 + US07 + Doku | 33 | ca. 2 |
| 5 | Nacharbeit, Tests, Doku, Präsentation | 30 | ca. 5 |

Die Stunden sind grobe Schätzungen. Nach Sprint 1 wissen wir, wie viel wir wirklich schaffen (das nennt man **Velocity**), und passen die Planung an. Angular ist für die meisten neu, deshalb wird Sprint 1 vermutlich langsamer. Die Velocity zeigt es uns.

## Unsere „Fertig"-Liste (Definition of Done)
Eine Story ist erst fertig, wenn:
- [ ] alle Akzeptanzkriterien stimmen,
- [ ] wir es in der Angular-Oberfläche im Browser ausprobiert haben (auch mit einem zweiten Mieter),
- [ ] der Mieter nur seine **eigenen** Daten sieht,
- [ ] mindestens ein **Test** läuft und grün ist (Backend: `python manage.py test` im Ordner `backend`, Frontend: `npm test` im Ordner `frontend`),
- [ ] `flake8` und `black` (Python) sowie `prettier` (Angular) nichts mehr meckern,
- [ ] ein anderes Paar den **Pull Request** angeschaut und freigegeben hat,
- [ ] README oder Doku angepasst sind, falls sich etwas geändert hat (bei einem neuen Endpunkt auch [api.md](../design/api.md)).

## Wenn etwas nicht klappt
- Story zu groß? Wir teilen sie in kleinere (z. B. erst die API, dann die Angular-Seite).
- Sprint-Ziel nicht geschafft? Kein Drama. Wir besprechen es im Review, der PO entscheidet, was in den nächsten Sprint kommt.
- Zu viele Stories offen? Der PO streicht von hinten (Kann-Stories zuerst).

## Wochenablauf
| Tag | Was |
|---|---|
| Mittwoch | Neuer Sprint startet, Aufgaben schnappen |
| Do bis Mo | Arbeiten, jeden Tag kurzes Daily (siehe [meeting-vorlage.md](../meetings/meeting-vorlage.md)) |
| Montag | Pull Requests fertig machen, Reviews |
| 1x die Woche | Treffen (1,5 Std.): Review, Retro, Planning für den nächsten Sprint |
