p= int(input("Enter starting principle please. "))

n = float(input("Enter Compound intrest rate."))

r = float(input("Enter annual interest amount."))

t = f(input("Enter the amount of years. "))

final = P * (((1 + (r/n)) ** (n*t)))

print ("The final amount after", t, "years is", final)

