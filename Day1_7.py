#binary_sum
A = input("a= ")
B = input("b= ")
P = set(A)
X = set(B)
S = {'0','1'}
if S==P or P=={'0'} or P=={'1'} and S==X or X=={'0'} or X=={'1'}:
    A = int(A,2)
    B = int(B,2)
    C = bin(A+B)
    d = C[2:]
    print (d)
else:
    print("Enter only 0 or 1")
