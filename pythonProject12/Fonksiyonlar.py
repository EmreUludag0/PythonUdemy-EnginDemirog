#%%
def selamVer(isim = "ziyaretçi"):
    print("Merhaba " + isim)

selamVer("Emre")
selamVer()

def selamVer2(isim = "ziyaretçi", soyisim = " arkadas"):
    print("Merhaba " + isim + " " + soyisim)
selamVer2()
selamVer2("Emre", "uludag")

def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2, 3)
print(alan)

dikUcgenAlaniHesapla2 = lambda a,b: a*b/2
print(dikUcgenAlaniHesapla2(2,4))



