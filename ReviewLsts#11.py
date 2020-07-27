
'''
Reviewing lists
Alright, let's review what we've learned in lessons 1-9 about lists!

We create a list by putting values inside square brackets []. 
Values can be integers, strings, floats, Boolean or even other lists. They get separated by commas ,.

##############################################
# task # 1

#Create a list of 5 numbers called numbers, containing integers and floats


#Create a list of animals


#Print the first number using its index


#Print the last animal using its index

##############################################
#We've also learned how to use list functions such as pop() and append() to modify lists.

#Create a list called numbers
numbers = [5, 10, 15, 20]

#Create a list of animals
animals = ["cat", "dog", "rabbit", "turtle", "mouse"]

#Insert the number 0 at the start of the numbers list


#Add "snake" to the end of the animals list


#Remove 20 from the numbers list


#Remove the 3rd animal from the animals list


#Print each list



##############################################
'''
Review shuffling, sorting and looping through lists
Lists have a built-in function called sort() that will sort a list into order. This works if the list is all the same datatype, but you can't sort a list with, for example, strings and integers.

We can also shuffle it, but we have to import the random module to do this.

If we want to use each of the values, we can loop through the list with a for loop using in.
'''


#Add random module


#Create a list of animals
animals = ["dog", "turtle", "mouse", "cat", "snake"]

#Sort the list alphabetically


#Print the list with a loop



print("----------------")

#Shuffle the list


#Print the list again with a loop
##############################################
'''
Review slices.
Slices are like subsets of lists, such as the first 3 values in a list. 
When we use slice notation, we actually make a copy of the list containing those values, so the original list is unchanged and we can use the slice the same way we would use any other list.

my_list[start:stop] - remember the stop value is not included.

'''
#Create a list of students
students = ["lisa", "sebastian", "frank", "maia",  "alex"]

#Print the first 2 students


#Print the last 3 students


#Print the middle 3 students

##############################################


'''
