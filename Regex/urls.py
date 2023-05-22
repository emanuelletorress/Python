import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# Searches through pattern and substitutes \2 and \3 in subbed_urls with group 2 and group 3 of the pattern
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3)) # groups: ()