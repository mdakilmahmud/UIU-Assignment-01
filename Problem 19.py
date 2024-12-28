# num=[22,42,12,6,0,44,346,23,9,3] Write a program to print the maximum number in the given List. (You cannot use max() function)
# Sample Input:
# Sample Output: Max value is : 346

# Solution:
num=[22,42,12,6,0,44,346,23,9,3]
max_value=0
for i in num:
      if i>max_value:
            max_value=i
print(f'Max value: {max_value}')