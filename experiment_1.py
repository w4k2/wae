import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore')
import helper as h
import numpy as np
import strlearn as sl
import matplotlib.pyplot as plt

# Prepare
base_clfs = h.base_clfs()
streams = h.streams()
#streams = ["toyset.arff"]

WEIGHT_CALCULATION = ('same_for_each', 'kuncheva', 'bell_curve',
                      'proportional_to_accuracy_related_to_whole_ensemble')
AGING_METHOD = ('weights_proportional', 'constant', 'gaussian')
THETA = (.1,.3,.5,.7,.9)
POST_PRUNING = (True, False)

# Process
for post_pruning in POST_PRUNING:
    for theta in THETA:
        for weight_calculation_method in WEIGHT_CALCULATION:
            for aging_method in AGING_METHOD:
                for stream in streams:
                    print(stream)
                    # Loading stream
                    X, y = sl.utils.load_arff("streams/%s" % stream)
                    for base_clfn in base_clfs:
                        base_clf = base_clfs[base_clfn]

                        resname = "%s_%s_%s_%s_%s_%.1f" % (
                            stream[:-5], base_clfn, post_pruning,
                            weight_calculation_method,
                            aging_method, theta
                        )

                        wae = sl.ensembles.WAE(
                            base_clf=base_clf,
                            post_pruning=post_pruning,
                            theta=theta,
                            weight_calculation_method=weight_calculation_method,
                            aging_method=aging_method)
                        print(resname)
                        learner = sl.Learner(X, y, wae)
                        learner.run()

                        plt.plot(learner.score_points,learner.scores)
                        plt.title(stream[:-5])
                        plt.ylim([0,1])
                        plt.savefig("figures/%s.png" % resname)
                        plt.clf()
                        np.savetxt("results/%s.csv" % resname,
                                   learner.scores, delimiter=',', fmt='%.3f')
