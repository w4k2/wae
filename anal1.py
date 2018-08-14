"""Analysis of hyperparameter."""

import helper as h
import numpy as np

# Get all hyperparameters
h.say("Establishing hyperparameters")
POST_PRUNING = h.POST_PRUNING()
THETA = h.THETA()
WEIGHT_CALCULATION = h.WEIGHT_CALCULATION()
AGING_METHOD = h.AGING_METHOD()
streams = h.streams()
base_clfs = h.base_clfs()
print(POST_PRUNING, THETA, WEIGHT_CALCULATION,AGING_METHOD,streams,base_clfs)

# Get all the results
h.say("Gathering results")
results_cube = np.load('results.npy')

# Searching hpam by hpam
h.say("Searching best for hpam")
h.say(" - post pruning")
for i, pp in enumerate(POST_PRUNING):
    for j, s in enumerate(streams):
        print(i, j, pp, s)
        resc = results_cube[i,:,:,:,j,:,:]
        ind, mean, vec, std = h.best_in_subcube(resc)
        print(ind, mean, std)
