mystr = "The quick brown fox jumps over the lazy dog"

# Capitalizing the first character
print(mystr.capitalize())

# lowercase of all the characters in the string
print(mystr.lower())

# uppercase of all the characters in the string
print(mystr.upper())

# swapping the cases
print(mystr.swapcase())

# title case
print(mystr.title())


#searching in strings

# the number of times it appears in the string
# count is case sensitive
print(mystr.count('he'))

# ends with and starts with that particular string
print(mystr.endswith('dog'))
print(mystr.startswith('The'))

# finding the first instance of the word
print(mystr.find('he'))
# finding the last instance of the word
print(mystr.rfind('he'))


# checking for alphanumeric, alpha, num
#isdecimal, isdigit, islower, isnumeric, isspace, istitle, isupper
print('123#'.isalnum())
print('ABC'.isalpha())
print('ABCDEF'.isascii())


# formatting in the string

# center the string around dashes
print(mystr.center(50, '-'))

# justify the string
# left justify and right justify
print(mystr.rjust(100, '-'))
print(mystr.ljust(100, '-'))


# left strip and right strip
mystr2 = '      The Quick brown fox jumps over the lazy dog.        '

print(mystr2.strip())  # takes away spacing from both sides of the string
print(mystr2.lstrip())
print(mystr2.rstrip())


#splitting, partitioning
# partition returns three things, everything before the first instance of what is being partitioned,
# the partition character, then the rest of the string
print(mystr.partition(' '))
print(mystr.partition('brown'))

# rpartition - starts partitioning from the end
print(mystr.rpartition('he'))

# split, find every instance of the character and splits
print(mystr.split(' '))

# splitlines , splitting on a line
text = ''' Trevor joined Strathmore
in the year 2018
'''
print(text.splitlines())

#join and split
names = ["Trevor", "Matilda", "Mbarire", "Billy"]
a = ""
print(a.join(['M', 'o', 'b']))

b = "-"
print(b.join("MCO"))

print(''.join(mystr))

ssn = "123-12-123"
print(ssn.split('-'))
# joining a list into one string
print(" ".join(names))

# splicing
names = ["Trevor", "Matilda", "Mbarire", "Billy"]
print(names[1:])
print(names[:2])
print(names[-1])
