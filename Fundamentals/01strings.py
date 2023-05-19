# Multi-line string: use three double quotes
message = """Hi!
I'm nurse joy"""
print(message)

msg = 'Hello World'

# Length of a string
print(len(msg)) # 11

# Access a certain character
print(msg[2]) # l

# Slicing - access a portion of the string - first index is inclusive, second is not
print(msg[0:6]) # Hello
print(msg[6:]) # World

print(msg.lower())
print(msg.upper())

# .count() - counts words or characters in a string
print(msg.count('World')) # 1
print(msg.count('l')) # 3

# .find() - finds the first char
print(msg.find('l')) # 2

# .replace(_,_) - returns a string
print(msg.replace('World', 'Universe')) # Hello Universe

name = 'Manu'
greeting = 'Hell<3'
# '{}'.format(_)
print('{}, {}'.format(name, greeting)) # Manu, Hell<3

# f'{variable}' - f string
print(f'{name}, {greeting}') # Manu, Hell<3