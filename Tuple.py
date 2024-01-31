
tupleListe = (2, 4, 6, "ankara", (2, 3, 4), [])
liste = [2, 4, 6, "ankara", (2, 3, 4), ()]

liste[0] = 6
#tupleListe[0] = 6 #tuple ile liste farkı = tuple değişmez

tupleDeger = ("Engin",)
print(type(tupleDeger))

print(tupleListe[-2]) #sağdan ikinci komutu verir
print(liste[-2]) #sağdan ikinci komutu verir

print(tupleListe[1:2])
print(liste[1:2])

print(tupleListe)
print(liste)

print(len(tupleListe))
print(len(liste))
