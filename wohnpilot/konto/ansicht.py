from getpass import getpass

from wohnpilot.konto.daten import anmelden as pruefe_anmeldung
from wohnpilot.wohnpilot_db import datenbank_erstellen


def anmelden(verbindung):
    """Fragt den Namen und das Passwort ab."""
    benutzername = input("Benutzername: ")
    passwort = getpass("Passwort: ")

    konto = pruefe_anmeldung(verbindung, benutzername, passwort)
    if konto is None:
        print("Anmeldung nicht möglich - falsche Eingaben.")
        return None

    print("Anmeldung erfolgreich. Hallo", konto["vorname"] + "!")
    return konto


def main():
    """Startet den Login und beendet die Sitzung nach Enter."""
    verbindung = datenbank_erstellen()
    try:
        konto = anmelden(verbindung)
        if konto is not None:
            input("Du bist angemeldet. Zum Abmelden Enter drücken.")
            print("Du bist jetzt abgemeldet.")
    finally:
        verbindung.close()


if __name__ == "__main__":
    main()
