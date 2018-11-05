c=str(input("Enter 'y' to continue......."))

while(c == 'y'):
    p= int(input("Enter the initial investment:"))
    r= int(input("Enter annual nominal interest rate:"))
    n = int(input("Enter number of times the interst is compounded per year:"))
    t = int(input("Enter number of years:"))

    a = p*(1+(r/n))**(n*t)

    i= (a-p)

    print("The required compounded interest is")
    print(i)

    print("Do you want to continue???")
    c=str(input("Enter 'y' to continue......."))
                


