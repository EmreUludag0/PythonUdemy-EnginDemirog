ogrenciler = ["emre", "eren", "arda"]

ogrenciler.append("ahmet") #eleman ekleme
#ogrenciler[4] = "veli"
print(ogrenciler[3])
ogrenciler.remove("arda") #eleman silme
print(ogrenciler)

#list constructor
sehirler = list(("Ankara", "istanbul", "Ankara"))
print(sehirler)
print(len(sehirler))

#Diğer fonksiyonlar
#print(sehirler.clear())
print("ankara sayisi = "+ str(sehirler.count("Ankara")))
print("ankara indexi = " + str(sehirler.index("Ankara")))

sehirler.pop(1)
sehirler.insert(0, "İstanbul")
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0] = "İzmir"

print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3) #birleştirme
sehirler.sort() #a'dan z'ye sıralar
sehirler.reverse() #tersten sıralar
print(sehirler)


