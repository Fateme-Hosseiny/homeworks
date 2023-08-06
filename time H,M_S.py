H= int(input("enter hour:"))

M=int(input("enter minute:"))

S= int(input("enter Secound:"))

print (f"{H}:{M}:{S}")

a=H*3600

b=M*60

c=a+b+S

print("Time=", c ,"second")