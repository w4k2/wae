import helper as h
import numpy as np
import matplotlib.pyplot as plt
import csv

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

bestres = results_cube[0,0,1,1,:,:]

print("Compare with others")
print(bestres.shape)
for j, db in enumerate(streams):
    print(db)
    csv_data = np.zeros((199, 5))
    csv_data[:,0] = [i*500 for i in range(199)]
    csv_data[:,1] = bestres[j,0,:]
    for i, m in enumerate(["AUE", "AWE", "DWM"]):
        print(m)
        fname = "cmp/%s_%s.csv" % (m, db)
        print(fname)

        datafile = open(fname, 'r')
        datareader = csv.reader(datafile)
        data = []
        for row in datareader:
            data.append(row[4])
        data = np.array(data[1:-1]).astype(float)
        print(data.shape)
        csv_data[:,2+i] = data/100

        #df = pd.read_csv(fname, engine='c', names=None)


    np.savetxt("summaries/cmp_%s" % db, csv_data, fmt='%.3f', delimiter=',')


# PP impact
print("Analyze post pruning impact")
for j, db in enumerate(streams):
    csv_data = np.zeros((199, 3))
    csv_data[:,0] = [i*500 for i in range(199)]
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
        csv_data[:,i+1] = mres

        plt.plot(mres, label=pp)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/pp%i.png" % j)
    plt.clf()
    print(csv_data)
    np.savetxt("summaries/pp_%s" % db, csv_data, fmt='%.3f', delimiter=',')
    print("summaries/pp_%s" % db)

# Theta impact
print("Analyze theta impact")
for j, db in enumerate(streams):
    print(j, db)
    csv_data = np.zeros((199, 6))
    csv_data[:,0] = [i*500 for i in range(199)]
    plt.figure(figsize=(10,5))
    plt.title("Theta impact on %s" % db)
    plt.ylim((0,1))
    plt.ylabel('Accuracy')
    plt.xlabel('Samples')
    plt.xticks(np.arange(0,201,20), [i*500 for i in range(0,201,20)])
    plt.grid(color='gray', linestyle='--', linewidth=.25)
    for i, t in enumerate(THETA):
        print(i, t)
        resc = results_cube[:,i,:,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        print(mres.shape)
        csv_data[:,i+1] = mres

        plt.plot(mres, label=t)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/t%i.png" % j)
    plt.clf()
    np.savetxt("summaries/t_%s" % db, csv_data, fmt='%.3f', delimiter=',')
    print("summaries/t_%s" % db)

# Weight impact
print("Analyze weight impact")
for j, db in enumerate(streams):
    print(j, db)
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
        print(i, pp)
        resc = results_cube[:,:,i,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        csv_data[:,i+1] = mres
        print(mres.shape)

        plt.plot(mres, label=w)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/w%i.png" % j)
    plt.clf()
    np.savetxt("summaries/w_%s" % db, csv_data, fmt='%.3f', delimiter=',')

# Aging impact
print("Analyze aging impact")
for j, db in enumerate(streams):
    print(j, db)
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
        print(i, pp)
        resc = results_cube[:,:,i,:,j,:,:]
        mres = np.mean(resc, axis=(0,1,2,3))
        print(mres.shape)
        csv_data[:,i+1] = mres

        plt.plot(mres, label=a)

    plt.legend(bbox_to_anchor=(.125, .15))
    plt.savefig("analysis/a%i.png" % j)
    plt.clf()
    np.savetxt("summaries/a_%s" % db, csv_data, fmt='%.3f', delimiter=',')
