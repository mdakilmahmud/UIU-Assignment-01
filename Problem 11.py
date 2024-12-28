# Write a program that will take N numbers as inputs and compute their average. (Restriction: Without using any array)
# Sample Input: N=3 & 10 , 5, 6
# Sample Output: Average : 7

# Solution:
num=int(input('N = '))
total=0
for i in range(num):
       num1= float(input(f'n{i+1} = '))
       total+=num1 
average=total/num
print(f'Average:{average}')