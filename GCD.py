import math
def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
print("GCD of",a,"and",b,"is",end=" ")
print(hcf(a,b))            
# output:
# Enter A value:12
# Enter B value:18
# GCD of 12 and 18 is 6
