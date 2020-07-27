# Sort a list 

'''
This lesson will look at some other functions that will allow you to sort, shuffle and pick random values with lists.

The first function we will look at is sort(). You can probably guess what that does! There are some things to remember from level 1:

Capitals come 'before' lower case letters.
You can't sort a list with both strings and integers, unless you turn the numbers into strings by putting them in quotes "".

Note that the sort() function actually changes the list to the new order, so you can't get the original order back after using it.

EX:
numbers = [34, 3, 7, 56, 1, 2, 976, 425435, 4, 8, 67]
numbers.sort()
print(numbers)

'''
#Student lists
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

#Sort the students present list and print
print("Students present: ")

students_present.sort()

for student in students_present:
  print(student.title())
  
#Sort the students absent list and print
print("Students absent: ")
students_absent.sort()

for student in students_absent:
  print(student.title())
  
#############################################################################
# Get and sort a shopping list

''''
Let's try using sort() in a slightly bigger program where it might be more useful.

The code in the editor uses a loop to ask the user for all of the items for their grocery list. 
When the user types in done, we will print out their list of items in alphabetical order.
We're going to use the code we saw in the last lesson to make sure we don't get duplicates in the list too!
''''


# INITIAL CODE

#Create an empty grocery_list


#Start a loop to ask user to enter their grocery list
repeat = True
while repeat == True:
  item = input("Please enter an item or 'done' to end input: ").strip().lower()
  
  #Check if user has entered done so that loop can be stopped if so
  if item == ???:
    repeat = ???
  else:
    #Check if item is already in list
    count = ???
    
    #If so, give user error message, otherwise add the item and give success message
    if count > 0:
      print("Sorry {} is already on the list!".format(item))
    else:
      grocery_list.append(item)
      print("{} has been added!".format(item))

#Once user is done, sort the list then print out their list for them
print("Your grocery list is: ")


# FINAL 
#Create an empty grocery_list
grocery_list=[]

#Start a loop to ask user to enter their grocery list

repeat = True
while repeat == True:
  item = input("Please enter an item or 'done' to end input: ")
  
  #Check if user has entered done so that loop can be stopped if so
  if item == 'done':
    repeat = False
  elif item in grocery_list:
    print(item, "is already on the list!")
  else:
    grocery_list.append(item)
    print(item," has been added!")

#Once user is done, sort the list then print out their list for them
print("Your grocery list is: ")
print(grocery_list.sort())
for item in grocery_list:
  print(item.title()) #Add a capital letter




#############################################################################

'''
Shuffle a deck of cards
In the level 1 course, we learned about using the random module to generate random numbers. 
We can use some other functions that come with the random module to work with lists.

Let's take a look at shuffle(), remembering we have to import the random module if we want to use it:

import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
'''
#Import the random module
import random 

#A list of cards
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print("Initial cards arrangement before shuffle: ")
print(cards)

print("After the shuffle")
#Shuffle the cards and print
random.shuffle(cards)

print(cards)

print("After the second shuffle")
#Shuffle the cards and print
random.shuffle(cards)

print(cards)


#############################################################################

'''
Pick a random item from a list using shuffle().
With the code we have learned, there are two possible ways we can pick a random item from a list:

Pick a random number (i) then get the item in that position e.g. my_list[i]
Shuffle the list and get the first item e.g. my_list[0].

'''
import random

#Create a list of responses
responses = ["Yes", "No", "Maybe", "Outlook Doubtful", "It is impossible to say", "Try again later", "nobody knows", "Definitely"]

#Ask the user for their name and store it, welcome the user
name = input("What is your name?").title()
print("Hi", name, "this Magic 8 Ball can answer all of your burning questions")

#Use a loop to let the user ask their questions
repeat = True
while repeat == True:
  question = input("Please ask a yes or no question or type 'done' to quit:")
  
  if question == "done":
    print("All the best for the future. Goodbye!")
    repeat = False
  else:
    random.shuffle(responses)
    print(responses[0])

#############################################################################
Refactor code to pick a random item using random numbers.
Now let's try that same code again, using a random number to get the response instead of shuffling the list.

#To import the random module:
import random

#Generate a random number from 1 to 10 with it
number = random.randrange(1, 11)
print(number)

# CODE FINAL PROGRAM 
import random

#Create a list of responses
responses = ["Yes", "No", "Maybe", "Outlook Doubtful", "It is impossible to say", "Try again later", "There is a chance", "Without a doubt"]

#Ask the user for their name ad store it, welcome the user
name = input("What is your name?").title()
print("Hi, this Magic 8 Ball can answer all of your burning questions")

#Use a loop to let the user ask their questions
repeat = True
while repeat == True:
  question = input("Please ask a yes or no question or type 'done' to quit:")
  if question == "done":
    print("All the best for the future. Goodbye!")
    repeat = False
  else:
    i= random.randrange(0, len(responses))
    print(responses[i])

