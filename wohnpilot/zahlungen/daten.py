"""Datenschicht

mietzahlungen(verbindung, mieter_id):
SQL-Abfrage mit JOIN, WHERE m.mieter_id = ? und ORDER BY.
Jeder Mieter sieht nur seine eigenen Zahlungen: Mila 5, Theo 4, Juno 0.
ermittle_status(status, faelligkeitsdatum, heute):
bestimmt den Status bezahlt, überfällig oder offen.
Überfällige Zahlungen werden über das Datum erkannt,
auch wenn sie in der Datenbank noch als offen stehen.
"""

from datetime import date


def mietzahlungen(verbindung, mieter_id):
    """Liefert alle Zahlungen aus den Mietverträgen des angegebenen Mieters."""
    abfrage = """
        SELECT
        m.mietvertrag_id, z.zahlungsdatum, z.faelligkeitsdatum, z.betrag, z.status
        from
        mietvertraege m
        join zahlungen z
        on
        m.mietvertrag_id = z.mietvertrag_id
        where
        m.mieter_id = ?
        order by faelligkeitsdatum ASC;
    """
    return verbindung.execute(abfrage, (mieter_id,)).fetchall()


heute = date.today().isoformat()


def ermittle_status(status, faelligkeitsdatum, heute):
    """Bestimmt, ob eine Zahlung bezahlt, offen oder überfällig ist."""
    if status == "bezahlt":
        return "bezahlt"
    elif faelligkeitsdatum < heute:
        return "überfällig"
    else:
        return "offen"


# Wird nur ausgeführt, wenn man die Datei direkt startet (nicht beim Import)
if __name__ == "__main__":
    from datetime import date
    from wohnpilot.wohnpilot_db_create import verbinden

    verbindung = verbinden("wohnpilot/wohnpilot.db")
    for mieter_id in (8, 9, 10):
        zahlungen = mietzahlungen(verbindung, mieter_id)
        print(f"Mieter {mieter_id}: {len(zahlungen)} Zahlungen")
        for zeile in zahlungen:
            status_neu = ermittle_status(
                zeile["status"], zeile["faelligkeitsdatum"], heute
            )
            print("   ", zeile["faelligkeitsdatum"], status_neu)
    verbindung.close()
