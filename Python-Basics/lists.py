#Data structures
L=[1,2,3,4,"hello",3]
print(L)
print("The type of L is:",type(L))
print(L[1:3])
print(L[::-1])
L=L  + ["how","are",6,"you"]
print(L)
L.append("meow")
del L[1]
print(L)
#copy function is used to copy a list
L2 =L
print(L2)
L2 =L.copy()
L2.append("MEOW2")
print(L2)
print(L)
L3 =L[1:5]
print(L3)
L3[0]="MEOW3"
print(L3)
print(L)
#other functions on list
print(len(L))
