"""Helper functions."""
from os import listdir
from sklearn import naive_bayes, neural_network, tree, neighbors, svm


def streams():
    """List of streams to analuze."""
    return listdir("streams")


def base_clfs():
    """List of used base classifiers."""
    return {
        "NB": naive_bayes.GaussianNB(),
    }

def WEIGHT_CALCULATION():
    return ('same_for_each', 'kuncheva',
                      'pta_related_to_whole',
                      'bell_curve')

def AGING_METHOD():
    return ('weights_proportional', 'constant',
                'gaussian')

def THETA():
    return (0, .1, .3, .5, .7, .9)

def POST_PRUNING():
    return (True, False)
