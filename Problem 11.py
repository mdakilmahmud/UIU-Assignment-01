# Write a program that will take two numbers X and Y as inputs. Then it will print the square of X and increment (if XY) X by 1, until X reaches Y. If and when X is equal to Y, the program prints “Reached!”
# Sample Input:x=5, y=10
# Sample Output:25, 36, 49, 64, 81, Reached!

# Solution:
n=int(input('Enter a number x = '))
n1=int(input('Enter a number y = '))
while n<n1:
    print(n**2, end = ",")
    n+= 1
print("Reached!")