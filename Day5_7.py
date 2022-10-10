def length(str):
    lis = list(str.split(" "))
    return len(lis[-1])
 
str = input("Enter the string: ")
print("The length of the last word is",length(str))
