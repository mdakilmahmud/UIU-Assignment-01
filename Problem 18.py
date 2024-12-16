# Write a program to count how many numbers in the calculates the sumof the indices of the odd and even numbers.
# num_list=[2,4,3,77,32,5,12,35,68,50,100]
# Sample Input:
# Sample Output:Odd numbers: 4
'''Even numbers: 7
Sum of indices of odd
numbers: 18
Sum of indices of even
numbers: 33'''

# Solution:
list1 = [2, 4, 3, 77, 32, 5, 12, 35, 68, 50, 100]
even_count = 0
odd_count = 0
sum_even_indices = 0
sum_odd_indices = 0
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        even_count += 1
        sum_even_indices += i
    else:
        odd_count += 1
        sum_odd_indices += i
print(f"Odd numbers: {odd_count}")
print(f"Even numbers: {even_count}")
print(f"Sum of indices of odd numbers: {sum_odd_indices}")
print(f"Sum of indices of even numbers: {sum_even_indices}")