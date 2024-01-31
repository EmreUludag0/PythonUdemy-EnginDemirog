def topla(sayi1, sayi2):
    return sayi1 + sayi2

def cıkar(sayi1, sayi2):
    return sayi1 - sayi2

def carp(sayi1, sayi2):
    return sayi1 * sayi2

def bol(sayi1, sayi2):
    return sayi1 / sayi2


print("operasyon?")
print("1: topla, 2: çıkar, 3: çarp, 4:böl")

secenek = input("operasyon seciniz= ")
girilecek1 = int(input("birinci sayi= "))
girilecek2 = int(input("ikinci sayi= "))

if secenek == '1':
    print("toplam: " + str(topla(girilecek1, girilecek2)))
elif secenek == '2':
    print("çıkarma: " + str(cıkar(girilecek1, girilecek2)))
elif secenek == '3':
    print("çarpma: " + str(carp(girilecek1, girilecek2)))
elif secenek == '4':
    print("bölme: " + str(bol(girilecek1, girilecek2)))
else:
    print("geçersiz seçenek")






