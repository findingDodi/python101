import random
import sys


print(sys.argv)
print(len(sys.argv))

# copy() klappt nur bei python3
appointment_list = sys.argv.copy()
appointment_list.pop(0)


#Aufgabe: beliebige Anzahl an Terminen die wir reintun, brauchen einen Termin als Ausgabe (der wird gestrichen)

#appointment_list = ["Coding101 JS", "Coding101 PHP", "Coding101 C++"]

#random_appointment = random.randrange(len(appointment_list))
#print(appointment_list[random_appointment])
#print(appointment_list)

appointment = random.choice(appointment_list)
print(appointment)
print(appointment_list)
print(sys.argv)


