from wohnpilot_db import datenbank_erstellen

SPALTEN = (
    "benutzername", "passwort_hash", "vorname", "nachname", "email",
    "telefon", "strasse", "hausnummer", "plz", "ort", "rolle", "erstellt_am",
)

BENUTZER = [
    # ---------- 5 VERWALTER ----------
    ("greta.hofmann", "$2y$10$TestHashGreta011", "Greta", "Hofmann",
     "greta.hofmann@wohnpilot.example", "0171 28463915",
     "Verwalterweg", "4", "10115", "Berlin", "verwalter", "2021-03-14 08:15:00"),
    ("leonhard.eichen", "$2y$10$TestHashLeonhard012", "Leonhard", "Eichen",
     "leonhard.eichen@wohnpilot.example", "0172 39581724",
     "Ahornstraße", "31", "04109", "Leipzig", "verwalter", "2021-09-27 10:40:00"),
    ("amina.berghaus", "$2y$10$TestHashAmina013", "Amina", "Berghaus",
     "amina.berghaus@wohnpilot.example", "0163 74829105",
     "Panoramaweg", "12", "70173", "Stuttgart", "verwalter", "2022-05-18 13:25:00"),
    ("finn.silber", "$2y$10$TestHashFinn014", "Finn", "Silber",
     "finn.silber@wohnpilot.example", "0157 81946327",
     "Silberstraße", "9", "20095", "Hamburg", "verwalter", "2023-02-06 09:05:00"),
    ("ronja.talblick", "$2y$10$TestHashRonja015", "Ronja", "Talblick",
     "ronja.talblick@wohnpilot.example", "0175 62918430",
     "Bergwiesenweg", "27", "53111", "Bonn", "verwalter", "2024-08-21 15:50:00"),

    # ---------- 2 ADMINS ----------
    ("maximilian.root", "$2y$10$TestHashMax016", "Maximilian", "Kern",
     "maximilian.kern@wohnpilot.example", "0170 38472916",
     "Datenweg", "1", "60311", "Frankfurt am Main", "admin", "2021-01-10 08:00:00"),
    ("nora.system", "$2y$10$TestHashNora017", "Nora", "Falkenstein",
     "nora.falkenstein@wohnpilot.example", "0161 57293840",
     "Serverallee", "42", "40213", "Düsseldorf", "admin", "2022-11-03 11:30:00"),

    # ---------- 10 MIETER ----------
    ("mila.sonnenberg", "$2y$10$TestHashMila001", "Mila", "Sonnenberg",
     "mila.sonnenberg@example.de", "0151 38174295",
     "Mondscheinweg", "7", "01067", "Dresden", "mieter", "2022-02-17 09:12:00"),
    ("theo.fuchs", "$2y$10$TestHashTheo002", "Theo", "Fuchs",
     "theo.fuchs@example.de", "0176 49281736",
     "Kupfergasse", "14", "90402", "Nürnberg", "mieter", "2022-07-29 14:35:00"),
    ("juno.winter", "$2y$10$TestHashJuno003", "Juno", "Winter",
     "juno.winter@example.de", "0160 58392417",
     "Schneeglöckchenstraße", "22", "24103", "Kiel", "mieter", "2022-12-11 11:20:00"),
    ("moritz.stein", "$2y$10$TestHashMoritz004", "Moritz", "Stein",
     "moritz.stein@example.de", "0157 29461853",
     "Hafenblick", "3", "23552", "Lübeck", "mieter", "2023-04-23 16:05:00"),
    ("elara.morgenstern", "$2y$10$TestHashElara005", "Elara", "Morgenstern",
     "elara.morgenstern@example.de", "0178 61749382",
     "Sternenallee", "18", "50667", "Köln", "mieter", "2023-09-15 08:45:00"),
    ("jonte.adler", "$2y$10$TestHashJonte006", "Jonte", "Adler",
     "jonte.adler@example.de", "0162 73849105",
     "Eichenbogen", "11", "79102", "Freiburg", "mieter", "2024-01-08 13:10:00"),
    ("livia.mond", "$2y$10$TestHashLivia007", "Livia", "Mond",
     "livia.mond@example.de", "0152 84619370",
     "Rosengartenweg", "5", "80331", "München", "mieter", "2024-06-19 10:30:00"),
    ("caspar.wolkenstein", "$2y$10$TestHashCaspar008", "Caspar", "Wolkenstein",
     "caspar.wolkenstein@example.de", "0173 92517468",
     "Wiesenpfad", "29", "34117", "Kassel", "mieter", "2024-11-02 15:40:00"),
    ("freya.koenig", "$2y$10$TestHashFreya009", "Freya", "König",
     "freya.koenig@example.de", "0163 47182950",
     "Birkenhang", "8", "01069", "Dresden", "mieter", "2025-05-27 09:55:00"),
    ("ruben.sturm", "$2y$10$TestHashRuben010", "Ruben", "Sturm",
     "ruben.sturm@example.de", "0159 63827104",
     "Waldwinkel", "16", "48143", "Münster", "mieter", "2026-02-14 12:25:00"),
]


def benutzer_einfuegen(conn):
    """Fügt die Testbenutzer ein. Bereits vorhandene Benutzernamen werden übersprungen,
    damit mehrfaches Ausführen keine Duplikate erzeugt (benutzername ist nicht UNIQUE)."""
    sql = (
        f"INSERT INTO benutzer ({', '.join(SPALTEN)}) "
        f"VALUES ({', '.join('?' * len(SPALTEN))})" # Platzhalter
    )
    eingefuegt = 0 # zählt, wie viele Benutzer hinzugefügt wurden
    for zeile in BENUTZER:
        vorhanden = conn.execute(
            "SELECT 1 FROM benutzer WHERE benutzername = ?", (zeile[0],)
        ).fetchone() # liefert den ersten Treffer oder None
        if vorhanden:
            continue # bei Duplikaten wird übersprungen
        conn.execute(sql, zeile)
        eingefuegt += 1
    conn.commit()
    return eingefuegt


if __name__ == "__main__": # prüft, ob die Datei direkt gestartet wurde
    conn = datenbank_erstellen() # erstellt oder öffnet, wenn vorhanden, die Datenbank
    anzahl = benutzer_einfuegen(conn) # fügt Benutzer hinzu und speichert die Anzahl
    print(f"{anzahl} Benutzer eingefügt.")
    for z in conn.execute( # zählt die Benutzer je Rolle und sortiert sie alphabetisch
        "SELECT rolle, COUNT(*) AS anzahl FROM benutzer GROUP BY rolle ORDER BY rolle"
    ):
        print(f"{z['rolle']}: {z['anzahl']}")
    conn.close()
