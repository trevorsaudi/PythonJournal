import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') 


#substitute the pattern match with group 2 and 3
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(0))