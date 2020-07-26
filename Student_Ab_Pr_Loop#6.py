
'''
Printing lists with a for loop.
We can use a for loop to access each of the values in a list, rather than just using print(list_name) . This lets us print each value on a new line, instead of all together with all the brackets and quotes:

colors = ["red", "green", "blue"]
for color in colors: 
  print(color)

'''

#Student lists
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

#Print out students present:
for student in students_present:
  print(student)
print(" ")

for student in students_absent:
  print(student)

print(len(students_present))

##################################################################################
'''
Joining items in a list with join().
If we want to format our list items nicely, but we also don't want them on different lines, we can use the join() function to combine them in other ways. 
This is like the opposite of the split() function, but the syntax is a bit different:

#example
colors = ["red", "green", "blue"]
print(" ".join(colors)) #Prints red-green-blue

#List of weapons available
weapons_available = ["Dagger", "Lance", "Flail", "Medieval Sword", "Broadsword", "Falchion sword", "Greatsword", "Longsword"]

#Print the list with commas separating
print(", ".join(weapons_available))

#Print the list with spaces separating
print(" ".join(weapons_available))

#Print the list with tildes separating ~
print("~".join(weapons_available))

#Print the list with roses separating @-->--
print("@-->--".join(weapons_available))

#####################################################################################
# Find the position of a value in a list

#List of weapons available
weapons_available = ["Dagger", "Lance", "Flail", "Medieval Sword", "Broadsword", "Falchion sword", "Greatsword", "Longsword"]

#Print the position of the Broadsword
print(weapons_available.index("Broadsword"))

#Find the position of the Flail and store as index
index = weapons_available.index("Flail")

#Print the index of the Flail in the sentence.
print(index)


#####################################################################################
'''
Count how many times a value is in a list using the count function - see next file #
We know how to find the length of an entire list, but it is also useful to be able to find out how many times a value is in a list. This is useful for several reasons:

To find out if a value is already in a list e.g. before adding it again.
To find out if a value is in there more than once e.g. to remove duplicates
To simply find out how many of that value are in the list.
'''

'''
Example
pencil_case = ["red pen", "blue pen", "pencil", "eraser" , "gluestick", "pencil", "black pen", "pencil", "red pen"]

#How many erasers?
print(pencil_case.count("eraser"))

#How many pencils?
print(pencil_case.count("pencil"))

'''







