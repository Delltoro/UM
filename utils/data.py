import pandas as pd

url = "D:/StudiaMagSem2/uczenieMaszynProjekt/glass1.dat"
dataframe = pd.read_csv(url)
array = dataframe.values
tmp = array[:, -1]
tmp2 = tmp == 'positive'

X = array[:, :-1]
y = tmp2.astype(int)


dataset = 'ecoli-0-1-4-6_vs_5'
dataset = np.genfromtxt("%s.csv" % (dataset), delimiter=",")
X = dataset[:, :-1]
y = dataset[:, -1].astype(int)