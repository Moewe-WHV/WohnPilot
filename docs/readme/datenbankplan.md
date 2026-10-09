# Datenbankplan

Dieses Dokument beschreibt die Datenbank von WohnPilot in Klartext. Es gehört zum ER-Diagramm `WohnPilot_ER_Modell_v2.png` (bzw. `.mwb`) in diesem Ordner und erklärt jede Tabelle, jede Spalte und jede Beziehung in Worten. Wer eine Tabelle ändert, passt beides an: das Diagramm und dieses Dokument.

Datenbank-Wart: Benjamin (siehe [rollen.md](../readme/rollen.md)).

## Grundidee

Jeder Mieter (`benutzer`) hat genau einen oder mehrere Mietverträge (`mietvertraege`), jeder Mietvertrag gehört zu genau einer Wohnung (`mietobjekte`). Rund um den Mietvertrag hängen die Dinge, die der Mieter laut unseren 10 User Stories sehen soll: Zahlungen, Nebenkostenabrechnungen, Dokumente. Rund um die Wohnung hängen Zähler und Wartungsmeldungen. Nachrichten laufen direkt zwischen zwei Benutzern (Mieter und Hausverwaltung).

## Übersicht der Tabellen

| Tabelle | Wofür |
|---|---|
| `benutzer` | Mieter und Hausverwaltung/Vermieter, zum Anmelden |
| `mietobjekte` | Die Wohnungen/Häuser selbst |
| `mietvertraege` | Verbindet einen Mieter mit einer Wohnung, mit Konditionen |
| `zahlungen` | Mietzahlungen zu einem Vertrag |
| `nebenkostenabrechnungen` | Jährliche Abrechnung zu einem Vertrag |
| `zaehler` | Strom-/Gas-/Wasserzähler einer Wohnung |
| `zaehlerstaende` | Abgelesene Werte eines Zählers |
| `wartungsmeldungen` | Schadens-/Wartungsmeldungen zu einer Wohnung |
| `nachrichten` | Nachrichten zwischen zwei Benutzern |
| `mietvertragsdokumente` | Hochgeladene Dateien zu einem Vertrag (Mietvertrag, Abrechnung etc.) |

## Tabellen im Detail

### `benutzer`
Mieter und Hausverwaltung sitzen in derselben Tabelle, unterschieden über `rolle`. In Stufe 1 legen wir Hausverwaltungs-Benutzer nur über das Testdaten-Skript an (siehe [projektbeschreibung.md](../readme/projektbeschreibung.md)).

| Spalte | Typ | Beschreibung |
|---|---|---|
| `benutzer_id` | INTEGER, PK | eindeutige ID |
| `benutzername` | VARCHAR(50) | Login-Name, eindeutig |
| `passwort_hash` | VARCHAR(255) | nie das Klartext-Passwort speichern |
| `vorname` | VARCHAR(50) | |
| `nachname` | VARCHAR(50) | |
| `email` | VARCHAR(150) | |
| `telefon` | VARCHAR(30) | |
| `strasse` | VARCHAR(100) | Meldeadresse |
| `hausnummer` | VARCHAR(10) | |
| `plz` | VARCHAR(10) | |
| `ort` | VARCHAR(100) | |
| `rolle` | ENUM | `mieter` oder `verwalter` |
| `erstellt_am` | DATETIME | |

### `mietobjekte`
Eine Wohnung/ein Haus, unabhängig vom aktuellen Mieter. So bleibt die Historie sauber, wenn ein Mietvertrag endet und ein neuer beginnt.

| Spalte | Typ | Beschreibung |
|---|---|---|
| `mietobjekt_id` | INTEGER, PK | |
| `typ` | ENUM | `wohnung`, `haus`, `gewerbe`, `stellplatz` |
| `strasse` | VARCHAR(100) | |
| `hausnummer` | VARCHAR(10) | |
| `wohnungsnummer` | VARCHAR(20) | leer bei Häusern |
| `plz` | VARCHAR(10) | |
| `ort` | VARCHAR(100) | |

