a=float(input("Enter the Starting number: "))
b=int(input("Maximum no of lines to be printed: "))
for i in range(b):
    for j in range(i+1):
        print('%.1f'%a,end=" ")
        a=a+0.1
    print()
