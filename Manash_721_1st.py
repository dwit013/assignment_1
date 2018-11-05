"""
Name: Manash singh
Roll no: 721
"""
prin=int(input("Enter principle amount"))
time=int(input("Enter number of year"))
rate=int(input("Enter annual nominal interest rate"))
n= int(input("Enter number of times the interest is compounded per year"))


compundI= prin*((1+(rate/n)) ** (n*time))


print("Required compound interest is: ",compundI)

