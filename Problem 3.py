# Write a program that will print the following series upto Nth terms.(1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, …….)
# Sample Input: N=5
# Sample Output: 1,0,1,0,1

# Solution:
num = int(input('N = '))
for i in range(num):
      if i%2==0:
            print(1,end=",")
      else:
            print(0,end=",")