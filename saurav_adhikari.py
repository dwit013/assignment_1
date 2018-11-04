# name saurav adhikari
# roll no 734
# class of 2021
# section B

p=int(input("Enter the principal amount(Rs):"))
n=int(input("Enter the no of times interest is compounded per year : "))
t=int(input("enter the no. of years : "))
r=float(input("Enter the annual interest(%) : "))

finalvalue= p*(1+(r/n))**(n*t)

print("The final amount after",t,"years is Rs.",finalvalue)
