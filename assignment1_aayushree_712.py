Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> principle=input("enter principal amount")
enter principal amount1234
>>> rate=input("enter the rate")
enter the rate5
>>> n=input("enter no. of times the interest is compunded per year")
enter no. of times the interest is compunded per year12
>>> time=input("no. of years")
no. of years5
>>> a=principle*(1+rate/n)**(n*time)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=principle*(1+rate/n)**(n*time)
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> type(rate)
<class 'str'>
>>> principle=float(input("enter the principle  amount"))
enter the principle  amount5000
\
>>> r=float(input("enter the rate"))
enter the rate1.4
>>> n=int(input("enter the no of times interest is compunded"))
enter the no of times interest is compunded3
>>> t=float(input("enter the time"))
enter the time3
>>> a=principle*(1+r/n)**(n*t)
>>> print(a)
157019.21442602845
>>> 
