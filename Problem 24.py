# num=[1,3,4,1,0,1,2,3,4,0,5,2,1,5,3,0]
# Write a program to count how many times each element appears in the given list. Solve the problem using a loop and another list to keep track of the counts.
# Sample Input:
# Sample Output: Count List: [3, 4, 2, 3, 2, 2]
'''Element 0 appears 3 times.
Element 1 appears 4 times.
Element 2 appears 2 times.
Element 3 appears 3 times.
Element 4 appears 2 times.
Element 5 appears 2 times'''

# Solution:
num=[1,3,4,1,0,1,2,3,4,0,5,2,1,5,3,0]
count=[0]*(max(num)+1)
for x in num:
    count[x]+=1
print(count)
for i in range(len(count)):
    print(f"Element {i} appears {count[i]} times.")