### `mietvertraege`
Das Herzstück: verbindet Mieter, Hausverwaltung und Wohnung.

| Spalte | Typ | Beschreibung |
|---|---|---|
| `mietvertrag_id` | INTEGER, PK | |
| `mieter_id` | INTEGER, FK → `benutzer.benutzer_id` | |
| `verwalter_id` | INTEGER, FK → `benutzer.benutzer_id` | zuständige Hausverwaltung |
| `mietobjekt_id` | INTEGER, FK → `mietobjekte.mietobjekt_id` | |
| `vertragsbeginn` | DATE | |
| `vertragsende` | DATE | leer bei laufendem Vertrag |
| `kaltmiete` | DECIMAL(10,2) | |
| `nebenkostenvorauszahlung` | DECIMAL(10,2) | |
| `kaution` | DECIMAL(10,2) | |
| `erstellt_am` | DATETIME | |

### `zahlungen`
Deckt User Story 4 ab: bezahlt, offen, überfällig.

| Spalte | Typ | Beschreibung |
|---|---|---|
| `zahlung_id` | INTEGER, PK | |
| `mietvertrag_id` | INTEGER, FK → `mietvertraege.mietvertrag_id` | |
| `faelligkeitsdatum` | DATE | |
| `zahlungsdatum` | DATE | leer solange nicht bezahlt |
| `betrag` | DECIMAL(10,2) | |
| `status` | ENUM | `offen`, `bezahlt`, `ueberfaellig` |

### `nebenkostenabrechnungen`
Eine Zeile pro Vertrag und Abrechnungsjahr.

| Spalte | Typ | Beschreibung |
|---|---|---|
| `nebenkostenabrechnung_id` | INTEGER, PK | |
| `mietvertrag_id` | INTEGER, FK → `mietvertraege.mietvertrag_id` | |
| `abrechnungsjahr` | YEAR | |
| `abrechnungsdatum` | DATE | |
| `gesamtbetrag` | DECIMAL(10,2) | |
| `erstellt_am` | DATETIME | |

### `zaehler`
Ein Zähler gehört zu einer Wohnung, nicht zu einem Mietvertrag (bleibt beim Mieterwechsel bestehen).

| Spalte | Typ | Beschreibung |
|---|---|---|
| `zaehler_id` | INTEGER, PK | |
| `mietobjekt_id` | INTEGER, FK → `mietobjekte.mietobjekt_id` | |
| `zaehlerart` | ENUM | `strom`, `gas`, `wasser` |
| `zaehlernummer` | VARCHAR(50) | |
| `einheit` | VARCHAR(10) | z. B. `kWh`, `m³` |

### `zaehlerstaende`
Jede Ablesung ist eine eigene Zeile (User Story 7: Zählerstände abgeben).

| Spalte | Typ | Beschreibung |
|---|---|---|
| `zaehlerstand_id` | INTEGER, PK | |
| `zaehler_id` | INTEGER, FK → `zaehler.zaehler_id` | |
| `ablesedatum` | DATE | |
| `zaehlerstand` | DECIMAL(12,2) | |
| `erstellt_am` | DATETIME | |

### `wartungsmeldungen`
User Story 8: Wartungs-/Schadensmeldung erstellen.

| Spalte | Typ | Beschreibung |
|---|---|---|
| `wartungsmeldung_id` | INTEGER, PK | |
| `mietobjekt_id` | INTEGER, FK → `mietobjekte.mietobjekt_id` | |
| `ersteller_id` | INTEGER, FK → `benutzer.benutzer_id` | meldender Mieter |
| `bearbeiter_id` | INTEGER, FK → `benutzer.benutzer_id` | zuständige Hausverwaltung, leer bis zugewiesen |
| `titel` | VARCHAR(150) | |
| `beschreibung` | TEXT | |
| `status` | ENUM | `offen`, `in_bearbeitung`, `erledigt` |
| `datum_gemeldet` | DATETIME | |
| `datum_erledigt` | DATETIME | leer solange offen |

