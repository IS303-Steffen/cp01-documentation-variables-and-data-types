from helper_functions import clear_screen
clear_screen()

# ==========
# TYPE HINTS
# ==========

'''
OVERVIEW
--------
Type hints let you show your intention for the data type when creating a
variable.

age: int = 20

I think they are useful in very specific situations (making functions) which
I'll mention later in the semester. I won't use them otherwise.

If you use them, beware that just because you used a type hint, that doesn't 
mean that data type is enforced for that variable. For example, you could 
list int as the data type, but still put a string inside. Type hints only
show your intention, not necessarily the reality.
'''

# 1. USE A TYPE HINT
# Create another age variable and give it a type hint of int
# Remember this doesn't actually change anything about the variable
# Try adding a mismatched type hint. Notice it doesn't actually do anything.

