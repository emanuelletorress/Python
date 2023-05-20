# Python doesn't have switch case

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

user = 'Admin'
logged_in = False

# not keyword
if not logged_in:
    print('Please, log in')

# is keyword - checks if two objects occupy the same memory location - '==' checks the values only
# Example 1 - they are in different memory location
a = [1,2,3]
b = [1,2,3]
print(id(a)) # id is the memory location
print(id(b))
print(a is b) # False

# Example 2 - they are the same object
a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b) # True

# All values that evaluate to False (everything else evaluates to True):
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')