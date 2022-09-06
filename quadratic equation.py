# import complex math module in our program
import cmath
#taking values form user at run time.
a = int(input("enter value of a"))
b = int(input("enter value of b"))
c = int(input("enter value of c"))
 
# calculating the discriminant here
d = (b**2) - (4*a*c)
 
# finding two solutions of the quadratic equation.
s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)
# printing the two solutions.
print('The solution are {0} and {1}'.format(s1,s2))
