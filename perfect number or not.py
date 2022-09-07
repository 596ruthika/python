n=int(input("enter any number:"))
sum1 = 0
for i in range(1,n):
    if(n%i==0):
        sum1=sum1+1
if (sum1==n):
    print("the number is a perfect number!")
else:
    print("the number is not a perfect number!")
