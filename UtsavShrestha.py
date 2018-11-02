p = float(input("Enter the princial amount:"))
r = float (input("Enter the rate:"))
t = float(input("Enter the time:"))
n = float (input("Enter the unmber of times the interest is compounded per year:"))

A = p*(1+(r/n))**(n*t)
I = A - p 

print("The compound interest is:" , I)


