

#########################################
'''
Using the numbers list items, print out 4 + 6 on line 5.
Use a print statement to print out the 3rd number multiplied by the 5th number.
Print out the result of 2 + 4 * 6, but make the addition happen first (hint: BEDMAS).
Print out the maximum number in the list.
Print out the minimum number in the list.
'''

# Numbers list
numbers = [2, 4, 6, 8, 10, 12]

# Print calculations
print(numbers[1]+ numbers[2])
print(numbers[2]* numbers[4])

print((numbers[0]+numbers[1])*numbers[2])

print(max(numbers))
print(min(numbers))
#########################################
Using list values that are strings
If we have some values in our list that are strings, we can use those wherever we would normally use string variables in our code.

For example, we can use them in conditions, we can use string functions like .strip() and .lower() on them, and we can use .format() 
to plug them into other strings.


#List of computer's favorites
favorites = ['blue', 9, 'pizza', 3.14159]

#Print statement


#Ask the user for their favorite food, check if it is the same as the computer
food = input("What is your favorite food?")
food = food.strip().lower()

if food == favorites[?]:
  #A function is used to make sure there is a capital at the start of the print statement
  print("{} is my favorite food too!".format(favorites[?].???))
  
else:
  print("{} is OK, but I prefer {}.".format(food.???, favorites[?]))
  
#Answer:
#List of computer's favorites
favorites = ['blue', 9, 'pizza', 3.14159]

#Print statement
print(favorites[0].upper())


#Ask the user for their favorite food, check if it is the same as the computer
food = input("What is your favorite food?")
food = food.strip().lower()

if food == favorites[2]:
  #A function is used to make sure there is a capital at the start of the print statement
  print("{} is my favorite food too!".format(favorites[2].capitalize()))
else:
  print("{} is OK, but I prefer {}.".format(food.capitalize(), favorites[2]))

  
#########################################
Checking if a value is in a list








#########################################





