import re

text_to_search = r'''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped using a backslash):
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

cat
rat
bat
tat
'''

sentence = 'Start a sentence and then bring it to an end'

#raw strings in regex interprets the strings how they are
#the compile method helps us create regex objects

pattern = re.compile(r'start',re.I)

#finditer
matches = pattern.finditer(sentence)

#findall - returns matching groups
matches = pattern.findall(text_to_search)


#match - determines if the regex matches at the beginning of the string
matches = pattern.match(sentence)

#search 
matches = pattern.search(sentence)

# with open('./Regexbasics/data.txt','r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)


# for match in matches:
#     print(match) #prints out the span(position of our match) and the match itself

print(matches)