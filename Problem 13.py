# Write a program that will find the GCD (greatest common divisor) and LCM (least common multiple) of two positive integers.
# Sample Input: 5 7
# Sample Output: GCD: 1 | LCM: 35

# Solution:
a = int(input("Enter a number (X): "))
b = int(input("Enter a number (Y): "))
x = a
y = b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = (a * b) // gcd
print(f'GCD: {gcd}')
print(f'LCM: {lcm}')
