import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

def tokenize_words(text):
    words = word_tokenize(text)
    return words

text = "NLTK is a leading platform for building Python programs to work with human language data."

words = tokenize_words(text)

print(words)
