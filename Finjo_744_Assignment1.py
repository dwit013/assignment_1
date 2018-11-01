"""

    Name: Tsering Finjo Sherpa
    Roll: 744

    Python Assignment 1

"""
#Calculating the Compound Interest

principle = int(input("Enter the principle: ")) #Principle amount (initial investment)
rate = float(input("\nEnter the rate: ")) #annual nominal interest rate
time = int(input("\nEnter the time: ")) #number of years
n = int(input("\nEnter the number of periods: ")) #number of times interest is compounded per year

amount = principle*((1+(rate/n)**(n*time)))

print("Your Amount after",time,"years time is Rs.",amount)
