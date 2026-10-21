### Hauptmenü wird angezeigt ###

def hauptmenu():
    print("Wohnpilot")
    print("----------------------------------")
    print("Hallo, [benutzer.vorname]!")
    print("Was möchtest du tun?")
    print(" ") # LEERZEILE
    print("1 - Eigene Kontaktdaten ansehen")
    print("2 - Eigene Mietobjekte aufrufen")
    print("3 - Eigene Nachrichten")
    print("4 - Anwendung beenden (Logout?).")

def kontaktdaten():
    print("----------------------------------")
    print("Eigene Kontaktdaten")
    print("----------------------------------")
    print("Name: " + "benutzer.vorname" + " " + "benutzer.nachname")
    print("1 - Zurück zum Hauptmenü")
    print("2 - Programm beenden")

def mietobjekte():
    print("----------------------------------")
    print("Eigene Mietobjekte")
    print("----------------------------------")
    print("1 - Zurück zum Hauptmenü")
    print("2 - Programm beenden")

def nachrichten():
    print("----------------------------------")
    print("Eigene Nachrichten")
    print("----------------------------------")
    print("1 - Zurück zum Hauptmenü")
    print("2 - Programm beenden")       

while True:
    hauptmenu()
    print("----------------------------------")
    auswahl = input("Eingabe der gewünschten Ziffer (1, 2 oder 3), um fortzufahren: ")

    if auswahl == "1":
        print("Ausgewählt: 1 - Eigene Kontaktdaten ansehen")
        while True:
            kontaktdaten()
            print("----------------------------------")
            auswahl = input("Eingabe der gewünschten Ziffer (1 oder 2), um fortzufahren: ")

            if auswahl == "1":
                 print("Ausgewählt: 1 - Zurück zum Hauptmenü")
                 break

            elif auswahl == "2":
                print("Ausgewählt: 2 - Anwendung beenden")
                exit()

            else:
                print("----------------------------------")
                print("Bitte gib eine gültige Ziffer (1, oder 2) an.")

    elif auswahl == "2":
        print("Ausgewählt: 2 - Eigene Mietobjekte ansehen")
        while True:
            mietobjekte()
            print("----------------------------------")
            auswahl = input("Eingabe der gewünschten Ziffer (1 oder 2), um fortzufahren: ")
            
            if auswahl == "1":
                print("Ausgewählt: 1 - Zurück zum Hauptmenü")
                break
            
            elif auswahl == "2":
                print("Ausgewählt: 2 - Anwendung beenden")
                exit()
            
            else:
                print("----------------------------------")
                print("Bitte gib eine gültige Ziffer (1, oder 2) an.")

    elif auswahl == "3":
        print("Ausgewählt: 3 - Eigene Nachrichten")
        while True:
            nachrichten()
            print("----------------------------------")
            
            auswahl = input("Eingabe der gewünschten Ziffer (1 oder 2), um fortzufahren: ")
            
            if auswahl == "1":
                print("Ausgewählt: 1 - Zurück zum Hauptmenü")
                break
            
            elif auswahl == "2":
                print("Ausgewählt: 2 - Anwendung beenden")
                exit()
            
            else:
                print("----------------------------------")
                print("Bitte gib eine gültige Ziffer (1, oder 2) an.")           

    elif auswahl == "4": 
        print("Programm beendet.")
        break

    else:
        print("----------------------------------")
        print("Bitte gib eine gültige Ziffer (1, 2, oder 3) an.")

print("Schleife verlassen.")

