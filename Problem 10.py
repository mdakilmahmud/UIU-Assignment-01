# Write a program that takes N integers from the user and finds the maximum number (without using built-in max).
# Sample Input: N=4
# Sample Output: Numbers: 10, 5, 20, 8

# Solution:
N = int(input("N = "))
max_number = 0
for i in range(N):
    current_number = int(input(f"Number {i + 1}: "))
    if  current_number > max_number:
        max_number = current_number
print(f"max = {max_number}")