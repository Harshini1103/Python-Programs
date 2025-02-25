num=int(input("Enter the number:"))
n1,n2=0,1
sum=0
if num<0:
    print("PLs enter the number Greater than 0")
else:
     for i in range(0,num):
        print(sum,end="")
        n1=n2
        n2=sum
        sum=n1+n2  
# output:
# Enter the number:6
# 011235          