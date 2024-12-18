import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ==========
# DATA TYPES
# ==========

'''
OVERVIEW
--------
In coding, data types specify the kind of data that a variable can hold.

Python is dynamically typed, meaning you don't have to explicitly specify
the data type of a variable before hand.

You simple declare the variable name, and provide it with a value. 

BASIC DATA TYPES
-----------------

    - string (str): storing text

    - integer (int): whole numbers

    - float (float): numbers with decimals

    - boolean (bool): True or False

TERMINOLOGY
-----------

When you create a variable, it is called "declaring"
When you put a value inside of a variable you are "initializing" the variable

In Python, you just declare and initialize a variable at the same time.

'''


# 1. CREATE A STRING 
# Store your name in a string. To make something a string, put the value in
# double of single quotes " " or ' '
name = 'steffen'
print(name)

# 2. CREATE AN INT
# Store your age in a variable
age = 32
print(age)

# 3. CREATE A FLOAT
# Store how much money is in your pocket in a variable
money = 10.32
print(money)

# 4. CREATE A BOOLEAN
# Store whether you like bacon or not in a variable. For booleans, you MUST
# use either True or False as the value, with a capital T or F.
bacon_liked = True
print(bacon_liked)

# 5. DISPLAY THE TYPE OF A VARIABLE
# If you want to see what the data type is, use print(type(variable_name))
# Try printing out the data type of your bacon boolean
print(type(bacon_liked))

# 6. COMBINING INTS AND FLOATS
# Try adding together your age and money variable using a plus sign +
# Store the result in a new variable and print it out. Try printing out the
# type of your new variable.

result = age + money
print(result)
print(type(result))

# 7. STORING A NUMBER AS A STRING
# Make a variable that stores your age, but as a string instead of as an
# integer. Print out the data type of the original age variable and the new
# age variable. Try adding your string age variable to the money variable
str_age = '20'
print(type(age))
print(type(str_age))


# won't work:
# result = str_age + money

'''
HUNGARIAN NOTATION
------------------
Sometimes, coders like to put the name of the datatype in the name of the
variable.

For example for the integer variable age, you might name the variable:
    i_age
    iAge
    int_age
    intAge

Notice you can use Hungarian Notation with any naming convention (snake case, 
camel case, etc.)

Hungarian notation is optional, but potentially useful to
keep track of what type a variable is at a glance. Just remember, because
Python is dynamically typed, you could accidentally give a variable a
misleading name.

I will usually not use Hungarian notation this semester, but feel free to use
it if you like it.
'''

# 8. USE HUNGARIAN NOTATION
# Create another variable for age, but this time, use hungarian notation
i_age = 34


'''
TYPE HINTS
----------
Type hints let you show your intention for the data type when creating a
variable.

age: int = 20

I think they are useful in very specific situations (making functions) which
I'll mention later in the semester. I won't use them otherwise.
'''

# 9. USE A TYPE HINT
# Create another age variable and give it a type hint of int
# Remember this doesn't actually change anything about the variable
# Try adding a mismatched type hint. Notice it doesn't actually do anything.

another_age: int = 21
print(type(another_age))

another_age: str = 21
print(type(another_age))