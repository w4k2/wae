from os import listdir
from sklearn import naive_bayes, neural_network, tree, neighbors, svm

def streams():
    return listdir("streams")

def base_clfs():
    return {
        #"DT": tree.DecisionTreeClassifier(),
        #"NB": naive_bayes.GaussianNB(),
        #"SVC": svm.SVC(probability=True),
        #"MLP": neural_network.MLPClassifier(),
        "kNN": neighbors.KNeighborsClassifier()
    }
