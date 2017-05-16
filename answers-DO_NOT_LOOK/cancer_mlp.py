from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

features = pd.read_csv("cancer_data.csv", index_col=False, header=0).drop("id", axis=1)
labels = features.pop("label").apply(lambda x: x/2-1)
X_train, X_test, y_train, y_test = train_test_split(features.values.astype(int), labels.values.astype(int), test_size=.33)
clf = MLPClassifier()
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)
