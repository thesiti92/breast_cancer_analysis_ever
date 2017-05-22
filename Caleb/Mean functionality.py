from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

def evaluator(file,endString):
    adder = 0
    count = 0
    while count < 10:
        df = pd.read_csv(file, index_col=False, header=0).drop("id", axis=1)
        labels = df.pop("label").apply(lambda x: x/2-1)
        X_train, X_test, y_train, y_test = train_test_split(df.values.astype(int), labels.values.astype(int), test_size=.33)
        clf = MLPClassifier()
        clf.fit(X_train, y_train)
        clf.score(X_test, y_test)
        adder = adder + clf.score(X_test, y_test)
        count = count + 1
    print("Here is the average")
    print(str(adder/count))
    print(endString)

evaluator("clump_thickness.csv", "End of clump thickness data")
evaluator("size_uniformity.csv","End of size uniformity data")
evaluator("shape_uniformity.csv","End of shape uniformity data")
evaluator()
evaluator()
evaluator()
evaluator()
evaluator()
evaluator()



objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2, 1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()'''