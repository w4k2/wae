"""Helper functions."""
from os import listdir
from sklearn import naive_bayes, neural_network, tree, neighbors, svm
import numpy as np

np.set_printoptions(precision=3)

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

def say(string):
    print("# %s" % string)

def best_in_subcube(resc):
    """Returns indices of best, mean best, best vector and best std."""
    flattened_accuracy = np.mean(resc, axis = -1)
    best_indices = np.unravel_index(flattened_accuracy.argmax(),
                                    flattened_accuracy.shape)

    max = np.max(flattened_accuracy)

    best_vector = resc[best_indices]

    mean_best = np.mean(best_vector)
    std_best = np.std(best_vector)

    return best_indices, mean_best, best_vector, std_best
