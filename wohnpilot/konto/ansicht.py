import getpass

from wohnpilot.konto.daten import anmelden
from wohnpilot.wohnpilot_db import datenbank_erstellen

FEHLERMELDUNG_ANMELDUNG = "Anmeldung nicht möglich - falsche Eingaben."


def anmeldeansicht(
    verbindung,
    eingabe=input,
    passwort_eingabe=getpass.getpass,
    ausgabe=print,
):
    """Fragt Zugangsdaten ab und gibt das angemeldete Konto zurück."""
    # getpass zeigt das eingegebene Passwort nicht auf dem Bildschirm an.
    benutzername = eingabe("Nutzername: ").strip()
    passwort = passwort_eingabe("Passwort: ")

    konto = anmelden(verbindung, benutzername, passwort)
    if konto is None:
        # Für falsche Namen und falsche Passwörter erscheint dieselbe Meldung.
        ausgabe(FEHLERMELDUNG_ANMELDUNG)
        return None

    ausgabe(f"Willkommen, {konto['vorname']} {konto['nachname']}!")
    ausgabe(f"Angemeldet als: {konto['rolle']}")
    return konto


def main():
    """Startet die Anmeldemaske mit der WohnPilot-Datenbank."""
    # Das vorhandene Schema wird angelegt, falls es noch nicht existiert.
    verbindung = datenbank_erstellen()
    try:
        anmeldeansicht(verbindung)
    finally:
        # Die Datenbankverbindung wird auch nach einer Fehlermeldung geschlossen.
        verbindung.close()


if __name__ == "__main__":
    main()
