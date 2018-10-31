Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> p = int(input("Enter principal amount:"))
Enter principal amount:5000
>>> r = float(input("Enter annual nominal interest rate:"))
Enter annual nominal interest rate:1.5
>>> n = int(input("Enter number of times the interest is compounded per year:"))
Enter number of times the interest is compounded per year:2
>>> t = int(input("Enter the numbr of years:"))
Enter the numbr of years:3
>>> a = p*(1+(r/n))**(n*t)
>>> print("The calculated compound interest is:",a)
The calculated compound interest is: 143614.501953125
>>> 
