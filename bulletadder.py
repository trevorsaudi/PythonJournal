import pyperclip
text = pyperclip.paste()


lines  = text.split('\n')

print(lines)


for i in range (len(lines)): # loop through all indexes of the lines list
    lines[i] = "*" + lines[i] # add a a star to each string in lines list

text = '\n'.join(lines)

pyperclip.copy(text)

