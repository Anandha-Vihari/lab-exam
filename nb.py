import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

msglbl_data = pd.read_csv('Statements_data.csv', names=['Message', 'Label'])
print("The Total instances in the Dataset: ", msglbl_data.shape[0])

msglbl_data['labelnum'] = msglbl_data.Label.map({'pos': 1, 'neg': 0})

X = msglbl_data["Message"]
Y = msglbl_data.labelnum

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y)

count_vect = CountVectorizer()
Xtrain_dims = count_vect.fit_transform(Xtrain)
Xtest_dims = count_vect.transform(Xtest)

df = pd.DataFrame(Xtrain_dims.toarray(), columns=count_vect.get_feature_names_out())

clf = MultinomialNB()
clf.fit(Xtrain_dims, Ytrain)

prediction = clf.predict(Xtest_dims)

print('******** Accuracy Metrics *********')
print('Accuracy : ', accuracy_score(Ytest, prediction)) 
print('Recall : ', recall_score(Ytest, prediction)) 
print('Precision : ', precision_score(Ytest, prediction))
print('Confusion Matrix : \n', confusion_matrix(Ytest, prediction))
print(10*"-")

test_stmt = [input("Enter any statement to predict :")]
test_dims = count_vect.transform(test_stmt)
pred = clf.predict(test_dims)

for stmt, lbl in zip(test_stmt, pred):
    if lbl == 1:
        print("Statement is Positive")
    else:
        print("Statement is Negative")
