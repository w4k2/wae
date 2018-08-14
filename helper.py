"""Helper functions."""
from os import listdir
from sklearn import naive_bayes, neural_network, tree, neighbors, svm
import numpy as np
import matplotlib.pyplot as plt

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
    return (.0, .1, .3, .5, .7, .9)

def POST_PRUNING():
    return (True, False)

def say(string):
    print("%%# %s" % string)

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

def mean_in_subcube(resc):
    """mean best, best vector and best std."""
    mean_vector = np.mean(resc, axis=(0,1,2,3))

    mean = np.mean(mean_vector)
    std = np.std(mean_vector)

    return mean, mean_vector, std


def prepfig(title):
    plt.figure(figsize=(7,3))
    plt.title(title)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)

def colors():
    return (
        (.7,.3,.3,.75),
        (.3,.7,.3,.75),
        (.3,.3,.7),
        (.7,.3,.7),
        (.7,.7,.3),
        (.3,.7,.7),
    )

def present_loctab(loctab, leads):
    a, b, _ = loctab.shape
    #print(loctab.shape)
    for i in range(b):
        print("\\scriptsize\\emph{%s} & " % str(leads[i]).replace('_',' '), end='')
        for j in range(a):
            maxind = np.argmax(loctab[j,:,0])
            mean = loctab[j,i,0]
            std = loctab[j,i,1]
            print("%s %.3f %s (%.2f)" % (
                "\\B " if i == maxind else "",
                mean,
                "\\B " if i == maxind else "",
                std
            ), end='')
            if j != a-1:
                print(" & ", end='')
        print(' \\\\')


def translated():
    return ['SD H1R1', 'SD H3R3', 'SD R1R2', 'ID R1R3', 'SD R2R3', 'SD R1R3', 'SD H1H3', 'SD H2R2', 'SD H2H3', 'SD H1H2']
