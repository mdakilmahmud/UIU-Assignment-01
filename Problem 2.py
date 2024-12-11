#Write a program that prints all Odd numbers between 1 to N. (use While or For loop.)
# Sample Input: N=10
# Sample Output: 1,3,5,7,9

# Solution: 
n=int(input('N = '))
for i in range(1,n,2):
      if i!=n-1:
            print(i,end=", ")
      else:
            print(i)