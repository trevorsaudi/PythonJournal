# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object
stack = []
while (True):
    lines = input(
        "Enter something, and press enter without typing anything when done ")
    if (lines != ""):
        stack.append(lines)
    else:
        break

for num, words in enumerate(stack, start=1):
    print("Line %d : %s" % (num, words))
