# Custom messages
""" try:
    f = open('text.txt')
    print(var)
except FileNotFoundError: # specific exceptions come first in the except block
    print('File not found')
except Exception: # more generic exception should be placed at the bottom
    print('Something went wrong') """

# Messages provided by the language
try:
    f = open('text.txt')
    # print(var)

    # Raising your own exception
    """ f = open('text.txt')
    if f.name == 'text.txt':
        raise Exception """

except FileNotFoundError as e: # specific exceptions come first in the except block
    print(e)
except Exception as e: # more generic exception should be placed at the bottom
    print('Error')
else: # runs if no exception is thrown
    print(f.read())
    f.close()
finally: # runs no matter what happens in the code
    print('Executing finally...')