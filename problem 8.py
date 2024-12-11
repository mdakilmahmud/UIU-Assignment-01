# Write a program to count the number of vowels in a given string using a loop.
# Sample Input: string="Hogwarts"
# Sample Output: Number of vowels: 2

# Solution:
word = str(input('String='))
vowel_count = 0
for char in word:
      if char in 'AEIOUaeiou':
            vowel_count+=1
print(f'Number of vowels: {vowel_count}')