### `nachrichten`
User Story 9: Nachrichten der Hausverwaltung lesen. Allgemein als Nachricht zwischen zwei Benutzern modelliert, damit später auch der Mieter schreiben kann.

| Spalte | Typ | Beschreibung |
|---|---|---|
| `nachricht_id` | INTEGER, PK | |
| `absender_id` | INTEGER, FK → `benutzer.benutzer_id` | |
| `empfaenger_id` | INTEGER, FK → `benutzer.benutzer_id` | |
| `titel` | VARCHAR(150) | |
| `inhalt` | TEXT | |
| `status` | ENUM | `gelesen`, `ungelesen` |
| `erstellt_am` | DATETIME | |

### `mietvertragsdokumente`
User Story 6 und 10: Dokumente ansehen/herunterladen. Deckt Mietvertrag, Nebenkostenabrechnung und sonstige Dateien ab — alles, was zu einem Vertrag hochgeladen wurde.

| Spalte | Typ | Beschreibung |
|---|---|---|
| `dokument_id` | INTEGER, PK | |
| `mietvertrag_id` | INTEGER, FK → `mietvertraege.mietvertrag_id` | |
| `dateiname` | VARCHAR(255) | Anzeigename |
| `dateipfad` | VARCHAR(500) | Speicherort auf der Festplatte |
| `hochgeladen_am` | DATETIME | |

## Beziehungen im Überblick

- Ein `benutzer` (Mieter) hat mehrere `mietvertraege`; ein `benutzer` (Verwalter) betreut mehrere `mietvertraege`.
- Ein `mietobjekt` hat im Lauf der Zeit mehrere `mietvertraege` (nacheinander, nicht gleichzeitig).
- Ein `mietvertrag` hat mehrere `zahlungen`, mehrere `nebenkostenabrechnungen` und mehrere `mietvertragsdokumente`.
- Ein `mietobjekt` hat mehrere `zaehler`, mehrere `wartungsmeldungen`.
- Ein `zaehler` hat mehrere `zaehlerstaende`.
- Ein `benutzer` sendet und empfängt mehrere `nachrichten` (zwei getrennte Beziehungen: Absender und Empfänger).
- Ein `benutzer` erstellt mehrere `wartungsmeldungen` und bearbeitet mehrere `wartungsmeldungen` (zwei getrennte Beziehungen).

## Hinweise zur Umsetzung in SQLite

Wir nutzen SQLite (siehe [projektbeschreibung.md](../readme/projektbeschreibung.md)). SQLite kennt die Typen oben nicht alle direkt, deshalb beim Schreiben von `schema.sql` (Sprint 2) so umsetzen:

| Im Plan | In SQLite |
|---|---|
| `INTEGER, PK` | `INTEGER PRIMARY KEY AUTOINCREMENT` |
| `VARCHAR(n)` | `TEXT` (Länge wird nicht erzwungen) |
| `TEXT` | `TEXT` |
| `DATE` / `DATETIME` | `TEXT` im Format ISO 8601 (`YYYY-MM-DD` bzw. `YYYY-MM-DD HH:MM:SS`) |
| `YEAR` | `INTEGER` |
| `DECIMAL(x,y)` | `NUMERIC` oder `INTEGER` (Betrag in Cent), um Rundungsfehler zu vermeiden |
| `ENUM` | `TEXT` mit `CHECK (spalte IN (...))` |

Fremdschlüssel (`FOREIGN KEY ... REFERENCES ...`) müssen in SQLite zusätzlich mit `PRAGMA foreign_keys = ON;` aktiviert werden, sonst werden sie nicht geprüft.

## Offene Punkte

- Werte für `mietobjekte.typ` sind ein Vorschlag — im Team bestätigen.
- Tabellen und Spaltennamen hier richten sich nach `WohnPilot_ER_Modell_v2`. Das ältere Diagramm `WohnPilot_ERModel_erweitert` ist der erste Entwurf und gilt nicht mehr.
- `schema.sql` mit den tatsächlichen `CREATE TABLE`-Befehlen folgt in Sprint 2 (Datenbank-Wart: Benjamin).
