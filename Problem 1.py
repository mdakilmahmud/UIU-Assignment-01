# Write a program that will take an input n from the console and print the following series up to n-th terms.
# Sample Input: n=5
# Sample Output: 1, 2, 3, 4, 5

# Solution:
n=int(input('n = '))
for i in range(1,n):
      print(i,end=",")
print(n)