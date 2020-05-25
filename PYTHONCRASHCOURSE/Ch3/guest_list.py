guests = ["bob", "bobby", "bobette"]

print("yo wassup " + guests[0])
print("Bob can't make it :(")

guests.remove("bob")
guests.append("joe")

print("YO welcome " + guests[2])

name = guests.pop()
print("yo im sorry " + name)

del guests[1]
del guests[0]

print(guests)