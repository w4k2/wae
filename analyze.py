import helper as h
import numpy as np
import matplotlib.pyplot as plt
import csv

# Prepare
POST_PRUNING = h.POST_PRUNING()
THETA = h.THETA()
WEIGHT_CALCULATION = h.WEIGHT_CALCULATION()
AGING_METHOD = h.AGING_METHOD()
streams = h.streams()
base_clfs = h.base_clfs()

# Load
results_cube = np.load('results.npy')
print(results_cube.shape)

bestres = results_cube[0,0,1,1,:,:]

print("Compare with others")
for j, db in enumerate(streams):
    csv_data = np.zeros((199, 5))

    resc = results_cube[:,:,:,:,j,:,:]
    ind, mean, vec, std = h.best_in_subcube(resc)

    csv_data[:,0] = [i*500 for i in range(199)]
    csv_data[:,1] = vec # bestres[j,0,:]

    for i, m in enumerate(["AUE", "AWE", "DWM"]):
        fname = "cmp/%s_%s.csv" % (m, db)

        datafile = open(fname, 'r')
        datareader = csv.reader(datafile)
        data = []
        for row in datareader:
            data.append(row[4])
        data = np.array(data[1:-1]).astype(float)
        csv_data[:,2+i] = data/100

    np.savetxt("summaries/cmp_%s" % db, csv_data, fmt='%.3f', delimiter=',')

# PP impact
print("Analyze post pruning impact")
for j, db in enumerate(streams):
    csv_data = np.zeros((199, 3))
    csv_data[:,0] = [i*500 for i in range(199)]
    plt.figure(figsize=(10,5))
    plt.title("Post pruning impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, pp in enumerate(POST_PRUNING):

        resc = results_cube[i,:,:,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))

        csv_data[:,i+1] = mres

        plt.plot(mres, label=pp)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/pp%i.png" % j)
    plt.clf()

    np.savetxt("summaries/pp_%s" % db, csv_data, fmt='%.3f', delimiter=',')


# Theta impact
print("Analyze theta impact")
for j, db in enumerate(streams):

    csv_data = np.zeros((199, len(THETA) +1))
    csv_data[:,0] = [i*500 for i in range(199)]
    plt.figure(figsize=(10,5))
    plt.title("Theta impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, t in enumerate(THETA):

        resc = results_cube[:,i,:,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))

        csv_data[:,i+1] = mres

        plt.plot(mres, label=t)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/t%i.png" % j)
    plt.clf()
    np.savetxt("summaries/t_%s" % db, csv_data, fmt='%.3f', delimiter=',')


# Weight impact
print("Analyze weight impact")
for j, db in enumerate(streams):

    csv_data = np.zeros((199, 5))
    csv_data[:,0] = [i*500 for i in range(199)]
    plt.figure(figsize=(10,5))
    plt.title("Weight impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, w in enumerate(WEIGHT_CALCULATION):

        resc = results_cube[:,:,i,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        csv_data[:,i+1] = mres


        plt.plot(mres, label=w)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/w%i.png" % j)
    plt.clf()
    np.savetxt("summaries/w_%s" % db, csv_data, fmt='%.3f', delimiter=',')

# Aging impact
print("Analyze aging impact")
for j, db in enumerate(streams):

    csv_data = np.zeros((199, 4))
    csv_data[:,0] = [i*500 for i in range(199)]

    plt.figure(figsize=(10,5))
    plt.title("Aging impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, a in enumerate(AGING_METHOD):

        resc = results_cube[:,:,i,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))

        csv_data[:,i+1] = mres

        plt.plot(mres, label=a)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/a%i.png" % j)
    plt.clf()
    np.savetxt("summaries/a_%s" % db, csv_data, fmt='%.3f', delimiter=',')
