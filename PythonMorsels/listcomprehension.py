#easier way of creating lists

nums = [1,2,3,4,5,6,7,8,9,10]

#examples
#I want 'n' for each 'n' in nums

my_list = []

for n in nums:
    my_list.append(n)
print (my_list)

#the list comprehension of the above

my_list = [n for n in nums]
print (my_list)



# I want n*n for each n in nums
my_list2 = []
for n in nums:
    my_list2.append(n*n)
print (my_list2)

# the list comprehension of the above
my_list2 = [n*n for n in nums]
print(my_list2)
# using lambdas and maps


# I want n for each n in nums if n is even

my_list3 = []

for n in nums:
    if n%2==0:
        my_list3.append(n)
print (my_list3)

#the list comprehension for the above
my_list3 = [n for n in nums if n%2==0]
print(my_list3)

#I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

letter = 'abcd'
my_list4 = []
for num,letter in (zip(letter,nums)):
    my_list4.append((num,letter))
print (my_list4)


#list comprehension for the above
my_list4 = [(letter,nums) for (letter,nums) in (zip(letter,nums)) ]
print(my_list4)