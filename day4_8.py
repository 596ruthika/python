def findMean(a, n):
  sum = 0
for i in range(0, n):
       sum += a[i]
return float(sum/n)
 # Function for calculating median
def findMedian(a, n):
   # First we sort the array
    sorted(a)
   # check for even case
if n % 2 != 0:
      return float(a[int(n/2)])
 
return float((a[int((n-1)/2)] + a[int(n/2)])/2.0)
 # Driver code
a = [1, 3, 4, 2, 7, 5, 8, 6]
n = len(a)
 # Function call
print("Mean =", findMean(a, n))
print("Median =", findMedian(a, n))
