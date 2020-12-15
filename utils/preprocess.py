
from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler, CondensedNearestNeighbour, ClusterCentroids

preprocs_list = ["None", "ROS", "SMOTE", "RUS", "CC"]

#metody preprocessingu
preprocs = {
    'none': None,
    'ros' : RandomOverSampler(random_state=1410),
    'smote' : SMOTE(random_state=1410),
    'rus' : RandomUnderSampler(random_state=1410),
    #'cnn' : CondensedNearestNeighbour(random_state=1410)
    'cc' : ClusterCentroids(random_state=1410)
}
