# hogwarts=[“Harry”,”Ron”,”Hermione”, “Dobby”, “Bellatrix”, “Voldemort”, “Ginny”, “Luna”, “Snape”] Write a program to filter out names from the list that have more than 5 letters.
# Sample Input:
# Sample Output:Hermione | Bellatrix| Voldemort

# Solution:
hogwarts = ['Harry', 'Ron', 'Hermione', 'Dobby', 'Bellatrix', 'Voldemort', 'Ginny', 'Luna', 'Snape']
for name in hogwarts:
      if len(name)>5:
            print(name)