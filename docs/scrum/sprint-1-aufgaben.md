# Sprint 1 – Aufgaben (30.09. bis 06.10.2026)

## Sprint-Ziel
> **Das Projekt läuft bei allen (Django-API und Angular-Oberfläche). Ein Mieter kann sich anmelden und sieht sein Profil.**

**Mindestziel** (falls es knapp wird): Backend und Frontend laufen und Anmelden funktioniert.

Zeit: ca. 35 Stunden. Die Stunden pro Aufgabe sind grobe Schätzungen für ein Paar inklusive Test und Review.

Zwei Änderungen zum ersten Entwurf: **Angular** ist dazugekommen, deshalb rutscht US08 Nachrichten nach Sprint 2. Angular ist für die meisten neu. Bitte früh fragen, nicht erst nach 20 Minuten Festhängen.

## Aufgabenliste
| Nr. | Aufgabe | Story | App / Ordner | ca. Std. | Danach erst | Wer (Paar) |
|---|---|---|---|---|---|---|
| T01 | GitHub-Board anlegen (Spalten) und Issues aus den Stories erstellen | – | – | 2 | | |
| T02 | Alle ins Repo einladen, Git-Übung: Namen in `docs/team.md` eintragen (Branch, Pull Request, Review, Merge) | – | `docs/` | 1 pro Person | | |
| T03 | Django-Projekt im Ordner `backend/` anlegen (`cd backend`, dann `django-admin startproject config .`), die 9 Apps mit `startapp` in `backend/apps/` anlegen (siehe Guide, Abschnitt 3; die Ordner gibt es schon), Django REST Framework in `INSTALLED_APPS` eintragen (steht schon in `backend/requirements.txt`). `python manage.py runserver` läuft, `/admin` ist erreichbar | Setup | `backend/` | 3 | | |
| T04 | Angular-Projekt im Ordner `frontend/` anlegen (im Projektordner: `npx @angular/cli new frontend`, Stylesheet CSS, SSR/SSG **nein**). Läuft mit `npm start`. **Proxy** einrichten, damit `/api/...` an Django (Port 8000) geht. Prettier prüfen | Setup | `frontend/` | 3 | T03 | |
| T05 | README-Setup für Backend **und** Frontend prüfen und ergänzen. **Ein Neuer testet es** auf seinem Rechner (Mac und Windows) | Setup | `README` | 2 | T03, T04 | |
| T06 | Grundlayout in Angular (Menü, Router mit leeren Seiten, einheitliches Aussehen) | Setup | `frontend/` | 2 | T04 | |
| T07 | Tabellen (Models) in der jeweiligen App anlegen: Mieter (`accounts`), Wohnung (`wohnungen`), Mietvertrag (`mietvertraege`), Zahlung (`zahlungen`), Nachricht (`nachrichten`), plus erste Datenbank-Migration | Setup | `accounts`, `wohnungen`, `mietvertraege`, `zahlungen`, `nachrichten` | 3 | T03 | |
| T08 | Testdaten-Befehl: zwei Mieter (Anna und Ben) mit Wohnung, Vertrag, Zahlungen, Nachrichten | Setup | `accounts` | 2 | T07 | |
| T09 | Login-API: `POST /api/anmelden/` und `/api/abmelden/`, Fehlermeldung bei falschem Passwort (Verfahren nach Entscheidung E08). Eintrag in [api.md](../design/api.md) | US09 | `accounts` | 3 | T03 | |
| T10 | Angular: Login-Seite und Abmelden-Knopf (Service, Formular, Fehlermeldung). Hier richten wir auch den CSRF-Schutz zentral ein | US09 | `frontend/` | 3 | T04, T09 | |
| T11 | Alle Seiten ohne Anmeldung sperren: die API verlangt standardmäßig Anmeldung, der Angular-Guard leitet zum Login um | US09 | `backend/`, `frontend/` | 2 | T10 | |
| T12 | Tests für Anmelden (Backend): mit/ohne Login, nach Abmelden gesperrt | US09 | `accounts` | 2 | T11 | |
| T13 | Profil: API `GET /api/profil/` (nur der angemeldete Mieter) und Angular-Profilseite mit Name und Kontaktdaten | US01 | `accounts`, `frontend/` | 3 | T07, T10 | |
| T14 | Test: Anna sieht Annas Daten, Ben nicht (API-Test) | US01 | `accounts` | 2 | T13, T08 | |
| T15 | Entscheidungslog anlegen, erste Einträge (E07 Angular, E08 Anmeldeverfahren) | Doku | `docs/` | 1 | | |
| T16 | Review-Vorbereitung: Ergebnisse für Dienstag live zeigen | – | – | 1 | alle | |

Summe: etwa 35 Stunden.

## Reihenfolge-Tipp
| Tag | Was |
|---|---|
| **Mi 30.09.** | Vorher Node.js installieren (`node --version`). Erste Stunde **alle zusammen**: T03 (Django-Projekt anlegen), einer tippt, alle schauen zu und legen es dann auf ihrem Rechner an. Danach T01 und T02 |
| **Do 01.10.** | Einführung in Angular und Django REST Framework. Danach T04, T07, T09 starten. Anmeldeverfahren (E08) entscheiden |
| **Fr 02.10.** | T05, T06, T08, T10, T11 |
| **Mo 05.10.** | T12, T13, T14 (Tests), Pull Requests fertig machen, Reviews |
| **Di 06.10.** | Review, Retro, Planning (Treffen 90 Min.) |

## Wenn es zu viel wird
1. T06 (Layout) einfach halten: nur ein Menü, kein Design.
2. Profil (T13, T14) nach Sprint 2 verschieben.
3. Mindestziel beachten: Backend und Frontend laufen + Anmelden.

## So nimmt man sich eine Aufgabe
1. Eigenen Namen (Paar) in die Spalte „Wer" eintragen.
2. Karte auf dem Board nach **In Arbeit** ziehen.
3. Branch anlegen: `feature/t08-login`
4. Am Ende Pull Request öffnen. Ein anderes Paar prüft ihn.
5. Nach dem Merge Karte nach **Fertig**.
