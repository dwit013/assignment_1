# Python Program to Calculate Compound interest
# where P = Principal amount , t = no of years , r = Rate of Interest and n = no. of times interest is compounded per year 

P = 3200
r = 3.2
t = 2
n = 3

A = P*(1+(r/n))**(n*t)

print ("The Total Amount is " + str(A))

