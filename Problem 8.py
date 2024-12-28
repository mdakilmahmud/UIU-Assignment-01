# Write a program that will reverse the digits of an input integer.
# Sample Input: Enter a number: 1234
# Sample Output: 4321

# Solution:
original_num = int(input("Enter a number: "))
is_negative = original_num < 0
if is_negative:
    original_num = -original_num
reversed_number = int(str(original_num)[::-1])
if is_negative:
    reversed_number = -reversed_number
print("Reversed number:", reversed_number)