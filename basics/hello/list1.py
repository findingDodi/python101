#tuple müssen überschrieben werden
unchange = ("Hamster", "Dog", "Cat")
print(unchange)
print(unchange[1])

#list änderbare Liste
mylist = ["Firefox", "Safari", "Chrome", "Chrome"]
print(mylist)
print(mylist[1])
mylist.append("Opera")
print(mylist)
mylist[1] = "Internet Explorer"
print(mylist)
mylist.remove("Chrome")
print(mylist)
print(mylist.pop(1))
print(mylist)

#dictionary key value store (Hashmap)
mydict = {"Breakfast": "Toast", "Lunch": "Sandwich", "Dinner": "Pizza"}
print(mydict)
print(mydict["Lunch"])
mydict["Lunch"] = "Bagel"
print(mydict)
mydict["Snack"] = "Chips"
print(mydict)
del mydict["Snack"]
print(mydict)
mydict.pop("Lunch")
print(mydict)
if "Breakfast" in mydict:
    print(mydict["Breakfast"])
    
print("*" * 10)

print("Länge Liste:", len(mylist))

print("*" * 10)

for browser in mylist:
    print(browser)
