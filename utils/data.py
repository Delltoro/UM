import pandas as pd

dataURL = [
    'glass1',
    'ecoli-0_vs_1',
    'wisconsin.dat',
    'pima',
    'iris0',
    'yeast-2_vs_4',
    'yeast-0-5-6-7-9_vs_4',
    'vowel0',
    'glass-0-1-6_vs_2',
    'glass2',
    'shuttle-c0-vs-c4',
    'ecoli-0-1_vs_5',
    'glass-0-1-4-6_vs_2',
    'ecoli-0-1-4-7_vs_5-6',
    'cleveland-0_vs_4',
    'ecoli-0-1-4-6_vs_5',
    'kddcup-land_vs_satan',
    'kr-vs-k-zero_vs_fifteen',
    'poker-8-9_vs_5',
    'poker-8_vs_6',
    'kddcup-rootkit-imap_vs_back'
]


def loadData():
    url = "D:/StudiaMagSem2/uczenieMaszynProjekt/glass1.dat"
    dataframe = pd.read_csv(url)
    array = dataframe.values
    tmp = array[:, -1]
    tmp2 = tmp == 'positive'

    X = array[:, :-1]
    y = tmp2.astype(int)

