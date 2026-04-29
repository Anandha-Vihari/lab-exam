
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = pd.read_csv("Statements_data.csv", names=['Message', 'Label'])

data['labelnum'] = data.Label.map({'pos':1, 'neg':0})

X = data["Message"]
Y = data["labelnum"]

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y)

cv = CountVectorizer()

Xtrain_dtm = cv.fit_transform(Xtrain)
Xtest_dtm = cv.transform(Xtest)

model = MultinomialNB()
model.fit(Xtrain_dtm, Ytrain)

pred = model.predict(Xtest_dtm)

print("Accuracy:", accuracy_score(Ytest, pred))

msg = ["This is a good product"]
msg_dtm = cv.transform(msg)

result = model.predict(msg_dtm)

if result[0] == 1:
    print("Positive")
else:
    print("Negative")