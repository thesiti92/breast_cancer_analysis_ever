import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


wisconsin_data = pd.read_csv('breast-cancer-wisconsin.csv', index_col=False, header=0).dropna('id', axis=1)


X_train, X_test, y_train, y_test = train_test_split(features.values.astype(int), labels.values.astype(int), test_size=.33)
clf = MLPClassifier()
clf.fit(X_train, y_train)

print


#ask alex what score means, is there a way to correspond the predicted values with the serial numbers of the data set, is there a way I can feed the model a random attribute set and have it predict the result


