str=input("Enter the string:")
rev_str=""
for char in str:
    rev_str=char+rev_str
print("Reverse of the Given",str,"is:",rev_str)
if(str==rev_str):
    print(str,"Given string is pallindrome")
else:
    print(str,"Given string is not a pallindrome")   
output:1
Enter the string:madam
Reverse of the Given madam is: madam
madam Given string is pallindrome
output:2
Enter the string:oiuygfds
Reverse of the Given oiuygfds is: sdfgyuio
oiuygfds Given string is not a pallindrome
