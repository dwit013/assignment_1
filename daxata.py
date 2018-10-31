Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> P = 5500 #pricipal amount (initial investment)
>>> r = 6.2 #annual nominal interest rate (as a decimal)
>>> n = 3 #number of times the interest is compounded per year
>>> t = 5 #number of years
>>> ci = P*((1+(r/n))**(n*t))
>>> print (" The compound interest, A = ", ci) 
 The compound interest, A =  109739070884.36275
>>> 
