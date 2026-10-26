"""Anzeige

cent_als_euro(): wandelt 93000 in 930,00 € um, ohne float.
datum_deutsch(): wandelt 2026-10-03 in 03.10.2026 um und None in -.
zeige_zahlungen(verbindung, mieter_id): gibt für jede Zahlung Betrag, Zahlungsdatum,
Fälligkeitsdatum und den berechneten Status aus."""

from datetime import date

from wohnpilot.zahlungen.daten import ermittle_status, mietzahlungen


def cent_als_euro(betrag_cent):
    """Wandelt einen Betrag in Cent in einen Euro-Text um,
    z. B. 93000 -> '930,00 €'."""
    euro = betrag_cent // 100
    cent = betrag_cent % 100
    return f"{euro},{cent:02d} €"


def datum_deutsch(iso_datum):
    """Wandelt ein Datum von '2026-10-03' in '03.10.2026' um,
    leeres Datum wird '-'."""
    if not iso_datum:
        return "-"
    else:
        jahr, monat, tag = iso_datum.split("-")
        return f"{tag}.{monat}.{jahr}"


def zeige_zahlungen(verbindung, mieter_id):
    """Zeigt dem Mieter seine Mietzahlungen als Tabelle im Terminal."""
    heute = date.today().isoformat()
    zahlungen = mietzahlungen(verbindung, mieter_id)

    for zeile in zahlungen:
        status = ermittle_status(zeile["status"], zeile["faelligkeitsdatum"], heute)
        print(
            f'Betrag: {cent_als_euro(zeile["betrag"])}, '
            f'Zahlungsdatum: {datum_deutsch(zeile["zahlungsdatum"])}, '
            f'Fälligkeitsdatum: {datum_deutsch(zeile["faelligkeitsdatum"])}, '
            f"Status: {status}"
        )


if __name__ == "__main__":
    from wohnpilot.wohnpilot_db_create import verbinden

    verbindung = verbinden("wohnpilot/wohnpilot.db")
    zeige_zahlungen(verbindung, 8)
    verbindung.close()
