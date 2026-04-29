import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("Statements_data.csv", names=['Message', 'Label'])

data['labelnum'] = data.Label.map({'pos':1, 'neg':0})

X = data["Message"]
Y = data["labelnum"]

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y)

cv = CountVectorizer()

Xtrain_dtm = cv.fit_transform(Xtrain)
Xtest_dtm = cv.transform(Xtest)

model = MLPClassifier(hidden_layer_sizes=(5,2), max_iter=1000)

model.fit(Xtrain_dtm, Ytrain)

pred = model.predict(Xtest_dtm)

print("Accuracy:", accuracy_score(Ytest, pred))