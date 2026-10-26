import sqlite3

from wohnpilot.konto.daten import anmelden
from wohnpilot.wohnpilot_db import datenbank_erstellen


def test_anmelden_mit_richtigen_daten():
    verbindung = datenbank_erstellen(":memory:")
    verbindung.execute(
        """
        INSERT INTO benutzer (
            benutzername, passwort, vorname, nachname, email, rolle,
            erstellt_am
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "mila",
            "wohnpilot123",
            "Mila",
            "Sonnenberg",
            "mila@example.de",
            "mieter",
            "2026-01-01",
        ),
    )

    konto = anmelden(verbindung, "mila", "wohnpilot123")

    assert konto["benutzername"] == "mila"
    assert konto["rolle"] == "mieter"
    assert "passwort" not in konto
    verbindung.close()


def test_anmelden_mit_falschem_passwort():
    verbindung = datenbank_erstellen(":memory:")
    verbindung.execute(
        """
        INSERT INTO benutzer (
            benutzername, passwort, vorname, nachname, email, rolle,
            erstellt_am
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "mila",
            "wohnpilot123",
            "Mila",
            "Sonnenberg",
            "mila@example.de",
            "mieter",
            "2026-01-01",
        ),
    )

    konto = anmelden(verbindung, "mila", "falsch")

    assert konto is None
    verbindung.close()


def test_anmelden_mit_doppeltem_nutzernamen():
    verbindung = datenbank_erstellen(":memory:")
    for vorname in ("Mila", "Mira"):
        verbindung.execute(
            """
            INSERT INTO benutzer (
                benutzername, passwort, vorname, nachname, email, rolle,
                erstellt_am
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "doppelt",
                "wohnpilot123",
                vorname,
                "Test",
                f"{vorname}@example.de",
                "mieter",
                "2026-01-01",
            ),
        )

    konto = anmelden(verbindung, "doppelt", "wohnpilot123")

    assert konto is None
    verbindung.close()


def test_datenbank_benennent_alte_passwort_spalte_um(tmp_path):
    datenbank_pfad = tmp_path / "alte_datenbank.db"
    alte_verbindung = sqlite3.connect(datenbank_pfad)
    alte_verbindung.execute("""
        CREATE TABLE benutzer (
            benutzer_id INTEGER PRIMARY KEY,
            passwort_hash TEXT NOT NULL
        )
        """)
    alte_verbindung.close()

    verbindung = datenbank_erstellen(datenbank_pfad)
    spalten = [
        spalte["name"] for spalte in verbindung.execute("PRAGMA table_info(benutzer)")
    ]

    assert "passwort" in spalten
    assert "passwort_hash" not in spalten
    verbindung.close()
