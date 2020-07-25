'''
task 1
The print() function outputs text to the screen. 
On line 2, print Welcome to AP CSP.
On line 5, use input() to ask the user for their name and store it in a variable called name.
On line 6, print out Nice to meet you [...] where [...] is the name the user types in.


task #2
calculator

#This prints out the result of 2 + 13
print(2 + 13)

#Print out the result of 3 * 7
print(3*7)

#Order of operations
print((3 + 4) * 7 - 1)

#Print some division
print(4/4)

task # 3
review Boolean

#Boolean values
print(4 > 7) #Change to print False
print("Level 1" != "Level 2") #Change to print True

#Ask the user how they are and respond accordingly
mood = input("How are you feeling today?")

if mood == "happy":
  print("That's great!")
elif mood == "sad":
  print("Tomorrow is another day..")
else:
  print("It happens")

task #4 
Loops

#For loop printing numbers 1-15
for i in range(1, 16):
  print(i)

#For loop printing a string three times
for i in range(3):
  print("I see red!")
  
#While loop printing numbers with 10 included
i = 0
while i <= 10:
  print(i)
  i += 1
  
#While loop that repeats until input matches the condition
password = input("Enter the password: ")
while password != "monty":
  print("Wrong password!")
  password = input("Enter the password: ")

print("Password accepted")


'''
