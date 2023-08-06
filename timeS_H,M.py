import math

S=int(input("Enter second:"))

H=S//3600

M=(S % 3600)//60

SE=(S % 3600) % 60

print(f"{H}:{M}:{SE}")
        