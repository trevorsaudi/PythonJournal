# reverse all words in a sentence longer than 4 characters
def spin_words(sentence):

    words = sentence.split(" ")

    if len(words) == 0:
        return

    for i, word in enumerate(words):
        if (len(word) >= 5):

            words[i] = reverse(word)

    return " ".join(words)


def reverse(s):
    return s[::-1]


# expected output olleH my name is roverT iduaS and I am in eromhtartS ytisrevinU
print(spin_words("Hello my name is Trevor Saudi and I am in Strathmore University"))
