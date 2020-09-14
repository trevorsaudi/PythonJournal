# The zip function iterates through multiple iterables, and aggregates them
# uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lowercase = 'abcdefghijklmnopqrstuvwxyz'


# for upper, lower in zip(uppercase, lowercase):
#     print(upper, lower)


uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

#combining enumerate and zip helps us extract the index
for i, (upper, lower) in enumerate(zip(uppercase, lowercase)):

    print(i+1, upper, lower)
