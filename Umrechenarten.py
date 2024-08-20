# Einheiten
einh1 = "km"
einh2 = "m"
einh3 = "h"
einh4 = "s"
einh5 = "m/s"
einh6 = "km/h"

# Auswählen
ausw1 = str(input("m -->km: km \nkm --> m: m \ns --> h: h \nh --> s: s \nm/s \nkm/h \nEinheit eingeben:" ))

#Zahlen eingeben
if ausw1 == einh1 or ausw1 == einh2 or ausw1 == einh3 or ausw1 == einh4:
	zahl1 = float(input(f"Zahl zu {ausw1} Umrechnen:"))
elif ausw1 == einh5:
	zahl1 = float(input("Meter eingeben:"))
	zahl2 = float(input("Sekunde eingeben:")) 
elif ausw1 == einh6:
	zahl1 = float(input("Kilometer eingeben:"))
	zahl2 = float(input("Stunde eingeben:")) 
    
#Rechnen + Ergebnisse
if ausw1 == einh1:
	ergebniss = zahl1 / 1000
	print(zahl1, "m =", ergebniss, einh1)
elif ausw1 == einh2:
	ergebniss = zahl1 * 1000
	print(zahl1, "km =", ergebniss, einh2)
elif ausw1 == einh3:
	ergebniss = zahl1 / 3600
	print(zahl1, "s =", ergebniss, einh3)
elif ausw1 == einh4:
	ergebniss = zahl1 * 3600
	print(zahl1, "h =", ergebniss, einh4)
elif ausw1 == einh5:
	ergebniss = zahl1 / zahl2
	print("Es sind:", ergebniss, einh5)
elif ausw1 == einh6:
	ergebniss = zahl1 / zahl2
	print("Es sind:", ergebniss, einh6)