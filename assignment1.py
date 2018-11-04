#name=Bipul Shrestha
#roll=714
#batch:2021 'B'

principle = float(input("Enter the princial amount:"))
rate = float (input("Enter the rate:"))
time = float(input("Enter the time:"))
n = int (input("Enter the no of times the interest is compounded per year:"))

Amount = principle*(1+(rate/n))**(n*time)
print("The amount calculated is:",Amount)
