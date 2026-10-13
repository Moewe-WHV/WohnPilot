WohnPilot - Anforderungsdokumentation

Zu den WohnPilot Benutzern gehören die Rollen Mieter, Vermieter und Admin.

Das sind unsere 11 User Stories für den Mieter:

1. US09 Anmelden und abmelden
        Anmeldung: Eingabe des Nutzernamens und des verdeckten Passworts
            Erfolgreich: Benutzer gelangt zum Hauptmenü
            Fehler: Erzeugt Fehlermeldung: "Anmeldung nicht möglich - falsche Eingaben."
        Abmeldung: Benutzer kann sich jederzeit abmelden. Aktive Sitzung wird beendet

2. US01 Eigene Daten ansehen
        Der angemeldete Mieter sieht nur seine eigenen Daten. Das sind
                Vorname und Nachname
                E-Mail
                Telefon
                Strasse und Hausnummer
                PLZ und Ort 

3. Mietobjekt ansehen
        Der angemeldete Mieter sieht nur seine eigenen gemieteten Objekte
        Mit Auswahl eines Mietobjekts gelangt er zum Untermenü für Schritte (4-11)
        Mietobjekte werden aufgelistet angezeigt mit
                Typ (Wohnung oder Haus)
                (evtl. Name des Vermieters / der Verwaltung)
                Strasse und Hausnummer
                PLZ und Ort

4. US02 Mietvertrag ansehen
        Dem angemeldeten Benutzer wird der Mietvertrag des ausgewählten Mietobjekts in PDF Format angezeigt.
        Der Pfad der PDF wird aus der Tabelle "Mietvertraege" ausgelesen.
                Im Mietvertrag werden folgende Informationen angezeigt:
                        Erstellt am
                        Name des Verwalters
                        Vertragsbeginn 
                        Vertragsende
                        Kaltmiete
                        Nebenkostenvorauszahlung
                        Kaution
        
5. US03 Mietzahlungen ansehen (bezahlt, offen, überfällig)
        Dem angemeldeten Benutzer werden die Mietzahlungen des ausgewählten Mietobjekts angezeigt.
        Folgende Informationen werden angezeigt: 
                Zahlungsdatum
                Fälligkeitsdatum
                Betrag
                Status (bezahlt, offen oder überfällig)

6. US04 Nebenkostenabrechnung ansehen
        Dem angemeldeten Benutzer wird die aktuellste Nebenkostenabrechnung in PDF Format angezeigt.
        Der Pfad der PDF wird aus der Tabelle "Mietvertraege" ausgelesen.
                In der Nebenkostenabrechnung werden folgende Informationen angezeigt:
                        Erstellt am
                        Abrechnungsjahr
                        Abrechnungsdatum
                        Gesamtbetrag
                        
7. US05 Nebenkostenabrechnung als PDF herunterladen
        Die im externen Fenster (bspw. pdf-Reader) geöffnete pdf kann vom Benutzer heruntergeladen werden.
    
8. US06 Zählerstände übermitteln
        Zunächst muss der Zähler ausgewählt bzw. angelegt werden
                (zaehler_id und mietobjekt_id werden automatisch zugefügt)
                Zählerart (Strom, Gar oder Wasser)
                Zählernummer eingeben
        Der angemeldete Benutzer kann seine Zählerstände eingeben und übermitteln. 
                [Anzeige von Zählerart und Zählernummer]
                Ablesedatum
                Zählerstand

9. US07 Wartungs- oder Schadensmeldung erstellen
        Der angemeldete Benutzer kann für das im Hauptmenü ausgewählte Mietobjekt eine Meldung erstellt werden.
		Folgende Informationen müssen vom Benutzer ausgefüllt werden
		    Titel
		    Beschreibung
		    (nach Erstellung wird Status (offen, in_bearbeitung, erledigt, abgelehnt) auf offen gelegt)

10. US08 Nachrichten der Hausverwaltung lesen
        Dem angemeldeten Benutzer werden die Nachrichten der Hausverwaltung aufgelistet angezeigt. 
        Folgende Informationen werden angezeigt: 
            Erstellt am
            Titel
            Inhalt

