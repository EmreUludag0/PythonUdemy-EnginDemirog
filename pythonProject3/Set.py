studentsSet = {"emre", "eren", "arda"}
studentsSet2 = set("mehmet", "veli", "ayşe") #bu şekilde de tanımlanabilir
print(studentsSet)

for student in studentsSet:
    print(student)

print("eren" in studentsSet)

if "eren" in studentsSet:
    print("listede var")

studentsSet.add("ali")
print(studentsSet)

studentsSet.update(["merve", "mert", "selin"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove(("selin")) #set'ten çıkarır
print(len(studentsSet))

studentsSet.discard(("selin")) #set'ten çıkartır ve bulamazsa arıza çıkartmaz
print(len(studentsSet))

x = studentsSet.clear() #random siler
print(len(studentsSet))
print(studentsSet)
