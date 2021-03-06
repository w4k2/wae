"""Prepare cube with collective results."""
import helper as h
import numpy as np

# Prepare
base_clfs = h.base_clfs()
streams = h.streams()

POST_PRUNING = h.POST_PRUNING()
THETA = h.THETA()
WEIGHT_CALCULATION = h.WEIGHT_CALCULATION()
AGING_METHOD = h.AGING_METHOD()

count = len(streams) * len(WEIGHT_CALCULATION) * len(AGING_METHOD) * len(THETA) * len(POST_PRUNING) * len(base_clfs)

results_cube = np.zeros((len(POST_PRUNING),
                         len(THETA),
                         len(WEIGHT_CALCULATION),
                         len(AGING_METHOD),
                         len(streams),
                         len(base_clfs),
                         199))

print(results_cube.shape)

# Process
for a, post_pruning in enumerate(POST_PRUNING):
    for b, theta in enumerate(THETA):
        for c, weight_calculation_method in enumerate(WEIGHT_CALCULATION):
            for d, aging_method in enumerate(AGING_METHOD):
                for e, stream_n in enumerate(streams):
                    # Loading stream
                    for f, base_clfn in enumerate(base_clfs):
                        resname = "%s_%s_%s_%s_%s_%.1f" % (
                            stream_n[:-5], base_clfn, post_pruning,
                            weight_calculation_method,
                            aging_method, theta
                        )
                        res = np.loadtxt("results/%s.csv" % resname,
                                         delimiter=',')
                        results_cube[a, b, c, d, e, :] = res

np.save('results', results_cube)
