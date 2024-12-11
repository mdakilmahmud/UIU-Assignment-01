# Write a program that will take a string as an input and print the string backwards using loops.
# Sample input: String=”Dumbledore”
# Sample output: erodelbmuD

# Solution:
str_ing=str(input('String='))
reversed_string=""
for char in str_ing:
      reversed_string=char + reversed_string
print(reversed_string)