# Take a list input from the console and Write a program to check if a specific number is present in a list.
# Sample Input: list=[111,2,43] | n=111 | n=4
# Sample Output: Present | Not Found!

# Solution:
lst=list(map(int,input("Enter the list (space-separated)= ").split()))
n=int(input("Enter the number you want to search n= "))
for item in lst:
      if item == n:
            print('Found!')
            break
else:
      print('Not Found')