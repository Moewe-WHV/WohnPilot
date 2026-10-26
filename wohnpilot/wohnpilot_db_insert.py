from wohnpilot.wohnpilot_db import datenbank_erstellen

SPALTEN = (
    "benutzername", "passwort", "vorname", "nachname", "email",
    "telefon", "strasse", "hausnummer", "plz", "ort", "rolle", "erstellt_am",
)

BENUTZER = [
    # ---------- 5 VERWALTER ----------
    ("greta.hofmann", "wohnpilot123", "Greta", "Hofmann",
     "greta.hofmann@wohnpilot.example", "0171 28463915",
     "Verwalterweg", "4", "10115", "Berlin", "verwalter", "2021-03-14 08:15:00"),
    ("leonhard.eichen", "wohnpilot123", "Leonhard", "Eichen",
     "leonhard.eichen@wohnpilot.example", "0172 39581724",
     "Ahornstraße", "31", "04109", "Leipzig", "verwalter", "2021-09-27 10:40:00"),
    ("amina.berghaus", "wohnpilot123", "Amina", "Berghaus",
     "amina.berghaus@wohnpilot.example", "0163 74829105",
     "Panoramaweg", "12", "70173", "Stuttgart", "verwalter", "2022-05-18 13:25:00"),
    ("finn.silber", "wohnpilot123", "Finn", "Silber",
     "finn.silber@wohnpilot.example", "0157 81946327",
     "Silberstraße", "9", "20095", "Hamburg", "verwalter", "2023-02-06 09:05:00"),
    ("ronja.talblick", "wohnpilot123", "Ronja", "Talblick",
     "ronja.talblick@wohnpilot.example", "0175 62918430",
     "Bergwiesenweg", "27", "53111", "Bonn", "verwalter", "2024-08-21 15:50:00"),
    # ---------- 2 ADMINS ----------
    ("maximilian.root", "wohnpilot123", "Maximilian", "Kern",
     "maximilian.kern@wohnpilot.example", "0170 38472916",
     "Datenweg", "1", "60311", "Frankfurt am Main", "admin", "2021-01-10 08:00:00"),
    ("nora.system", "wohnpilot123", "Nora", "Falkenstein",
     "nora.falkenstein@wohnpilot.example", "0161 57293840",
     "Serverallee", "42", "40213", "Düsseldorf", "admin", "2022-11-03 11:30:00"),
    # ---------- 10 MIETER ----------
    ("mila.sonnenberg", "wohnpilot123", "Mila", "Sonnenberg",
     "mila.sonnenberg@example.de", "0151 38174295",
     "Mondscheinweg", "7", "01067", "Dresden", "mieter", "2022-02-17 09:12:00"),
    ("theo.fuchs", "wohnpilot123", "Theo", "Fuchs",
     "theo.fuchs@example.de", "0176 49281736",
     "Kupfergasse", "14", "90402", "Nürnberg", "mieter", "2022-07-29 14:35:00"),
    ("juno.winter", "wohnpilot123", "Juno", "Winter",
     "juno.winter@example.de", "0160 58392417",
     "Schneeglöckchenstraße", "22", "24103", "Kiel", "mieter", "2022-12-11 11:20:00"),
    ("moritz.stein", "wohnpilot123", "Moritz", "Stein",
     "moritz.stein@example.de", "0157 29461853",
     "Hafenblick", "3", "23552", "Lübeck", "mieter", "2023-04-23 16:05:00"),
    ("elara.morgenstern", "wohnpilot123", "Elara", "Morgenstern",
     "elara.morgenstern@example.de", "0178 61749382",
     "Sternenallee", "18", "50667", "Köln", "mieter", "2023-09-15 08:45:00"),
    ("jonte.adler", "wohnpilot123", "Jonte", "Adler",
     "jonte.adler@example.de", "0162 73849105",
     "Eichenbogen", "11", "79102", "Freiburg", "mieter", "2024-01-08 13:10:00"),
    ("livia.mond", "wohnpilot123", "Livia", "Mond",
     "livia.mond@example.de", "0152 84619370",
     "Rosengartenweg", "5", "80331", "München", "mieter", "2024-06-19 10:30:00"),
    ("caspar.wolkenstein", "wohnpilot123", "Caspar", "Wolkenstein",
     "caspar.wolkenstein@example.de", "0173 92517468",
     "Wiesenpfad", "29", "34117", "Kassel", "mieter", "2024-11-02 15:40:00"),
    ("freya.koenig", "wohnpilot123", "Freya", "König",
     "freya.koenig@example.de", "0163 47182950",
     "Birkenhang", "8", "01069", "Dresden", "mieter", "2025-05-27 09:55:00"),
    ("ruben.sturm", "wohnpilot123", "Ruben", "Sturm",
     "ruben.sturm@example.de", "0159 63827104",
     "Waldwinkel", "16", "48143", "Münster", "mieter", "2026-02-14 12:25:00"),

    # Nur für den lokalen Login-Test: Das Passwort lautet "test123".
    # Dieses einfache Testpasswort niemals für echte Konten verwenden.
    ("login.test", "test123", "Login", "Test",
     "login.test@wohnpilot.example", None, None, None, None, None,
     "mieter", "2026-10-20 12:00:00"),
]


def benutzer_einfuegen(conn):
    """Fügt Testbenutzer ein oder setzt deren Testpasswort erneut."""
    sql = (
        f"INSERT INTO benutzer ({', '.join(SPALTEN)}) "
        f"VALUES ({', '.join('?' * len(SPALTEN))})"
    )
    benutzernamen = []
    for zeile in BENUTZER:
        vorhanden = conn.execute(
            "SELECT 1 FROM benutzer WHERE benutzername = ?", (zeile[0],)
        ).fetchone()
        if vorhanden:
            # So bekommen auch vorhandene Testkonten wieder das Testpasswort.
            conn.execute(
                "UPDATE benutzer SET passwort = ? WHERE benutzername = ?",
                (zeile[1], zeile[0]),
            )
        else:
            conn.execute(sql, zeile)
        benutzernamen.append(zeile[0])
    conn.commit()
    return benutzernamen


if __name__ == "__main__":
    conn = datenbank_erstellen()
    benutzernamen = benutzer_einfuegen(conn)
    print(f"{len(benutzernamen)} Testkonten sind bereit.")
    print("Alle Testkonten verwenden dasselbe Passwort: wohnpilot123")
    for benutzername in benutzernamen:
        print(benutzername)
    for z in conn.execute(
        "SELECT rolle, COUNT(*) AS anzahl FROM benutzer GROUP BY rolle ORDER BY rolle"
    ):
        print(f"{z['rolle']}: {z['anzahl']}")
    conn.close()
