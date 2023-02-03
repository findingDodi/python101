zahl1 = 3
name = "Dorina"

# int und string können nicht miteinander verbunden/verknüpft werden
# Python ist stark typisiert
# ausgabe = name + zahl1
ausgabe = name + str(zahl1)

print(ausgabe)
print(name, zahl1)

zahleingabe = input("Enter Number ")
ergebnis = int(zahleingabe) + zahl1
print(ergebnis)
