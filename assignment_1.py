principal = int(input("Enter principal:"))
time = int(input("Enter time:"))
rate = int(input("Enter rate:"))
n = int(input("enter number of time the interest is compounded per year:"))
nt = n*time

amount = principal*((1+(rate/n))**(nt))
print(amount)