from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

count = 0
while count < 10:
    df = pd.read_csv("clump_thickness.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf = MLPClassifier()
    clf.fit(X_train, y_train)
    print clf.score(X_test, y_test)
    count = count + 1
print("End of clump thickness data")

count = 0
while count < 10:
    df = pd.read_csv("size_uniformity.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf1 = MLPClassifier()
    clf1.fit(X_train, y_train)
    print clf1.score(X_test, y_test)
    count = count + 1
print("End of size uniformity data")

count = 0
while count < 10:
    df = pd.read_csv("shape_uniformity.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    print clf2.score(X_test, y_test)
    count = count + 1
print("End of shape uniformity data")

count = 0
while count < 10:
    df = pd.read_csv("marginal_adhesion.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    print clf2.score(X_test, y_test)
    count = count + 1
print("End of marginal adhesion data")

count = 0
while count < 10:
    df = pd.read_csv("epithelial_size.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    print clf2.score(X_test, y_test)
    count = count + 1
print("End of epithelial size data")

count = 0
while count < 10:
    df = pd.read_csv("bare_nuclei.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    print clf2.score(X_test, y_test)
    count = count + 1
print("End of bare nuclei data")

count = 0
while count < 10:
    df = pd.read_csv("bland_chromatin.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    print clf2.score(X_test, y_test)
    count = count + 1
print("End of bland chromatin data")

count = 0
while count < 10:
    df = pd.read_csv("normal_nucleoli.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    print clf2.score(X_test, y_test)
    count = count + 1
print("End of normal nucleoli data")

count = 0
while count < 10:
    df = pd.read_csv("mitosis.csv", index_col=False, header=0).drop("id", axis=1)
    labels = df.pop("label").apply(lambda x: x/2-1)
    X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
    clf2 = MLPClassifier()
    clf2.fit(X_train, y_train)
    print clf2.score(X_test, y_test)
    count = count + 1
print("End of mitosis data")

