# WohnPilot Projektbeschreibung

## Worum geht es?
WohnPilot ist ein Mieterportal. Ein Mieter meldet sich an und findet dort alles rund um seine Wohnung an einem Ort: seine Daten, den Mietvertrag, die Mietzahlungen, die Nebenkostenabrechnung und Nachrichten von der Hausverwaltung.

## Warum dieses Projekt?
Stell dir vor, Familie Beispiel wohnt zur Miete. Der Mietvertrag liegt irgendwo im Ordner, die Nebenkostenabrechnung kam mit der Post und ob die Miete im Mai schon überwiesen wurde, weiß keiner so genau. Dafür wollen wir eine einfache Lösung bauen.

Das Thema passt gut für uns, weil:
- jeder aus dem Alltag weiß, wie Miete und Nebenkosten funktionieren,
- es viele kleine Teile gibt, die man gut aufteilen kann,
- wir klein anfangen können und es später ausbauen können.

## Wer nutzt es?
- **Mieter:** sieht seine eigenen Daten, lädt Unterlagen herunter, gibt Zählerstände ab und meldet Schäden.
- **Hausverwaltung / Vermieter:** pflegt die Daten. In den ersten 5 Wochen machen wir dafür noch keine eigene Oberfläche. Die Daten kommen über ein Testdaten-Skript in die Datenbank. Eine richtige Oberfläche für die Hausverwaltung kommt später.

## Was ist in den 5 Wochen drin? (Stufe 1)
Das sind unsere 10 User Stories für den Mieter:
1. Anmelden und abmelden
2. Eigene Daten ansehen
3. Mietvertrag ansehen
4. Mietzahlungen ansehen (bezahlt, offen, überfällig)
5. Nebenkostenabrechnung ansehen
6. Nebenkostenabrechnung als PDF herunterladen
7. Zählerstände abgeben
8. Wartungs- oder Schadensmeldung erstellen
9. Nachrichten der Hausverwaltung lesen
10. Alle Dokumente ansehen und herunterladen

Das Use-Case-Diagramm liegt in `docs/design/`.

## Was ist bewusst nicht drin?
- Eine Webseite oder andere Oberfläche (Frontend). Wir bedienen das Programm erstmal im Terminal.
- Online-Bezahlen und eine echte Bankanbindung
- Echte Mieterdaten (wir arbeiten nur mit erfundenen Testdaten)
- Eine Oberfläche für die Hausverwaltung
- Veröffentlichung im Internet

## Womit bauen wir?
| Was | Womit | Warum |
|---|---|---|
| Programmiersprache | Python | Haben wir im Unterricht |
| Datenbank | SQLite | Läuft ohne extra Server, ist nur eine Datei. SQL kennen wir aus dem Unterricht, wir schreiben es selbst (Modul `sqlite3`) |
| Oberfläche | Terminal mit Menü | Einfach und wir können uns auf die Logik konzentrieren |
| Tests | pytest | Einfach zu lesen und schnell geschrieben |
| Zusammenarbeit | Git und GitHub | Branches, Pull Requests, Board |
| Vorgehen | Scrum, 5 Sprints à 1 Woche | Jede Woche ist etwas Fertiges zu sehen |

Wir wollten zuerst mit Django und Angular arbeiten. Weil wir nur noch 6 Leute sind und erst die Grundlagen aus dem Unterricht sauber nutzen wollen, haben wir das gestrichen (siehe Entscheidungslog E02).

## Wie könnte es weitergehen? (Ausbaustufen)
- **Stufe 1 (5 Wochen):** Mieterportal im Terminal mit den 10 Stories.
- **Stufe 2:** Eine Oberfläche im Browser für die Mieter. Dafür suchen wir uns dann ein passendes Werkzeug aus. Dazu ein eigener Bereich für die Hausverwaltung (Nebenkostenabrechnung erstellen, Zahlungsstatus ändern, Meldungen bearbeiten, Dokumente hochladen). Das steht schon im Use-Case-Diagramm. Das Mockup in `docs/design/Mockups/` kann dafür als Vorlage dienen.
- **Stufe 3:** Mehr Komfort: E-Mail-Benachrichtigungen, Suche und Filter, Diagramme zu den Kosten, mehrere Häuser.
- **Stufe 4:** Betrieb wie im Unternehmen: andere Datenbank (z. B. MariaDB), automatische Tests bei GitHub, Veröffentlichung auf einem Server.

## Was lernen wir dabei?
| Fach | Wo es vorkommt |
|---|---|
| Python | ganzes Projekt |
| SQL | Tabellen, Beziehungen, Abfragen (direkt in `sqlite3`) |
| Datenschutz | Mieterdaten sind persönlich: jeder sieht nur seine eigenen Daten, nur Testdaten, Passwörter nur als Hash |
| PQSM / Qualität | Tests, Code-Review, Fertig-Liste |
| Anwendungsentwicklung | Use-Case-Diagramm, später ER-Diagramm |
| WiSo | Teamarbeit, Rollen, Planung |

## Woran merken wir, dass es geklappt hat? (Ziel am 03.11.2026)
- Ein Mieter kann sich anmelden und alle 10 Stories nutzen.
- Der Mieter sieht nie Daten von anderen Mietern.
- Alles ist in GitHub und dokumentiert. Ein neuer Kollege könnte in einer Stunde starten.
- Es gibt Tests und die sind grün.
