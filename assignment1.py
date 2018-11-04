#name=Sahej Maharjan
#roll=729
#batch:2021 'B'

p = float(input("Enter princial amount:"))
r = float (input("Enter rate:"))
t = float(input("Enter time:"))
n = int (input("Enter no of times the interest is compounded per year:"))
a = p*(1+(r/n))**(n*t)
print("The amount is:",a)
