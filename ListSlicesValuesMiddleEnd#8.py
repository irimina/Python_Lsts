# Task: Getting part of the list 
'''
Find a subset of a list.
If we have a list, we can get just part of that list to use. 
This lesson will show you different ways of getting subsets of lists, which are called slices.

The syntax for a slice is: my_list[start:stop] and start and stop are both integers. 
Like the range() function, the stop value is not included, so the list will end with the value before it.

'''

import random

#A list of students
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]

#We need to pick 3 students from the list
print(students_present[0:3])

#A list of cards
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Print the first 5 cards
print(cards[0:5])

#Shuffle the cards
random.shuffle(cards)

#Print the first 5 cards again
print(cards[0:5])

#########################################################################################
'''
Getting a slice from the middle of the list
Our slice notation looks like this: my_list[a:b]

If a is 0, we will get the first b items, starting at the beginning of the list, e.g. if b is 6, we will get the first 6 items (my_list[0:6]).

If we want to take a slice out of the middle of the list, we can use another number for a. 
The first value should be the index of the first item we want.

'''
#A list of students
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]

#We need to pick 3 students from the list, then the second 3
print(students_present[0:3])
print(students_present[3:6])

#A list of cards
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Print the first 5 cards, then the second 5 cards 
print(cards[0:5])
print(cards[5:10])

#########################################################################################
'''
Getting a slice from the end of a list.
We can also take a slice from the end of a list by leaving the stop value empty:

my_list[5:] # Gets from the 5th value to the end of the list
Remember that the value with the start index, in this case 5, is included.
'''
#A list of students
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]

#We need to pick 3 students from the list
print(students_present[0:3])
print(students_present[3:6])
print(students_present[6:])

#A list of cards
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


print(" , ".join(cards))
#Print the second 5 cards

print(cards[0:5])
print(cards[5:10])
print(cards[10:])

#########################################################################################

'''
Getting the last value in a list.
If we wanted to find the last value in the list, we could use a combination of skills like using len() 
to find the length of it and so on... BUT that involves a lot of confusing steps, so luckily Python has an easy way of doing it.
The last value in any list also has an index of -1. So:

my_list[-1] will get the last value in the list. Easy!
'''
#A list of students
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]

#We need to pick 3 students from the list
print(students_present[0:3])
print(students_present[3:6])
print(students_present[6:])
print(students_present[-1])

#A list of cards
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Print the second 5 cards
print(cards[0:5])
print(cards[5:10])
print(cards[10:])
print(cards[-1])

#########################################################################################




