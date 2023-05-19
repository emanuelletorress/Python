# Also called hashmaps or associative arrays
# Each value has a key
# Values can be of any type
student = {'name': 'Manu', 'age': 24, 'courses': ['compSci', 'compEng']}

# Getting a value through a key
print(student['name'])

# Returns None in case of a key that doesn't exist
print(student.get('lyrics'))

# Returns 'Not found' in case of a key that doesn't exist
print(student.get('lyrics', 'Not found'))

# Adding a key
student['lyrics'] = '8888'
print(student)

# Ways of updating values
student['name'] = 'Lilith'
print(student)

student.update({'name': 'Numa', 'lyrics': 'HWAA'})
print(student)

# Deleting a key
del student['age']
print(student)

# .pop() returns a value
# len(dict)
# dict.values() returns a list of values
# dict.items() returns a list of tuples (key, value)

# Looping through a dict
for key, value in student.items():
    print(key, value)