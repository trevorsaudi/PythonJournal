# favorite_pets = {
#     'horusr': 'cats',
#     'caisa64': 'cats and dogs',
#     '__Myst__': 'cats',
# }

# favorite_pets['akuli'] = "monkey"
# for names,pets in favorite_pets.items() :
#     print ("%s are %s favourite pets" %(pets,names))

# a program that counts the number of times  a word appears in a sentence

sentence = input("please input a sentence")

words = {}

for word in sentence.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(words.items())

for word, num in words.items():
    if num == 1:
        # "1 times" looks weird
        print(word, "appears once in the sentence")
    else:
        print(word, "appears", num, "times in the sentence")
