# Write a simple program to calculate the compound interest

p=float(input("Enter principle amount:"))
t=float(input("Enter time duration in years:"))
r=float(input("Enter rate of interest:"))
n=int(input("Enter number of times the interest is compounded per year:"))
amount = p * (1 + r/n)**(n*t)
compound_interest=amount-p;
print("Compound interest is", compound_interest)
