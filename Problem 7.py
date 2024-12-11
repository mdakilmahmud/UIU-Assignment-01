# Write a program that will reverse the digits of an input integer.
# Sample Input: Enter a number: 1234
# Sample Output: 4321

# Solution:
original_num = int(input("Enter a number: "))
reversed_number = 0
is_negative = original_num < 0
if is_negative:
    original_num = -original_num
num_str = str(original_num)
for digit in num_str:
    reversed_number = reversed_number * 10 + int(digit)
if is_negative:
    reversed_number = -reversed_number
print("Reversed number:", reversed_number)
