principal = int (input(" Enter the principal amount(initial investment) : "))
rate = float(input(" Enter the value of annual nominal interest rate(as a decimal): "))
num = int(input(" Enter the number of times the interest is compounded per year : "))
time =int(input(" Enter the number of years : "))

value = (1 + rate / num)

amount = principal * (value)**num*time

print("Amount is: ",str(amount))

