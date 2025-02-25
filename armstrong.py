def armstrong(n):
    return n==sum(int(digit)** len(str(n)) for digit in str(n))
num=int(input("Enter a number:"))
print(num,"is" if armstrong(num) else "is not","an armstrong number.")