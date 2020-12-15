#import pi
from sklearn import datasets
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, KFold, RepeatedKFold, RepeatedStratifiedKFold
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from numpy import unique
from sklearn.base import clone
from utils.metric import metrics
from utils.preprocess import preprocs
from utils.IO import writeResToFile,loadResFromFile,getResultsFromFileAsArray,saveTableToFile
from utils.plot import generateChart
from datasets.dataUrls import dataURL

from collections import Counter
from imblearn.datasets import fetch_datasets


#Generate a random n-class classification problem.
X, y = datasets.make_classification(
    weights=[0.8, 0.2],
    n_samples=100,
    n_features=2,
    n_informative=1,
    n_repeated=0,
    n_redundant=0,
    flip_y=.05,
    random_state=1234,
    n_clusters_per_class=1
)

ecoli = fetch_datasets()['ecoli']
ecoli.data.shape
array = ecoli.values



#drzewo klasyfikacyjne z domyślnymi wartościami parametrów
clf = DecisionTreeClassifier(random_state=1410)


#podzial na zbior uczacy-70% i testowy-30% (najprostsza metoda: temporary)
'''X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=.30,
    random_state=1234
)'''

#wielokrotna 5krotna walidacja krzyzowa (10x5)
rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=2, random_state=42)
scores = np.zeros((len(preprocs), 5*2, len(metrics)))

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
## Loop to plot
#for row in range(0, len(table.index)):
#    print(table[0])
#    generateChart2(scores,row=row, title='grou1', color='red')


