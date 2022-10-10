def power (x,n):
    return x**n
def addition (x,n):
    return x+n
def substraction (x,n):
    return x-n
def multiplication (x,n):
    return x*n
def division (x,n):
    return x/n

print("select operation")
print("1.power")
print("2.addition")
print("3.substraction")
print("4.multiplication")
print("5.division")

while True:
    choice=input("enter choice (1/2/3/4/5):")
    if choice in ('1','2','3','4','5'):
            num1= float(input("enter the first number="))
            num2=float(input("enter the second number="))
            if choice=='1':
               print (num1,"**",num2, "=",power(num1,num2))
            elif choice=='2':
                print(num1,"+",num2, "=",addition(num1,num2))
            elif choice=='3':
                print (num1,"-",num2, "=",substraction(num1,num2))
            elif choice=='4':
                print (num1,"*",num2, "=",multiplication(num1,num2))
            elif choice=='5':
                print (num1,"/",num2, "=",division(num1,num2))
            else:
                    print("invalid")
