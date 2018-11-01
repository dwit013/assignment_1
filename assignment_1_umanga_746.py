#Umanga Pathak
#Roll: 746
#Python program to calculate compound interest

prinpical = int(input("Enter principal: "))
time = int(input("Enter number of years: "))
rate = float(input("Enter rate: "))
num = int(input("Enter number of times the interest is calculatedd per year: "))

temp = 1 + rate/num

pow = num*time

amount = temp**pow

amount = amount*prinpical

print ("Amount = " + str(amount))
