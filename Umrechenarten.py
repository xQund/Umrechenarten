#Nach dem Umrechnen Wiederholen
while ausw3 != 2:
    
#Variablen
    ausw1 = 0
    ausw2 = 0
    ausw3 = 0
    num1 = 0
    
#Auswahl der Umrechenart    
    while ausw1 != 1 and ausw1 != 2 and ausw1 != 3 and ausw1 != 4 and ausw1 != 5:
        print("___________________")
        if num1 != 0:
            print("Ungülltige Nummer, bitte erneut eingeben!")
        ausw1 = int(input("1: m <->km \n2: cm <-> Inch \n3: s <-> h \n4: sm <-> km \n5: m/s <-> km/h \nNummer eingeben:" ))
        num1 = num1 + 1

#Strings und feste Integer benennen
    if ausw1 == 1:
        formel1 = "m"
        formel2 = "km"
        zahl2 = 1000
    elif ausw1 == 2:
        formel1 = "cm"
        formel2 = "Inch"
        zahl2 = 2.54
    elif ausw1 == 3:
        formel1 = "s"
        formel2 = "h"
        zahl2 = 3600
    elif ausw1 == 4:
        formel1 = "sm"
        formel2 = "km"
        zahl2 = 1.852
    elif ausw1 == 5:
        formel1 = "m/s"
        formel2 = "km/h"
        zahl2 = 3.6
   
#Auswahl der Einheit
    num1 = 0
    while ausw2 != 1 and ausw2 != 2:
        print("___________________")
        if num1 != 0:
            print("Ungülltige Nummer, bitte erneut eingeben!")
        ausw2 = int(input(f"1: {formel1} -> {formel2} \n2: {formel2} -> {formel1} \nNummer eingeben:"))
        num1 = num1 + 1
    
#Eingabe der Zahl + Umrechnen
    if ausw2 == 1:
        zahl1 = float(input(f"___________________\nBitte {formel1} eingeben:"))
        ergebniss = zahl1 / zahl2
        print(f"{zahl1}{formel1} = {ergebniss}{formel2}")
    if ausw2 == 2:
        zahl1 = float(input(f"___________________\nBitte {formel2} eingeben:"))
        ergebniss = zahl1 * zahl2
        print(f"{zahl1}{formel2} = {ergebniss}{formel1}")

#Auswahl zum Verlassen
    num1 = 0
    while ausw3 != 1 and ausw3 != 2:
        print("___________________")
        if num1 != 0:
            print("Ungülltige Nummer, bitte erneut eingeben!")
        ausw3 = int(input("1: Nochmal!!:) \n2: Verlassen \nNummer eingeben:"))
        num1 = num1 + 1

#Ende
print("___________________\nEnde")