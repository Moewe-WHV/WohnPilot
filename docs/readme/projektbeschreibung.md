# WohnPilot – Projektbeschreibung

## Worum geht es?
WohnPilot ist ein **Mieterportal**. Ein Mieter meldet sich auf einer Webseite an und findet dort alles rund um seine Wohnung an einem Ort: seine Daten, den Mietvertrag, die Mietzahlungen, die Nebenkostenabrechnung und Nachrichten von der Hausverwaltung.

## Warum dieses Projekt?
Stell dir vor, Familie Beispiel wohnt zur Miete. Der Mietvertrag liegt irgendwo im Ordner, die Nebenkostenabrechnung kam per Post, und ob die Miete im Mai schon überwiesen wurde, weiß keiner so genau. Genau dafür bauen wir eine einfache Lösung.

Das Thema ist für uns gut geeignet, weil:
- jeder aus dem Alltag weiß, wie Miete und Nebenkosten funktionieren,
- es viele kleine Teile gibt, die man **gut aufteilen** kann,
- es klein anfangen darf und sich später **professionell ausbauen** lässt.

## Wer nutzt es?
- **Mieter:** sieht seine eigenen Daten, lädt Unterlagen herunter, meldet Zählerstände und Schäden.
- **Hausverwaltung / Vermieter:** pflegt die Daten. In den ersten 5 Wochen machen wir das über den fertigen Admin-Bereich von Django. Eine eigene Oberfläche dafür kommt später.

## Was ist in den 5 Wochen drin? (Stufe 1)
Das sind unsere 10 User Stories für den Mieter:
1. Anmelden und abmelden
2. Eigene Daten ansehen
3. Mietvertrag ansehen
4. Mietzahlungen ansehen (bezahlt, offen, überfällig)
5. Nebenkostenabrechnung ansehen
6. Nebenkostenabrechnung als PDF herunterladen
7. Zählerstände übermitteln
8. Wartungs- oder Schadensmeldung erstellen
9. Nachrichten der Hausverwaltung lesen
10. Alle Dokumente ansehen und herunterladen

Die genauen Texte stehen in [user-stories.md](user-stories.md). Das Use-Case-Diagramm liegt in `docs/design/`.

## Was ist bewusst nicht drin?
- Online-Bezahlen, echte Bankanbindung
- Echte Mieterdaten (wir arbeiten nur mit **erfundenen Testdaten**)
- Eine schöne Oberfläche für die Hausverwaltung (Stufe 2)
- Veröffentlichung im Internet

## Womit bauen wir?
| Was | Womit | Warum |
|---|---|---|
| Programmiersprache | Python | Haben wir im Unterricht |
| Web-Framework | Django | Bringt Anmeldung, Datenbank und Admin schon mit. Einige im Team kennen es |
| Datenbank | SQLite | Läuft ohne extra Server, ist eine einzelne Datei. Die SQL-Grundlagen sind wie bei MariaDB. Später kann man die Datenbank wechseln |
| Aussehen | HTML und CSS | Reicht für den Anfang |
| Zusammenarbeit | Git und GitHub | Branches, Pull Requests, Board |
| Vorgehen | Scrum, 5 Sprints à 1 Woche | Jede Woche ist etwas Fertiges zu sehen |

## Wie könnte es weitergehen? (Ausbaustufen)
- **Stufe 1 (5 Wochen):** Mieterportal mit den 10 Stories, Hausverwaltung über den Admin-Bereich.
- **Stufe 2:** Eigener Bereich für die Hausverwaltung: Nebenkostenabrechnung erstellen, Zahlungsstatus ändern, Meldungen bearbeiten, Dokumente hochladen (steht schon im Use-Case-Diagramm).
- **Stufe 3:** Komfort: E-Mail-Benachrichtigungen, Suche und Filter, Diagramme zu den Kosten, mehrere Häuser.
- **Stufe 4:** Betrieb wie im Unternehmen: andere Datenbank (z. B. MariaDB), automatische Tests bei GitHub, Veröffentlichung auf einem Server.

## Was lernen wir dabei?
| Fach | Wo es vorkommt |
|---|---|
| Python | ganzes Projekt |
| SQL | Tabellen, Beziehungen, Abfragen (über Django) |
| Datenschutz | Mieterdaten sind persönlich: jeder sieht nur seine eigenen Daten, nur Testdaten |
| PQSM / Qualität | Tests, Code-Review, „Fertig"-Liste |
| Anwendungsentwicklung | Use-Case-Diagramm, später ER-Diagramm |
| WiSo | Teamarbeit, Rollen, Planung |

## Woran merken wir, dass es geklappt hat? (Ziel am 03.11.2026)
- Ein Mieter kann sich anmelden und alle 10 Stories nutzen.
- Der Mieter sieht **nie** Daten von anderen Mietern.
- Alles ist in GitHub und dokumentiert. Ein neuer Kollege könnte in einer Stunde starten.
- Es gibt Tests, die grün sind.
