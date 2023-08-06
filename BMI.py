import math
w=float(input("enter weight kg:"))
H=float(input("enter height m:"))
BMI=w/(H*H)
print("BMI:", BMI)
if BMI<18.5:
 print("Underweight")
elif 18.5<= BMI <= 24.9 : 
 print("Normal")
elif 25<=BMI <=29.9:
 print("over weight")
elif 30<=BMI<= 34.9:
  print("Obese")
elif BMI>35:
  print("extermely obese")