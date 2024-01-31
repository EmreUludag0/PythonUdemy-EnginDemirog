f = open("musteriler.txt")
#print(f.read())
print("*****************")
print(f.readline())
f.close()
#r Read, a Append, w Write, x Create

fileToAppend = open("ogrenciler.txt", "")
fileToAppend.write("\n")
fileToAppend.write("Eren")
fileToAppend.close()

import os

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("dosya yok")
os.rmdir("empty")






