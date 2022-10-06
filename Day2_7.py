a=input("s1 = ")
b=input("s2 = ")
c=min(len(a),len(b))
d=0
for i in range(c):
    if(a[i]==b[i]):
        d+=1
print("There are ",d,"characters different in ",a," and ",b)
