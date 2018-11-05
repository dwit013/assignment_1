Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> principle=float("Enter Principle")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    principle=float("Enter Principle")
ValueError: could not convert string to float: 'Enter Principle'
>>> principle=float(input("Enter Principle"))
Enter Principle1000
>>> rate=float(input("Enter Rate of Intrest"))
Enter Rate of Intrest4
>>> n=float(input("Enter n"))
Enter n12
>>> time=float(input("Enter time"))
Enter time5
>>> A=principle(1+rate/n)**(n*t)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    A=principle(1+rate/n)**(n*t)
TypeError: 'float' object is not callable
>>> A=principle*(1+rate/n)**(n*t)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    A=principle*(1+rate/n)**(n*t)
NameError: name 't' is not defined
>>> A=principle*(1+rate/n)**(n*time)
>>> print(A)
31356255640.743805
>>> 
