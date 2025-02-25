start=int(input("Enter the starting range:"))
end=int(input("Enter the ending range:"))
print("Prime numbers from",start,"to",end)
for num in range(start,end+1):
    if (num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)   
# output:
# Enter the starting range:1
# Enter the ending range:10
# Prime numbers from 1 to 10
# 2
# 3
# 5
# 7            

