from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='crhodes21', api_key='U4jIV8iTZLBAOUo9i3U1')

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
    #print("Here is the average")
    #print(str(adder/count))
    #print(endString)
    return(adder/count)


evaluator("main_cancer_data.csv","End of all attribute data")
evaluator("clump_thickness.csv", "End of clump thickness data")
evaluator("size_uniformity.csv","End of size uniformity data")
evaluator("shape_uniformity.csv","End of shape uniformity data")
evaluator("marginal_adhesion.csv","End of marginal adhesion data")
evaluator("epithelial_size.csv","End of epithelial size data")
evaluator("bare_nuclei.csv","End of bare nuclei data")
evaluator("bland_chromatin.csv","End of bland chromatin data")
evaluator("normal_nucleoli.csv","End of normal nucleoli data")
evaluator("mitosis.csv","End of mitosis data")

MeanArray = []
MeanArray.append(evaluator("main_cancer_data.csv","End of all attribute data"))
MeanArray.append(evaluator("clump_thickness.csv", "End of clump thickness data"))
MeanArray.append(evaluator("size_uniformity.csv","End of size uniformity data"))
MeanArray.append(evaluator("shape_uniformity.csv","End of shape uniformity data"))
MeanArray.append(evaluator("marginal_adhesion.csv","End of marginal adhesion data"))
MeanArray.append(evaluator("epithelial_size.csv","End of epithelial size data"))
MeanArray.append(evaluator("bare_nuclei.csv","End of bare nuclei data"))
MeanArray.append(evaluator("bland_chromatin.csv","End of bland chromatin data"))
MeanArray.append(evaluator("normal_nucleoli.csv","End of normal nucleoli data"))
MeanArray.append(evaluator("mitosis.csv","End of mitosis data"))
print(MeanArray)

data = [go.Bar(
            x=['All Attributes', 'Clump Thickness', 'Size Uniformity', 'Shape Uniformity', 'Marginal Adhesion',
               'Epithelial Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','mitosis'],
            y = MeanArray
    )]

py.iplot(data, filename='Attribute-Bar-Graph')

'''
objects = ('All Attributes', 'Clump Thickness', 'Size Uniformity', 'Shape Uniformity', 'Marginal Adhesion', 'Epithelial Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli,'Mitosis')
y_pos = np.arange(len(objects))
MeanArray = []

plt.bar(y_pos, MeanArray, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Model Accuracy')
plt.xlabel('Attribute Type')
plt.title('Attribute Correlation to Classification Accuracy')

plt.show()'''