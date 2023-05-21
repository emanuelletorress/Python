'''
LEGB - the order of scope checked by python
Local, Enclosing, Global, Built-in methods
'''

# Overwriting a global variable
""" x = 'global x'
def test():
    global x # tells python we're working with the global x now
    x = 'local x'
    print(x)

test()
print(x) """

# Working with enclosing functions
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        nonlocal x # overwriting the nonlocal x variables
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)
