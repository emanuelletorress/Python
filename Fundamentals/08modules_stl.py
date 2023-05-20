# module name cannot start out with numbers

# with no alias
# import my_module

# with alias
# import my_modules as mm

# importing everything - NOT RECOMMENDED as you won't know where a certain method came from
# from my_module import *

# importing components directly with aliases
from my_module import find_index as fi, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
print(index)
print(test)

# python finds the module by checking a list called sys.path
# the first path is the one where this file is
import sys
print(sys.path)

# some python modules from the stl
import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2023))

# os - gets us access to the underlying os
import os

# current working directory
print(os.getcwd())

# printing the location of this file on the file system
print(os.__file__)