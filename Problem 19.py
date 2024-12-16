# Write a program to print each spell in the list along with its length.
# spells = ["Expelliarmus", "Lumos", "Alohomora", "Accio", "Expecto Patronum"]
# Sample Input:
# Sample Output: Expelliarmus: 12 characters
'''Lumos: 5 characters
Alohomora: 9 characters
Accio: 5 characters
Expecto Patronum: 17
characters'''

# Solution:
spells = ["Expelliarmus", "Lumos", "Alohomora", "Accio", "Expecto Patronum"]
for item in spells:
    print(f"{item}: {len(item)} characters")  