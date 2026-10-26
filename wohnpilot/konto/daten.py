def hole_nutzerkonto_nach_nutzername(verbindung, benutzername):
    """Sucht ein Benutzerkonto mit dem eingegebenen Namen."""
    sql = """
        SELECT benutzer_id, benutzername, passwort, vorname, nachname,
               email, telefon, strasse, hausnummer, plz, ort, rolle
        FROM benutzer
        WHERE benutzername = ?
    """
    return verbindung.execute(sql, (benutzername,)).fetchall()


def anmelden(verbindung, benutzername, passwort):
    """Prüft die Zugangsdaten und gibt das Konto ohne Passwort zurück."""
    if not benutzername or not passwort:
        return None

    konten = hole_nutzerkonto_nach_nutzername(verbindung, benutzername.strip())

    # Nur genau ein Konto mit diesem Namen darf sich anmelden.
    if len(konten) != 1:
        return None

    konto = konten[0]
    if konto["passwort"] != passwort:
        return None

    angemeldetes_konto = {}
    for spalte in konto.keys():
        if spalte != "passwort":
            angemeldetes_konto[spalte] = konto[spalte]

    return angemeldetes_konto
