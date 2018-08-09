"""Experiment of WAE."""
import warnings
import helper as h
import numpy as np
import strlearn as sl
import matplotlib.pyplot as plt
import os.path

warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore')

# Prepare
base_clfs = h.base_clfs()
streams = h.streams()
#streams = ["toyset.arff"]

WEIGHT_CALCULATION = ('same_for_each', 'kuncheva',
                      'pta_related_to_whole',
                      'bell_curve')

AGING_METHOD = ('weights_proportional', 'constant',
                'gaussian')
THETA = (.1, .3, .5, .7, .9)
POST_PRUNING = (True, False)

count = len(streams) * len(WEIGHT_CALCULATION) * len(AGING_METHOD) * len(THETA) * len(POST_PRUNING) * len(base_clfs)

# Process
for post_pruning in POST_PRUNING:
    for theta in THETA:
        for weight_calculation_method in WEIGHT_CALCULATION:
            for aging_method in AGING_METHOD:
                for stream_n in streams:
                    # Loading stream
                    for base_clfn in base_clfs:
                        resname = "%s_%s_%s_%s_%s_%.1f" % (
                            stream_n[:-5], base_clfn, post_pruning,
                            weight_calculation_method,
                            aging_method, theta
                        )
                        print("[%i left] %s" % (count, resname), end='', flush=True)

                        if not os.path.isfile("results/%s.csv" % resname):

                            stream = sl.utils.ARFF("streams/%s" % stream_n)
                            base_clf = base_clfs[base_clfn]
                            print(".", end='', flush=True)

                            wae = sl.ensembles.WAE(
                                post_pruning=post_pruning,
                                theta=theta,
                                weight_calculation_method=weight_calculation_method,
                                aging_method=aging_method,
                                ensemble_size=5)
                            print(".", end='', flush=True)

                            wae.set_base_clf(base_clf)
                            learner = sl.learners.TestAndTrain(stream, wae)
                            print(".", end='', flush=True)
                            learner.run()
                            print(".", end='', flush=True)

                            plt.plot(learner.score_points, learner.scores)
                            plt.title(stream_n[:-5])
                            plt.ylim([0, 1])
                            plt.savefig("figures/%s.png" % resname)
                            plt.clf()
                            np.savetxt("results/%s.csv" % resname,
                                       learner.scores, delimiter=',', fmt='%.3f')
                            print(".", end='', flush=True)

                        count -= 1
                        print(".")
