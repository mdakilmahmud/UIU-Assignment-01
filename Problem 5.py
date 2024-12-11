# Write a program to count how many numbers between 1 and n are divisible by both 3 and 7.
# Sample Input: n=30
# Sample Output: count=2120

# Solution:
num=int(input('n='))
for i in range(1,num):
      if i%3==0 and i%7==0:
            print('count=',i)