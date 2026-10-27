from ..wohnpilot_db_create import verbinden


def lade_kontaktdaten(benutzer_id):
    conn = verbinden()
    try:
        zeile = conn.execute(
            """
            SELECT benutzername, vorname, nachname, email, telefon,
                   strasse, hausnummer, plz, ort
            FROM benutzer
            WHERE benutzer_id = ?
            """,
            (benutzer_id,),
        ).fetchone()

        return zeile
    finally:
        conn.close()


def kontaktdaten(benutzer_id): #Bekommt den parameter von Menu
    benutzer = lade_kontaktdaten(benutzer_id) #Holt sich die Daten aus der DB anhand der benutzer_id


    if benutzer is None: #wenn nicht logged in = keine Kekse
        print("Benutzer nicht gefunden.")
    else:
        print("----------------------------------")  
        print(f"Persönliche Daten von {benutzer['benutzername']}")
        print("----------------------------------")
        print(f"Name: {benutzer['vorname']} {benutzer['nachname']}")
        print(f"E-Mail: {benutzer['email']}")
        print(f"Telefon: {benutzer['telefon']}")
        print(f"Adresse: {benutzer['strasse']} {benutzer['hausnummer']}, "
              f"{benutzer['plz']} {benutzer['ort']}")
        print("----------------------------------")


    
