def hole_nutzerkonto_nach_nutzername(verbindung, benutzername):
    """Sucht ein Benutzerkonto anhand des Nutzernamens."""
    sql = """
        SELECT benutzer_id, benutzername, passwort, vorname, nachname,
               email, telefon, strasse, hausnummer, plz, ort, rolle
        FROM benutzer
        WHERE benutzername = ?
    """
    return verbindung.execute(sql, (benutzername,)).fetchone()


def pruefe_anmeldung(verbindung, benutzername, passwort):
    """Prüft die Zugangsdaten und gibt das Konto ohne Passwort zurück."""
    konto = hole_nutzerkonto_nach_nutzername(verbindung, benutzername.strip())

    if konto is None:
        return None

    if konto["passwort"] != passwort:
        return None

    angemeldetes_konto = {
        "benutzer_id": konto["benutzer_id"],
        "benutzername": konto["benutzername"],
        "vorname": konto["vorname"],
        "rolle": konto["rolle"],
    }
    return angemeldetes_konto
