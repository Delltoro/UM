from sklearn.model_selection import train_test_split, KFold, RepeatedKFold, RepeatedStratifiedKFold
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
import numpy as np
from sklearn.base import clone
from utils.metric import metrics
from utils.preprocess import preprocs
from utils.IO import writeResToFile,loadResFromFile,getResultsFromFileAsArray,saveTableToFile
from utils.plot import generateChart
import pandas
from datasets.dataUrls import dataURL


x = dataURL[20]
url = "D:/projekty/UM/datasets/" + x + ".dat"
dataframe = pandas.read_csv(url)
array = dataframe.values
tmp = array[:, -1]
tmp2 = tmp == 'positive'
X = array[:, :-1]
y = tmp2.astype(int)

# drzewo klasyfikacyjne z domyślnymi wartościami parametrów
clf = ExtraTreeClassifier(random_state=1410)


# wielokrotna 5krotna walidacja krzyzowa (10x5)
rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=2, random_state=42)
scores = np.zeros((len(preprocs), 5 * 2, len(metrics)))

for fold_id, (train, test) in enumerate(rskf.split(X, y)):
    for preproc_id, preproc in enumerate(preprocs):
        clf = clone(clf)

        if preprocs[preproc] == None:
            X_train, y_train = X[train], y[train]
        else:
            X_train, y_train = preprocs[preproc].fit_resample(X[train], y[train])

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X[test])

        for metric_id, metric in enumerate(metrics):
            scores[preproc_id, fold_id, metric_id] = metrics[metric](y[test], y_pred)

# Save scores to a file
writeResToFile(scores)

# Load scores from file
scores = loadResFromFile()

# Results table
table = getResultsFromFileAsArray(scores)
print(table)
# Save table to a file
saveTableToFile(table)

generateChart(scores)

