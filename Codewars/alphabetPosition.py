# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# ord is an inbuilt method that can convert letters to numericals

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def alphabet_position(text):

    # return ''.join(str(ord(c)-96) for c in text.lower() if c.isalpha())

    # check if the string type is valid
    if type(text) == str:
        # convert the string into lowercase
        new_text = text.lower()
        result = ''

    for letter in new_text:  # loop through all letters in the string
        if (letter.isalpha()):  # check if the letter is in the alphhabet
            # append the index of the letter in result, separate them with a space
            result = result + ' ' + str(alphabet.index(letter)+1)
    return result.lstrip()  # remove the space on the far left


print(alphabet_position("Hello"))
