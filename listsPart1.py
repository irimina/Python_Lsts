# intro to lists part 1 

################################################################
Task: add your birthday number, your name and a number

#A list of numbers
numbers = [10, 20, 30, 40, 50, 60]

#A list of names
names = ["Sarah", "Jose", "Tane", "mart"]

#A list of mixed values
my_favorites = [9, "blue", "butter paneer", "peaches", "kumara", "Saturday", 3.14159]


################################################################
Task: Print values from a list
#A list of numbers
numbers = [10, 20, 30, 40, 50, 60]

#A list of names
names = ["Sarah", "Jose", "Tane", "Monty"]

#A list of mixed values
my_favorites = [9, "blue", "butter paneer", "peaches", "kumara", "Saturday", 3.14159]

#Add your code here to print the entire list, the 3rd name and your favoeite fruit from the list
print(numbers)
print(names[2])
print(my_favorites[3])


################################################################
# click run to see what it does

#String of characters
alpha_string = "abcdefghijklmnopqrstuvwxyz"

#Convert it to a list using list()
alpha_list = list(alpha_string)
print(alpha_list)

#Create a string with vowels
#Convert it to a list of vowels

#String of characters
alpha_string = "abcdefghijklmnopqrstuvwxyz"

#Convert it to a list using list()
alpha_list = list(alpha_string)
print(alpha_list)

#Create a string with vowels
vowel_string="aeiou"

#Convert it to a list of vowels
vowel_list=list(vowel_string)

print(vowel_list)

################################################################

Task: Creating a list using the .split() function

Names list
name_string = "Becky Steve Thomas Rachel Bob Tom Miguel Hone Anahera Wei-ling"

#Split the names into a list on spaces (default)
names_list = name_string.split()


#Create a string with items on new lines (you don't need \n)


#Turn it into a list using .split()
#Names list
name_string = "Becky Steve Thomas Rachel Bob Tom Miguel Hone Anahera Wei-ling"

#Split the names into a list on spaces (default)
names_list = name_string.split()
print(names_list)

#Create a string with items on new lines (you don't need \n)
item_string= """ water
computer
school
network
hammer
walking
violently
mediocre
literature
chair
two
window
cords
musical
zebra
xylophone
penguin
home
dog kennel
final
ink
teacher
fun """
#Turn it into a list using .split()
item_list = item_string.split("\n")
print(item_list)

################################################################





################################################################
