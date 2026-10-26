"""Testdaten

wohnpilot_testdaten_zahlungen.py erstellt: 2 Wohnungen, 2 Mietverträge (Mila und Theo)
und 9 Zahlungen, eingefügt mit executemany.
Das Skript prüft vorher mit SELECT COUNT(*), ob schon Zahlungen da sind. 
Beim zweiten Ausführen wird deshalb nichts doppelt eingefügt."""


from wohnpilot_db_create import datenbank_erstellen

MIETOBJEKTE = [
    # (typ, strasse, hausnummer, wohnungsnummer, plz, ort)
    ("wohnung", "Testallee", "5", "1. OG links", "47441", "Moers"),
    ("wohnung", "Testallee", "5", "2. OG rechts", "47441", "Moers"),
]

MIETVERTRAEGE = [
    # (mieter_id, verwalter_id, mietobjekt_id, vertragsbeginn, vertragsende,
    # kaltmiete, nebenkostenvorauszahlung, kaution, erstellt_am)
    (8, 1, 1, "2026-07-01", None, 75000, 18000, 225000, "2026-06-15 10:00:00"),
    (9, 1, 2, "2026-08-01", None, 62000, 15000, 186000, "2026-07-20 10:00:00"),
]

ZAHLUNGEN = [
    # (mietvertrag_id, zahlungsdatum, faelligkeitsdatum, betrag, status)
    # Mila
    (1, "2026-07-01", "2026-07-03", 93000, "bezahlt"),
    (1, "2026-08-02", "2026-08-03", 93000, "bezahlt"),
    (1, "2026-09-10", "2026-09-03", 93000, "bezahlt"),  # zu spät, aber bezahlt
    (1, None, "2026-10-03", 93000, "offen"),  # Datum schon vorbei!
    (1, None, "2026-11-03", 93000, "offen"),
    # Theo
    (2, "2026-08-01", "2026-08-03", 77000, "bezahlt"),
    (2, None, "2026-09-03", 77000, "offen"),  # Datum schon vorbei!
    (2, "2026-10-01", "2026-10-03", 77000, "bezahlt"),
    (2, None, "2026-11-03", 77000, "offen"),
]


def testdaten_einfuegen(conn):
    """Fügt Testdaten für Mietobjekte, Mietverträge und Zahlungen ein.

    Sind schon Zahlungen in der Datenbank, wird nichts eingefügt,
    damit beim mehrfachen Ausführen keine Duplikate entstehen.
    Gibt die Anzahl der eingefügten Zahlungen zurück.
    """
    # Wenn schon Zahlungen da sind, nichts einfügen (sonst Duplikate)
    anzahl_vorhanden = conn.execute("SELECT COUNT(*) FROM zahlungen").fetchone()[0]
    if anzahl_vorhanden > 0:  # Wenn die Tabelle schon Zahlungen enthält, endet die Funktion hier
        return 0

    conn.executemany(
        "INSERT INTO mietobjekte (typ, strasse, hausnummer, wohnungsnummer, plz, ort) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        MIETOBJEKTE,
    )
    conn.executemany(
        """
        INSERT INTO mietvertraege (
            mieter_id, verwalter_id, mietobjekt_id,
            vertragsbeginn, vertragsende, kaltmiete,
            nebenkostenvorauszahlung, kaution, erstellt_am
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        MIETVERTRAEGE,
    )
    conn.executemany(
        """
        INSERT INTO zahlungen (
            mietvertrag_id, zahlungsdatum,
            faelligkeitsdatum, betrag, status
        )
        VALUES (?, ?, ?, ?, ?)""",
        ZAHLUNGEN,
    )

    conn.commit()
    return len(ZAHLUNGEN)


if __name__ == "__main__":
    conn = datenbank_erstellen()
    anzahl = testdaten_einfuegen(conn)
    print(f"{anzahl} Zahlungen eingefügt.")
    conn.close()
