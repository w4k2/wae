"""Helper functions."""
from os import listdir
from sklearn import naive_bayes, neural_network, tree, neighbors, svm


def streams():
    """List of streams to analuze."""
    return listdir("streams")


def base_clfs():
    """List of used base classifiers."""
    return {
        #"DT": tree.DecisionTreeClassifier(),
        "NB": naive_bayes.GaussianNB(),
        #"SVC": svm.SVC(probability=True),
        #"MLP": neural_network.MLPClassifier(),
        #"kNN": neighbors.KNeighborsClassifier()
    }
