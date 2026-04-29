
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

clf = svm.SVC(kernel='linear', C=1)
clf.fit(x_train, y_train)

pred = clf.predict(x_test)

print("Accuracy:", accuracy_score(y_test, pred) * 100)