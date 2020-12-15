import numpy as np
import pandas as pd
from utils.staticText import preprocs_list,metrics_list

def writeResToFile(scores):
    np.save("findings/results", scores)
    f = open("findings/scores.txt", "w")
    f.write(str(scores))
    f.close()

def loadResFromFile():
    scores = np.load("findings/results.npy")
    scores = np.mean(scores, axis=1).T
    return scores

def getResultsFromFileAsArray(scores):
    dataFromFile = list(scores)
    num = np.array(dataFromFile)
    table = pd.DataFrame(num, columns=[preprocs_list], index=[metrics_list])
    return table

def saveTableToFile(table):
    f = open("findings/table.txt", "w")
    f.write(str(table))
    f.close()