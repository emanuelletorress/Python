# 'pass' keyword - indicates that this function isn't doing anything for now but you might add content to it later
def hello_func():
    pass

print(hello_func())

# Keeping your code dry -> not repeating yourself

# Function with parameter
def hello(arg):
    print('Hello, {}'.format(arg))

hello('Universe')

# Default value - it'll execute in case no parameter is provided
def hello2(arg = 'World!'):
    print('Hello, {}'.format(arg))

hello2()

# *args - accepts an arbitrary num of args
# **kwargs - accepts an arbitrary num of positional args
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Political Science', 'Theory of Computation', name='Misty', age=24)

course = ['Political Science', 'Theory of Computation']
info = {'name': 'Misty', 'age': 24}

# courses and info as arguments
student_info(course, info) # both were passed as positional arguments

# *courses and **info as args and kwargs - unpacking values
student_info(*course, **info)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    # docstring - documents what the function does
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""
 
    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))