#Variablen
ausw1 = 0
ausw2 = 0

#Auswählen
while ausw1 != 1 and ausw1 != 2 and ausw1 != 3 and ausw1 != 4 and ausw1 != 5:
    ausw1 = int(input("1: m <->km \nk2: s <-> h \n3: m/s <-> km/h \n4: m/s <-> m <-> s\n5: km/h <-> km <-> h\nNummer eingeben:" ))

#Zahlen einfügen + Rechnen + Ergebnisse
if ausw1 == 1:
    while ausw2 != 1 and ausw2 != 2:
        ausw2 = int(input("1: m -> km \n2: km -> m \nNummer eingeben:"))
    if ausw2 == 1:
        zahl1 = float(input("Meter eingeben:"))
        ergebniss = zahl1 / 1000
        print(f"{zahl1}m = {ergebniss}km")
    if ausw2 == 2:
        zahl1 = float(input("Kilometer eingeben:"))
        ergebniss = zahl1 * 1000
        print(f"{zahl1}km = {ergebniss}m")
    
elif ausw1 == 2:
    while ausw2 != 1 and ausw2 != 2:
        ausw2 = int(input("1: s -> h \n2: h -> s \nNummer eingeben:"))
    if ausw2 == 1:
        zahl1 = float(input("Sekunden eingeben:"))
        ergebniss = zahl1 / 3600
        print(f"{zahl1}s = {ergebniss}h")
    if ausw2 == 2:
        zahl1 = float(input("Stunden eingeben:"))
        ergebniss = zahl1 * 3600
        print(f"{zahl1}h = {ergebniss}s")
        
elif ausw1 == 3:
    while ausw2 != 1 and ausw2 != 2:
        ausw2 = int(input("1: m/s -> km/h \n2: km/h -> m/s \nNummer eingeben:"))
    if ausw2 == 1:
        zahl1 = float(input("Meter pro Sekunde eingeben:"))
        ergebniss = zahl1 * 3.6
        print(f"{zahl1}m/s = {ergebniss}km/h")
    if ausw2 == 2:
        zahl1 = float(input("Kilometer pro Stunde eingeben:"))
        ergebniss = zahl1 / 3.6
        print(f"{zahl1}km/h = {ergebniss}m/s")
        
elif ausw1 == 4:
    while ausw2 != 1 and ausw2 != 2 and ausw2 != 3:
        ausw2 = int(input("1: m * s -> m/s \n2: m/s / s -> m \n3: m/s / m -> s \nNummer eingeben:"))
    if ausw2 == 1:
        zahl1 = float(input("Meter eingeben:"))
        zahl2 = float(input("Sekunde eingeben:"))
        ergebniss = zahl1 * zahl2
        print(f"{zahl1}m * {zahl2}s = {ergebniss}m/s")
    if ausw2 == 2:
        zahl1 = float(input("Meter pro Sekunde eingeben:"))
        zahl2 = float(input("Sekunde eingeben:"))
        ergebniss = zahl1 / zahl2
        print(f"{zahl1}m/s / {zahl2}s = {ergebniss}m")
    if ausw2 == 3:
        zahl1 = float(input("Meter pro Sekunde eingeben:"))
        zahl2 = float(input("Meter eingeben:"))
        ergebniss = zahl1 / zahl2
        print(f"{zahl1}m/s / {zahl2}m = {ergebniss}s")
        
elif ausw1 == 5:
    while ausw2 != 1 and ausw2 != 2 and ausw2 != 3:
        ausw2 = int(input("1: km * h -> km/h \n2: km/h / h -> km \n3: km/h / km -> h \nNummer eingeben:"))
    if ausw2 == 1:
        zahl1 = float(input("Kilometer eingeben:"))
        zahl2 = float(input("Stunde eingeben:"))
        ergebniss = zahl1 * zahl2
        print(f"{zahl1}km * {zahl2}h = {ergebniss}km/h")
    if ausw2 == 2:
        zahl1 = float(input("Kilometer pro Stunde eingeben:"))
        zahl2 = float(input("Stunde eingeben:"))
        ergebniss = zahl1 / zahl2
        print(f"{zahl1}km/h / {zahl2}h = {ergebniss}km")
    if ausw2 == 3:
        zahl1 = float(input("Kilometer pro Stunde eingeben:"))
        zahl2 = float(input("Kilometer eingeben:"))
        ergebniss = zahl1 / zahl2
        print(f"{zahl1}km/h / {zahl2}km = {ergebniss}h")

print("Ende")
