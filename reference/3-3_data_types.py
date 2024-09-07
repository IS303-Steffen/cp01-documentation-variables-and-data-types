# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

# DATA TYPES

'''
string: for storing text

integer (or int): Whole numbers, no decimals

float: number w/ decimals

boolean: True or False. 


'''

# store you name in a variable
# you can use single or double quotes
name = 'steffen'

# store your age in a variable
age = 32

# store how much money is in your pocket in a variable
money = 10.32

# state whether you like bacon or not
bacon_liked = True


# if you want to see what the data type is:
# print(type(variableName))
print(type(money))
# remember that python is dynamically typed! (instead of statically typed)

# PRACTICE #1
#   store an integer and a float in two separate variables. Print out their sum.

result = age + money
print(result)


# Hungarian notation
'''
Sometimes, people like to put the name of the datatype in the name of the variable
This is optional, but I recommend it if you want to keep track of what type it is
Just remember, don't name it something like iMoney if you are actually storing a Float
'''

i_age = 34