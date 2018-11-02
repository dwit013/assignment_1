p = float(input("Enter the Principle amount : "))
r = float (input("Enter the Rate of Interest : "))
t = float(input("Enter the Time Duration : "))
n = float (input("Enter the nunmber of times the interest is compounded per year : "))

A= p*(1+(r/n))**(n*t)
I = A - p 

print("The Compound Interest is : " , I)