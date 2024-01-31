ogrenciler = ["Emre", "Eren", "Arda", "Kazim", "Ozlem"]

fileToAppend = open("ogranciler","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")

fileToAppend.close()

