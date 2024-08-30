#Kommentare immer über oder Neben dem jeweiligen Schritt

#Variablen bestimmen
formelzeichen1 = "m", "cm", "s", "sm", "km/h", "km", "Inch", "h", "km", "m/s"
umrechenfaktoren1 = 1000, 2.54, 3600, 1.852, 3.6
#________________________________________________________________________________________________________________
#Auswahl der Umrechenart
def auswahl1(temp_ausw1 = 0):
    num1 = False
    #While Schleife wiederholt die Eingabe, bis eine Zahl von 1-6 eingegeben wurde
    while temp_ausw1 !="1" and temp_ausw1 !="2" and temp_ausw1 !="3" and temp_ausw1 !="4" and temp_ausw1 !="5" and temp_ausw1 !="6":
        print("___________________")
        #Abfrage ob diese Schleife schon einmal durchlaufen worden ist
        if num1 == True:      
            print("Ungülltige Eingabe, bitte Nummer von 1-5 eingeben!")
        else:
            num1 = True
        #Eingabe zur Auswahl der Umrechenarten
        temp_ausw1 = input("1: m <-> km \
                          \n2: cm <-> Inch \
                          \n3: s <-> h \
                          \n4: sm <-> km \
                          \n5: m/s <-> km/h \
                          \n6: Verlassen \
                          \nNummer eingeben:")
        
    #Zurückgabe der eingegebenen Nummer (1-6)
    return temp_ausw1          
#________________________________________________________________________________________________________________
#Auswahl der Einheit
def auswahl2(temp_ausw2 = 0):
    num1 = False
    #While Schleife wiederholt die Eingabe, bis eine Zahl von 1-3 eingegeben wurde
    while temp_ausw2 !="1" and temp_ausw2 !="2" and temp_ausw2 !="3":
        print("___________________")
        #Abfrage ob diese Schleife schon einmal durchlaufen worden ist
        if num1 == True:       
            print("Ungülltige Eingabe, bitte Nummer von 1-2 eingeben!")
        else:
            num1 = True
        
        temp_ausw2 = input(f"1: {formel1} -> {formel2} \
                           \n2: {formel2} -> {formel1} \
                           \n3: Zurück \
                           \nNummer eingeben:")
        
    #Zurückgabe der eingegebenen Nummer (1-3)
    return temp_ausw2         
#________________________________________________________________________________________________________________    
#Eingabe und Umrechnen der gewünschten Größe
def rechnen(zahl1 = 0):
    num1 = False
    #While Schleife wiederholt die Eingabe, bis eine Zahl eingegeben wurde
    while zahl1 == 0:
        print("___________________")
        #Abfrage ob diese Schleife schon einmal durchlaufen worden ist
        if num1 == True:       
            print("Ungülltige Eingabe, bitte Nummer nur Zahlen und maximal einen . eingeben!")
        #Eingabe der Umzurechnenden Zahl
        eing1 = str(input(f"Bitte {formel1} eingeben:"))
        #Eingabe Überprufen
        try:
            zahl1 = float(eing1)
        except:
            num1 = True
            
    #Rechnen je nach Umstellrichtung
    if ausw2 == "1":                                     
        ergebniss = zahl1 / zahl2
    elif ausw2 == "2":
        ergebniss = zahl1 * zahl2
    #Ausgabe des Umgerechneten Ergebnisses        
    print(f"{zahl1}{formel1} = {ergebniss}{formel2}")
    #Pausieren des Programmes um das Ergebnis zu Presentieren
    input("Drücke Enter um Fortzufahren")
#________________________________________________________________________________________________________________    
#Ausführung des Programms als Schleife
while True:
    #"auswahl1" Aufrufen und in ausw2 als Integer schreiben, zum Rechnen
    ausw1 = int(auswahl1())                   
    #Schleife Beenden, wenn die Nummer 6 "Verlassen" ausgewählt wurde
    if ausw1 == 6:                            
        print("\nProgramm Beendet")
        break
   
    #Formelzeichen als String-Variable und Umrechenfaktor als Integer-Variable bestimmen
    formel1 = formelzeichen1[ausw1 - 1]       #Erstes Formelzeichen
    formel2 = formelzeichen1[ausw1 + 4]       #Zweites Formelzeichen
    zahl2 = umrechenfaktoren1[ausw1 - 1]      #Umrechenfaktor
    
    #"auswahl2" Aufrufen und in ausw2 schreiben   
    ausw2 = auswahl2()
    #Drehen der Formelzeichen
    if ausw2 == "2":                          
        formel1, formel2 = formel2, formel1
    #Schleife von vorne Beginnen, wenn die Nummer 3 "Zurück" ausgewählt wurde
    elif ausw2 == "3":                        
        continue
    
    #"rechnen" Aufrufen
    rechnen()