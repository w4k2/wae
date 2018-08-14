"""Analysis of hyperparameter."""
import helper as h
import numpy as np
import csv
import matplotlib.pyplot as plt

# Get all hyperparameters
POST_PRUNING = h.POST_PRUNING()
THETA = h.THETA()
WEIGHT_CALCULATION = h.WEIGHT_CALCULATION()
AGING_METHOD = h.AGING_METHOD()
streams = h.streams()
base_clfs = h.base_clfs()
TRANSLATED = h.translated()
# print(POST_PRUNING, THETA, WEIGHT_CALCULATION,AGING_METHOD,streams,base_clfs)

# Print table header
print("\\begin{tabular}{p{3cm}|c|c|c|c|c|c|c|c|c|c}")
print("\\toprule")
print("& \\multicolumn{10}{c}{\\bfseries\\scriptsize Mean accuracy and standard deviation for given method}\\\\")
print("\\scriptsize\\bfseries Method &")
for i, s in enumerate(streams):
    print("\\multicolumn{1}{c%s}{\\scriptsize\\bfseries %s} %s" % (
        "|" if i != len(streams) - 1 else "",
        TRANSLATED[i],
        "&" if i != len(streams) - 1 else "\\\\"
    ))


# Get all the results
results_cube = np.load('results.npy')
# Get the best

# Searching hpam by hpam
cs = h.colors()

h.say(" - methods comparison")
print("\\midrule\\multicolumn{11}{c}{\\bfseries\\scriptsize Usage of post-pruning}\\\\")
local_tab = np.zeros((len(streams), 4, 2))
for j, s in enumerate(streams):
    resc = results_cube[:,:,:,:,j,:,:]
    # print(np.mean(resc))
    ind, mean, vec, std = h.best_in_subcube(resc)
    local_tab[j,0,:] = (mean, std)
    h.prepfig("Post pruning impact on %s" % s)
    plt.plot(vec, label="WAE", c=cs[0])
    plt.plot(np.ones(199) * mean, linestyle='-', lw=.5, c=cs[0][:3])

    for i, m in enumerate(["AUE", "AWE", "DWM"]):
        fname = "cmp/%s_%s.csv" % (m, s)
        datafile = open(fname, 'r')
        datareader = csv.reader(datafile)
        data = []
        for row in datareader:
            data.append(row[4])
        data = np.array(data[1:-1]).astype(float)
        metvec = data/100
        mean, std = np.mean(metvec), np.std(metvec)
        local_tab[j,i+1,:] = (mean, std)


        plt.plot(metvec, label=m, c=cs[i+1])
        plt.plot(np.ones(199) * mean, linestyle='-', lw=.5, c=cs[i+1][:3])
    plt.savefig("pap/cmp_%i_%i.png" % (j, i))
    plt.close('all')
h.present_loctab(local_tab, ["WAE", "AUE", "AWE", "DWM"])

print("\\bottomrule\\end{tabular}")
