#%% FOR DONGUSU
sehirler = ["ankara", "istanbul", "izmir"]

for sehir in sehirler:
    if sehir != "ankara":
        print(sehir + " için kod = "+ sehir[0:3])
        print("************")

for a in sehirler:
    print(a)

#%% WHILE

sayac = 1
sonuc = 0
while sayac <=10:
    sonuc = sonuc + sayac
    sayac = sayac + 1

print(sonuc)

#%% REAK VE CONTINUE
sehirler = ["ankara", "istanbul", "izmir"]
for sehir in sehirler:
    if sehir == "istanbul":
        continue #sadece o anki dönümünü iptal eder.
    print(sehir)

#%% RANGE FONKSIYONU
for x in range(1,10,2):
    print(x + 1)








