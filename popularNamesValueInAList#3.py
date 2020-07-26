'''
Checking if a value is in a list
Often we might want to see if a value is in a list. Python gives us the awesome in keyword that makes this very easy.
'''

# POPULAR NAMES

names =  ["charlotte", "olivia", "isla", "emily", "sophie", "oliver", "jack", "james", "mason", "liam"]

#Ask the user for their name and see if it is 
name = input("What is your name? ")

if name in names:
  print("Hey guess what? Your name was one of the top 10 baby names of 2014.  Go you!")
else:
  print(name.capitalize(),"is a great name, but it wasn't in the top 10 in 2014." )
 
 
 #######################################################################
 #PRIMARY COLORS ( practice following previous activity) 
 
 # create a list of primary colors of light, used in the pixels on your screen
primary_colors=["red", "green", "blue"];

#Ask the user to pick a color and store in the variable color
color=input("Pick a color ")

#Tell them whether or not it is one of the primary colors of light
if color in primary_colors:
  print(color,"is a primary color")
else:
  print(color.capitalize(), "is not a primary color")
  
 #######################################################################

  
  
  
  
  
