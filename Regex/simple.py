import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Compiling a pattern 'abc' into a re object
pattern = re.compile(r'start', re.IGNORECASE) # considers both lowercase and uppercase
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}') # phone number pattern
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # Mr/Mrs/Ms names

# .finditer() returns an iterator of matches to a certain pattern
# matches = pattern.finditer(text_to_search)
matches = pattern.finditer(sentence)

# .findall() returns a list of strings made up only by the groups () instead of an object and its characteristics
#matches = pattern.findall(text_to_search) 

for match in matches:
    print(match) 
    # r'abc' --> <re.Match object; span=(1, 4), match='abc'>
    # r'.' --> matches all characters, because '.' is a Meta characters and needs to be treated in a special way
    # r'\.' --> the correct way of treating '.'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z.-]+@[a-zA-Z-]+\.(com|edu|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match) """