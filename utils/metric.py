from strlearn.metrics import recall, precision, specificity, f1_score, geometric_mean_score_1, balanced_accuracy_score

metrics_list = ["Recall", "Precision", "Specificity", "F1", "G-mean", "BAS"]
#metryki bazowe & zagregowane
metrics = {
    'recall' : recall,
    'precision' : precision,
    'specificity' : specificity,
    'f1' : f1_score,
    'g-mean' : geometric_mean_score_1,
    'bas' : balanced_accuracy_score
}
