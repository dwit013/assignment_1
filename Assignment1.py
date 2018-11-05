p=int(input("Enter principle amount"))
t=int(input("Enter number of years"))
r=int(input("Enter annual nomial interest rate"))
n=int(input("Enter number of times the interest is compounded per year"))


i= p*((1+(r/n)) ** (n*t))


print(i)
