from getpass import getpass

from ..wohnpilot_db_create import datenbank_erstellen
from .daten import hole_nutzerkonto_nach_benutzername


def anmelden(verbindung):
    # Benutzername und Passwort im Terminal abfragen.
    benutzername = input("Benutzername: ")
    passwort = getpass("Passwort: ")

    # In der Datenbank das Konto zum eingegebenen Namen suchen.
    nutzerkonto = hole_nutzerkonto_nach_benutzername(verbindung, benutzername)

    # In diesem einfachen Lernschritt vergleichen wir das Testpasswort direkt.
    # Bei falschem Namen oder Passwort wird die Anmeldung abgelehnt.
    if nutzerkonto is None or passwort != nutzerkonto["passwort_hash"]:
        print("Anmeldung nicht möglich - falsche Eingaben.")
        return None

    # Nur diese Kontodaten bleiben während der Anmeldung im Programm.
    angemeldetes_konto = {
        "benutzer_id": nutzerkonto["benutzer_id"],
        "benutzername": nutzerkonto["benutzername"],
        "vorname": nutzerkonto["vorname"],
        "rolle": nutzerkonto["rolle"],
    }
    print("Anmeldung erfolgreich. Hallo", angemeldetes_konto["vorname"] + "!")
    return angemeldetes_konto

 
# # main zu Testzwecken, damit man die Anmeldung direkt ausprobieren kann.
# Später ruft die zentrale main() die Funktion anmelden() auf.
# Testdaten: benutzername: login.test, passwort: test123

def main():
    # Datenbank öffnen und Tabellen bei Bedarf anlegen.
    verbindung = datenbank_erstellen()

    # Die Verbindung auch dann schließen, wenn die Anmeldung fehlschlägt.
    try:
        nutzerkonto = anmelden(verbindung)

        # Bei erfolgreicher Anmeldung bleibt das Konto bis zum Enter angemeldet.
        if nutzerkonto is not None:
            input("Du bist angemeldet. Zum Abmelden Enter drücken.")
            print("Du bist jetzt abgemeldet.")
    finally:
        verbindung.close()


if __name__ == "__main__":
    # Dieser Start wird ausgeführt, wenn die Datei als Modul gestartet wird.
    main()
