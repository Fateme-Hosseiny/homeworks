import math
r= int(input("Enter students range:"))
a = []

for i in range(r):
    s= float(input("Enter score student:"))
    
    a.append(s)
    
avarage= (sum(a))/r

print("max.score:", max (a))

print("min.scoer:",min(a))

print("avarage class:",avarage)

    
    