11. US10 Alle Dokumente ansehen und herunterladen
        Dem angemeldeten Benutzer werden alle Dokumente angezeigt, die zum ausgewählten Mietobjekt gehören.
        Folgende Informationen werden angezeigt:
            Dateiname und Dateiformat
        Der Benutzer kann ein Dokument auswählen und herunterladen. 

Folgende Userstories und Funktionen werden nicht implementiert, zumindest nicht in den 5 Sprints. 

Das sind unsere 12 User Stories für den Vermieter:

1. US-09 Anmelden und abmelden
        Anmeldung: Eingabe des Nutzernamens und des verdeckten Passworts
            Erfolgreich: Benutzer gelangt zum Hauptmenü
            Fehler: Erzeugt Fehlermeldung: "Anmeldung nicht möglich - falsche Eingaben."
        Abmeldung: Benutzer kann sich jederzeit abmelden. Aktive Sitzung wird beendet

2. US01 Eigene Daten ansehen
        Der angemeldete Mieter sieht nur seine eigenen Daten. Das sind
            Vorname und Nachname
            E-Mail
            Telefon
            Strasse und Hausnummer
            PLZ und Ort 
3. Mietobjekte ansehen
	Mit Auswahl eines Mietobjekts gelangt der angemeldete Vermieter zum Untermenü für Schritte (4-11)
	Mietobjekte werden aufgelistet angezeigt mit
		Typ (Wohnung oder Haus)
		(evtl. Name des Vermieters / der Verwaltung)
		Strasse und Hausnummer
		PLZ und Ort

4. Mietvertrag ansehen
        Dem angemeldeten Benutzer wird der Mietvertrag des ausgewählten Mietobjekts in PDF Format angezeigt.
        Der Pfad der PDF wird aus der Tabelle "Mietvertraege" ausgelesen.
                Im Mietvertrag werden folgende Informationen angezeigt:
                        Erstellt am
                        Name des Verwalters
                        Vertragsbeginn 
                        Vertragsende
                        Kaltmiete
                        Nebenkostenvorauszahlung
                        Kaution

5. US03 Mietzahlungen ansehen (bezahlt, offen, überfällig)
    Dem angemeldeten Benutzer werden die Mietzahlungen des ausgewählten Mietobjekts angezeigt.
        Folgende Informationen werden angezeigt: 
                Zahlungsdatum
                Fälligkeitsdatum
                Betrag
                Status (bezahlt, offen oder überfällig)

6. US04 Nebenkostenabrechnung ansehen
    Dem angemeldeten Benutzer wird die Nebenkostenabrechnung in PDF Format angezeigt.
        Der Pfad der PDF wird aus der Tabelle "Mietvertraege" ausgelesen.
        In der Nebenkostenabrechnung werden folgende Informationen angezeigt:
                Erstellt am
                Abrechnungsjahr
                Abrechnungsdatum
                Gesamtbetrag

(7. V01 Nebenkostenabrechnung als PDF bereitstellen)

8. Zählerstände einsehen
        Der angemeldete Benutzer kann die Zählerstände der einzelnen Mieter einsehen. 
                [Anzeige von Zählerart und Zählernummer]
                Ablesedatum
                Zählerstand

9. Wartungs- oder Schadensmeldung einsehen
        Der angemeldete Benutzer kann für das im Hauptmenü ausgewählte Mietobjekt eine Meldung erstellt werden.
		Folgende Informationen müssen vom Benutzer ausgefüllt werden
		    Titel
		    Beschreibung
		    (nach Erstellung wird Status (offen, in_bearbeitung, erledigt, abgelehnt) auf offen gelegt)
10. Wartungs- oder Schadensmeldung bearbeiten
11. US08 Nachrichten der Hausverwaltung lesen
12. Alle Dokumente ansehen und herunterladen

Das sind unsere 4 User Stories für den Admin:

1. US-09 Anmelden und abmelden
    Anmeldung: Eingabe des Nutzernamens und des verdeckten Passworts
        Erfolgreich: Benutzer gelangt zum Hauptmenü
        Fehler: Erzeugt Fehlermeldung: "Anmeldung nicht möglich - falsche Eingaben."
    Abmeldung: Benutzer kann sich jederzeit abmelden. Aktive Sitzung wird beendet
2. Benutzer anlegen
3. Benutzer bearbeiten
4. Benutzer löschen 
        nur dann, wenn keine offenen Mietverträge und Rechnungen vorliegen
