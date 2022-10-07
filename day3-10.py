def comb(L):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=j and j!=k and i!=k):
                    print(L[i],L[j],L[k])
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
if ((n1>=0)and(n2>=0)and(n3>=0)):
    comb([n1,n2,n3])
else:
    print("Enter only positive values")
