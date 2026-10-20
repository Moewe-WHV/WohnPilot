import sqlite3 # Python-Modul für Verbindung zu SQLite

DB_PFAD = "wohnpilot.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS benutzer (
    benutzer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    benutzername TEXT NOT NULL COLLATE NOCASE, -- SQLite für: Groß- und Kleinschreibung werden bei Abfragen ignoriert
    passwort_hash TEXT NOT NULL,
    vorname TEXT NOT NULL,
    nachname TEXT NOT NULL,
    email TEXT NOT NULL COLLATE NOCASE,
    telefon TEXT,
    strasse TEXT,
    hausnummer TEXT,
    plz TEXT,
    ort TEXT,
    rolle TEXT NOT NULL CHECK (rolle IN ('mieter', 'verwalter', 'admin')),
    erstellt_am TEXT NOT NULL -- ISO-Format: 'YYYY-MM-DD HH:MM:SS'
);

CREATE TABLE IF NOT EXISTS mietobjekte (
    mietobjekt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    typ TEXT NOT NULL CHECK (typ IN ('wohnung', 'haus')),
    strasse TEXT NOT NULL,
    hausnummer TEXT NOT NULL,
    wohnungsnummer TEXT,
    plz TEXT NOT NULL,
    ort TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS mietvertraege (
    mietvertrag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mieter_id INTEGER NOT NULL,
    verwalter_id INTEGER NOT NULL,
    mietobjekt_id INTEGER NOT NULL,
    vertragsbeginn TEXT NOT NULL, -- 'YYYY-MM-DD'
    vertragsende TEXT,
    kaltmiete INTEGER NOT NULL,
    nebenkostenvorauszahlung INTEGER NOT NULL,
    kaution INTEGER,
    erstellt_am TEXT NOT NULL,
    pdf TEXT,

    CONSTRAINT FK_mietvertraege_mieter_id -- CONSTRAINT leitet die Definition einer Regel ein
        FOREIGN KEY (mieter_id)
        REFERENCES benutzer (benutzer_id)
        ON DELETE RESTRICT, -- Benutzer darf nicht gelöscht werden, solange noch ein Mietvertrag besteht

    CONSTRAINT FK_mietvertraege_verwalter_id
        FOREIGN KEY (verwalter_id)
        REFERENCES benutzer (benutzer_id)
        ON DELETE RESTRICT,

    CONSTRAINT FK_mietvertraege_mietobjekt_id
        FOREIGN KEY (mietobjekt_id)
        REFERENCES mietobjekte (mietobjekt_id)
        ON DELETE RESTRICT
);

-- mittels Index können Abfragen schneller durchgeführt werden (ohne jedesmal die gesamte Tabelle zu durchsuchen)
CREATE INDEX IF NOT EXISTS idx_mietvertraege_mieter_id ON mietvertraege (mieter_id);
CREATE INDEX IF NOT EXISTS idx_mietvertraege_verwalter_id ON mietvertraege (verwalter_id);
CREATE INDEX IF NOT EXISTS idx_mietvertraege_mietobjekt_id ON mietvertraege (mietobjekt_id);

CREATE TABLE IF NOT EXISTS mietvertragsdokumente (
    dokument_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mietvertrag_id INTEGER NOT NULL,
    dateiname TEXT NOT NULL,
    dateipfad TEXT NOT NULL,
    hochgeladen_am TEXT NOT NULL,

    CONSTRAINT FK_mietvertragsdokumente_mietvertrag_id
        FOREIGN KEY (mietvertrag_id)
        REFERENCES mietvertraege (mietvertrag_id)
        ON DELETE RESTRICT -- solange ein Mietvertragsdokument auf den Mietvertrag verweist, darf der Mietvertrag nicht gelöscht werden
);

CREATE INDEX IF NOT EXISTS idx_mietvertragsdokumente_mietvertrag_id ON mietvertragsdokumente (mietvertrag_id);

CREATE TABLE IF NOT EXISTS nachrichten (
    nachricht_id INTEGER PRIMARY KEY AUTOINCREMENT,
    absender_id INTEGER NOT NULL,
    empfaenger_id INTEGER NOT NULL,
    titel TEXT NOT NULL,
    inhalt TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('gesendet', 'gelesen')),
    erstellt_am TEXT NOT NULL,

    CONSTRAINT FK_nachrichten_absender_id
        FOREIGN KEY (absender_id)
        REFERENCES benutzer (benutzer_id)
        ON DELETE RESTRICT,

    CONSTRAINT FK_nachrichten_empfaenger_id
        FOREIGN KEY (empfaenger_id)
        REFERENCES benutzer (benutzer_id)
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_nachrichten_absender_id ON nachrichten (absender_id);
CREATE INDEX IF NOT EXISTS idx_nachrichten_empfaenger_id ON nachrichten (empfaenger_id);

CREATE TABLE IF NOT EXISTS zahlungen (
    zahlung_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mietvertrag_id INTEGER NOT NULL,
    zahlungsdatum TEXT,
    faelligkeitsdatum TEXT NOT NULL,
    betrag INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('offen', 'bezahlt', 'überaellig')),

    CONSTRAINT FK_zahlungen_mietvertrag_id
        FOREIGN KEY (mietvertrag_id)
        REFERENCES mietvertraege (mietvertrag_id)
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_zahlungen_mietvertrag_id ON zahlungen (mietvertrag_id);

CREATE TABLE IF NOT EXISTS zaehler (
    zaehler_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mietobjekt_id INTEGER NOT NULL,
    zaehlerart TEXT NOT NULL CHECK (zaehlerart IN ('strom', 'gas', 'wasser')),
    zaehlernummer TEXT NOT NULL,

    CONSTRAINT FK_zaehler_mietobjekt_id 
        FOREIGN KEY (mietobjekt_id)
        REFERENCES mietobjekte (mietobjekt_id)
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_zaehler_mietobjekt_id ON zaehler (mietobjekt_id);

CREATE TABLE IF NOT EXISTS zaehlerstaende (
    zaehlerstand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    zaehler_id INTEGER NOT NULL,
    ablesedatum TEXT NOT NULL,
    zaehlerstand NUMERIC NOT NULL,
    erstellt_am TEXT NOT NULL,

    CONSTRAINT FK_zaehlerstaende_zaehler_id
        FOREIGN KEY (zaehler_id)
        REFERENCES zaehler (zaehler_id)
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_zaehlerstaende_zaehler_id ON zaehlerstaende (zaehler_id);

CREATE TABLE IF NOT EXISTS nebenkostenabrechnungen (
    nebenkostenabrechnung_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mietvertrag_id INTEGER NOT NULL,
    abrechnungsjahr INTEGER NOT NULL, -- 2026
    abrechnungsdatum TEXT NOT NULL, -- 2027-02-17
    gesamtbetrag INTEGER NOT NULL,
    erstellt_am TEXT NOT NULL,
    pdf TEXT,

    CONSTRAINT FK_nebenkostenabrechnungen_mietvertrag_id
        FOREIGN KEY (mietvertrag_id)
        REFERENCES mietvertraege (mietvertrag_id)
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_nebenkostenabrechnungen_mietvertrag_id ON nebenkostenabrechnungen (mietvertrag_id);

CREATE TABLE IF NOT EXISTS wartungsmeldungen (
    wartungsmeldung_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mietobjekt_id INTEGER NOT NULL,
    ersteller_id INTEGER NOT NULL,
    bearbeiter_id INTEGER,
    titel TEXT NOT NULL,
    beschreibung TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('offen', 'in_bearbeitung', 'erledigt', 'abgelehnt')),
    datum_gemeldet TEXT NOT NULL,
    datum_erledigt TEXT,

    CONSTRAINT FK_wartungsmeldungen_mietobjekt_id
        FOREIGN KEY (mietobjekt_id)
        REFERENCES mietobjekte (mietobjekt_id)
        ON DELETE RESTRICT,

    CONSTRAINT FK_wartungsmeldungen_ersteller_id
        FOREIGN KEY (ersteller_id)
        REFERENCES benutzer (benutzer_id)
        ON DELETE RESTRICT,

    CONSTRAINT FK_wartungsmeldungen_bearbeiter_id
        FOREIGN KEY (bearbeiter_id)
        REFERENCES benutzer (benutzer_id)
        ON DELETE SET NULL -- Wird der Benutzer = Bearbeiter gelöscht, wird die bearbeiter_id = NULL
);

CREATE INDEX IF NOT EXISTS idx_wartungsmeldungen_mietobjekt_id ON wartungsmeldungen (mietobjekt_id);
CREATE INDEX IF NOT EXISTS idx_wartungsmeldungen_ersteller_id ON wartungsmeldungen (ersteller_id);
CREATE INDEX IF NOT EXISTS idx_wartungsmeldungen_bearbeiter_id ON wartungsmeldungen (bearbeiter_id);
"""


def verbinden(db_pfad=DB_PFAD):
    # öffnet die Datenbankdatei wohnpilot.db; wenn sie fehlt, wird sie angelegt
    conn = sqlite3.connect(db_pfad)
    # sqlite3.Row ist speichereffizient, weil die Daten nur ein einziges mal abgelegt werden. Beim Aufruf wird der Index ermittelt. 
    conn.row_factory = sqlite3.Row # legt fest, wie die Zeilen aus einer SQLite-Datenbankabfrage dargestellt werden. Anstatt als Tupel werden sie hiermit als Dictionaries angezeigt. 
    # SQLite prüft Fremdschlüssel nur, wenn das pro Verbindung eingeschaltet wird
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def datenbank_erstellen(db_pfad=DB_PFAD):
    # Verbindung zur Datenbank herstellen
    conn = verbinden(db_pfad)
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


if __name__ == "__main__":
    # Dieser Block läuft nur, wenn die Datei direkt gestartet wird, also wenn eine andere py-Datei das Skript importiert
    # ansonsten muss im Terminal "python wohnpilot_db.py" ausgeführt werden, um die Tabellen zu erstellen
    conn = datenbank_erstellen()
    # Entspricht SHOW TABLES in SQL
    for zeile in conn.execute(
        # Tabellen mit sqlite als Präfix werden von der Suche ausgeschlossen, weil es interne Dateien geben kann (von SQLite selbst)
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ):
        print(zeile["name"])
    conn.close()
