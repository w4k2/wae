import helper as h
import numpy as np
import matplotlib.pyplot as plt

# Prepare
POST_PRUNING = (True, False)
THETA = (.1, .3, .5, .7, .9)
WEIGHT_CALCULATION = ('same_for_each', 'kuncheva',
                      'pta_related_to_whole',
                      'bell_curve')
AGING_METHOD = ('weights_proportional', 'constant', 'gaussian')
streams = h.streams()
base_clfs = h.base_clfs()

# Load
results_cube = np.load('results.npy')
print(results_cube.shape)

# PP impact
print("Analyze post pruning impact")
for j, db in enumerate(streams):
    # print(j, db)
    plt.figure(figsize=(10,5))
    plt.title("Post pruning impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, pp in enumerate(POST_PRUNING):
        # print(i, pp)
        resc = results_cube[i,:,:,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        # print(mres.shape)

        plt.plot(mres, label=pp)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/pp%i.png" % j)
    plt.clf()

# Theta impact
print("Analyze theta impact")
for j, db in enumerate(streams):
    print(j, db)
    plt.figure(figsize=(10,5))
    plt.title("Theta impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, t in enumerate(THETA):
        print(i, pp)
        resc = results_cube[:,i,:,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        print(mres.shape)

        plt.plot(mres, label=t)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/t%i.png" % j)
    plt.clf()

# Weight impact
print("Analyze weight impact")
for j, db in enumerate(streams):
    print(j, db)
    plt.figure(figsize=(10,5))
    plt.title("Weight impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, w in enumerate(WEIGHT_CALCULATION):
        print(i, pp)
        resc = results_cube[:,:,i,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        print(mres.shape)

        plt.plot(mres, label=w)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/w%i.png" % j)
    plt.clf()

# Aging impact
print("Analyze aging impact")
for j, db in enumerate(streams):
    print(j, db)
    plt.figure(figsize=(10,5))
    plt.title("Aging impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, a in enumerate(AGING_METHOD):
        print(i, pp)
        resc = results_cube[:,:,i,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        print(mres.shape)

        plt.plot(mres, label=a)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/a%i.png" % j)
    plt.clf()

# Weight impact
print("Analyze aging impact")
for j, db in enumerate(streams):
    print(j, db)
    plt.figure(figsize=(10,5))
    plt.title("Aging impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, a in enumerate(AGING_METHOD):
        print(i, pp)
        resc = results_cube[:,:,i,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        print(mres.shape)

        plt.plot(mres, label=a)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/a%i.png" % j)
    plt.clf()
