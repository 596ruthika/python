def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
try:
    a=int(input("Enter the number: "))
    if(a<=0):
        print("Invalid input")
    else:
        print(a,"Factorial: ",fact(a))
        c=0
        for i in range(1,a+1):
            if(a%i==0):
                c+=1
        print("No of factors of",a,"is",c)
except ValueError:
    print("Invalid input")
