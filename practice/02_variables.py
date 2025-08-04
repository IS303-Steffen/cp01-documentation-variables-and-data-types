from helper_functions import clear_screen
clear_screen()

# =========
# VARIABLES
# =========

'''
OVERVIEW
--------
When coding, you will need to store data and manipulate it. You store data in
variables

Think of variables as buckets that hold whatever you put into them. They are
called "variables" just like in mathematics, because the value they hold can
vary.

You give the bucket (the variable) a name, and then an = and then the value to
store into it.

WHERE ARE VARIABLES STORED ON YOUR COMPUTER?
--------------------------------------------
You are probably used to storing files (like a Microsoft Word document) on your
computer. When you store a file like that, it is stored "on disk" on your hard
drive. Think of that as long term memory, like how your brain remembers facts
like "how many states are in the USA"

However, when you create a variable in python, it is stored "in memory"
temporarily while your python code runs. In your computer, this is called RAM.
Once your python code is finished running (meaning every instruction from the
top to the bottom has been executed) then your computer just forgets any 
variables you created and their values.

Think of it like your parent telling you what to get at the grocery store. Your
brain stores that in short-term memory long enough for you to complete the task,
and then you discard the information. For example, do you remember exactly what
you bought from the grocery store a year ago? No, because it wasn't committed to
long term memory.

Later on in class, we'll learn how to store variables to your computer's "long 
term memory", aka the hard drive.
'''


# 1. CREATE A VARIABLE
# Create a variable called age, and put a number into it.
# Then make another variable to store your grandfather's age.



'''
RULES FOR VARIABLE NAMES
------------------------
1. Valid Characters
    - You can only use letters, numbers, and underscores _ .

2. Starting Characters 
    - The starting character must be a letter or an underscore. You can use
      numbers, just not at the start.

3. Case Sensitivity
    - Age and age will be two different variables.

4. Invalid Characters 
    - Spaces, and other characters like "!" can't be used anywhere in the
      variable name
    - ~!@#$%^&*()-+=[]{}\|;:'",<>./?
'''

# 2. DISPLAY A VARIABLE'S VALUE
# Use the print() function to print out the value of your first variable. Do
# it again for your second variable.


'''
VARIABLE NAMING CONVENTIONS
-------------------------
You have the freedom to name your variables whatever you want (within the rules
of Python syntax).

However, you should be aware of some naming conventions. Sticking with a single
convention style makes your code easier to read. Whatever you use, try to stick
with it for all of your code.

Snake Case: example_variable
    - All lowercase, separated underscores. This is what the makers of Python
      suggest you use for variables.

Camel Case: exampleVariable
    - lowercase first, no spaces or underscores. Capitalized first letter
      for each word afterwards.

Pascal Case: ExampleVariable
    - Same as camel, but has an Uppercased first letter. This is suggested
      to be used for Class names in Python, which we'll use later in the
      semester.

Kebab Case: example-variable
    - All lowercase, separated by a dash. Doesn't work in most languages, but
      is common in HTML


    Doesn't matter what you use! just be consistent.
'''

# 3. PRACTICE THE NAMING CONVENTIONS
# Write out your grandpa variable in each of the naming conventions. Remember
# that the naming convention changes literally nothing about the behavior of
# the variable. It is just for consistency in reading your code.

