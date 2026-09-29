
| ID | Name | Voraussetzung | Testdaten | Schritte | Erwartetes Ergebnis | Ausgeführt am | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anmelden_01 |	Erfolgreich anmelden | Website erreichbar und geöffnet | Username und Passwort | 1. Eingabe des Usernamen <br> 2. Eingabe des Passworts <br> Teiltest: Eingabe des Passworts nicht in Klartext <br> 3. Bestätigen der Anmeldung (Enter oder Button) | User wird erfolgreich eingeloggt. | | |


anmelden_02	Fehler bei anmelden	Website erreichbar und geöffnet		"1. Eingabe eines falschen Usernamen
oder Eingabe eines falschen Passworts
3. Bestätigen der Anmeldung (Enter oder Button)"	"Es erscheint eine Fehlermeldung:
""Anmeldung nicht möglich - falsche Eingaben. """		
profil_01	User sieht Profilansicht	"1. Website erreichbar und geöffnet
2. User ist erfolgreich angemeldet"		"1. Öffnen der Profilansicht. 
2. Prüfe: Stimmen Daten des angemeldeten Users 
mit den angezeigten Kontaktdaten überein?"	"User sieht sein eigenes Profil 
sowie seine Kontaktdaten: Vorname, Nachname, Adresse, PLZ, evtl. Etage und Wohnungsnummer, Telefon, E-Mail"		
mietvertrag_01	User hat Zugriff auf Mietvertrag	"1. Website erreichbar und geöffnet
2. User ist erfolgreich angemeldet
3. Vermieter hat Mietvertrag bereitgestellt"	Datei: Mietvertrag	"1. Öffnen der Dokumentenansicht. 
2. Auswahl des Mietvertrags."	Der Mietvertrag des Users wird geöffnet und korrekt angezeigt. 		
mietzahlungen_01	User hat Zugriff auf Mietzahlungen	"1. Website erreichbar und geöffnet
2. User ist erfolgreich angemeldet
3. Mietzahlungen wurden durchgeführt"		"1. Öffnen der Ansicht für Mietzahlungen.
2. Auswahl eines bestimmten Monats."	"Der User sieht die ausgewählte Mietzahlung und 
diese wird korrekt angezeigt. "		
betraege_01	Prüfung offener Beträge	"1. Website erreichbar und geöffnet
2. User ist erfolgreich angemeldet
3. Offener Betrag ist vorhanden"		Öffnen der Rechnungsansicht	Offene Beträge des Users werden angezeigt. 		
betraege_02	Prüfung geleisteter Beträge	"1. Website erreichbar und geöffnet
2. User ist erfolgreich angemeldet
3. Geleisteter Betrag ist vorhanden"		Öffnen der Rechnungsansicht	Geleistete Beträge des Users werden angezeigt. 		
download_01	User kann Dokumente herunterladen	"1. Website erreichbar und geöffnet
2. User ist erfolgreich angemeldet
3. Dokumente wurden bereitgestellt"	"Dokumente: Nebenkostenabrechnung, 
Mietvertrag, Rechnungen etc. "				
