# Write a program that will find x y (x to the power y) where x, y are positive integers.
# Sample Input:5 2 | 2 4
# Sample Output:25 | 16

# Solution:
num1, num2 = map(int, input("Enter x and y (space-separated): ").split())
result = num1 ** num2
print(result)