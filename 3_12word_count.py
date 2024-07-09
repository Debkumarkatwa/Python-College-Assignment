# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
def count_words(words):

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1

    return word_freq

string="Hello world hello hello world world"
words=string.split()
word_freq=count_words(words)
print(word_freq)