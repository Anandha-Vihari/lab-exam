import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

def remove_stopwords(text):
    words = word_tokenize(text)
    english_stopwords = set(stopwords.words("english"))

    filtered_words = [
        word for word in words
        if word.lower() not in english_stopwords
    ]

    filtered_text = " ".join(filtered_words)
    return filtered_text

text = "NLTK is a leading platform for building Python programs to work with human language data."

filtered_text = remove_stopwords(text)

print(filtered_text)
