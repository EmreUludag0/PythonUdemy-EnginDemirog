#set Union
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

#set Intersection
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

#set Difference ve Symmetric
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))










