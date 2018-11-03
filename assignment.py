Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> p=float(input("Enter principal amount: "))
Enter principal amount: 100
>>> r=float(input("Enter interest rate: "))
Enter interest rate: 5
>>> n=int(input("Enter number of times interest compounded per year: "))
Enter number of times interest compounded per year: 1
>>> t=int(input("Enter number of years: "))
Enter number of years: 1
>>> print("compound interest is: ",p*math.pow(1+r/n,n*t))
compound interest is:  600.0
>>> 
