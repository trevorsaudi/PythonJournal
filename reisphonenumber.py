import re

isphonenumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = isphonenumber.search('My number is 415-555-4242')
print(mo.group())

#grouping with parentheses

isphonenumber2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = isphonenumber2.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
#retrieving all the groups at once using the groups() method
print(mo.groups())
areacode, mainNumber =  mo.groups()
print(areacode,mainNumber)