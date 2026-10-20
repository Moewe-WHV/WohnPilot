def hole_nutzerkonto_nach_benutzername(verbindung, benutzername):
    # Die Abfrage holt das Konto mit diesem Benutzernamen aus der Datenbank.
    abfrage = """
        SELECT benutzer_id, benutzername, passwort_hash, vorname, rolle
        FROM benutzer
        WHERE benutzername = ?
    """

    # Das Fragezeichen wird durch den eingegebenen Benutzernamen ersetzt.
    nutzerkonto = verbindung.execute(abfrage, (benutzername,)).fetchone()

    # Wenn es den Namen nicht gibt, ist das Ergebnis None.
    return nutzerkonto
