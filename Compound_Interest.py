# Program to calculate compount interest

principal_amount = int(input("Enter principal amount :"))
rate = int(input("Enter the nomial interest rate(as a decimal) :"))
number = int(input("Number of times the interest is compounded per year :"))
time = int(input("Number of years :"))

amount = principal_amount*pow((1+(rate/number)),(number*time))
print("Total amount is :")
print(amount)
