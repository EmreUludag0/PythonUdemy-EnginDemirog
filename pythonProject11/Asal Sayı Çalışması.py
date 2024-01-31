#%% asal sayi
sayi = int(input("sayi giriniz: "))

asalMi = True
for x in range(2, sayi):
    if (sayi % x) == 0:
        asalMi = False
        break
if asalMi == True:
    print("asal")
else:
    print("Asal Degil")




