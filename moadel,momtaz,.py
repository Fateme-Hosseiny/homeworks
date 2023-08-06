import math
name=input("enter your name:")
family=input("enter family:")
A=float(input("enter first score:"))
B=float(input("enter second score:"))
C=float(input("enter third score:"))
a=(A+B+C)/3
print("average:",a)
if a>=17:
 print("privileged!")  
elif 12<= a <= 17:
 print("Normal")
elif a<12 : 
 print("conditional")