import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

attributes = ['Sample Code Number']
wisconsin_data = pd.read_csv('breast-cancer-wisconsin.csv', index_col=False, header=0).dropna('id', axis=1)

X = [[0,699], [1,9]]
y = [2, 4]


X_train, X_test, y_train, y_test = train_test_split(features.values.astype(int), labels.values.astype(int), test_size=.33)
clf = MLPClassifier()
clf.fit(X_train, y_train)

print clf.score(X_test, y_test)


