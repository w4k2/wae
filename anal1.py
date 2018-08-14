"""Analysis of hyperparameter."""
import helper as h
import numpy as np
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
print("& \\multicolumn{10}{c}{\\bfseries\\scriptsize Mean accuracy and standard deviation for given method parameter}\\\\")
print("\\scriptsize\\bfseries Value &")
for i, s in enumerate(streams):
    print("\\multicolumn{1}{c%s}{\\scriptsize\\bfseries %s} %s" % (
        "|" if i != len(streams) - 1 else "",
        TRANSLATED[i],
        "&" if i != len(streams) - 1 else "\\\\"
    ))


# Get all the results
results_cube = np.load('results.npy')

# Searching hpam by hpam
cs = h.colors()

h.say(" - post pruning")
print("\\midrule\\multicolumn{11}{c}{\\bfseries\\scriptsize Usage of post-pruning}\\\\")
local_tab = np.zeros((len(streams), len(POST_PRUNING), 2))
for j, s in enumerate(streams):
    #h.prepfig("Post pruning impact on %s" % s)
    for i, pp in enumerate(POST_PRUNING):
        resc = results_cube[i,:,:,:,j,:,:]
        mean, vec, std = h.mean_in_subcube(resc)
        local_tab[j,i,:] = (mean, std)
        #plt.plot(vec, label=pp, c=cs[i])
        #plt.plot(np.ones(199) * mean, linestyle='-', lw=.5, c=cs[i][:3])
    #plt.savefig("pap/pp_%i_%i.png" % (j, i))
    #plt.close('all')
h.present_loctab(local_tab, POST_PRUNING)

h.say(" - theta")
print("\\midrule\\multicolumn{11}{c}{\\bfseries\\scriptsize Used theta value}\\\\")
local_tab = np.zeros((len(streams), len(THETA), 2))
for j, s in enumerate(streams):
    #h.prepfig("Theta impact on %s" % s)
    for i, t in enumerate(THETA):
        resc = results_cube[:,i,:,:,j,:,:]
        mean, vec, std = h.mean_in_subcube(resc)
        local_tab[j,i,:] = (mean, std)
        #plt.plot(vec, label=t, c=cs[i])
        #plt.plot(np.ones(199) * mean, linestyle='-', lw=.5, c=cs[i][:3])
    #plt.savefig("pap/t_%i_%i.png" % (j, i))
    #plt.close('all')
h.present_loctab(local_tab, THETA)

h.say(" - weight calculation")
print("\\midrule\\multicolumn{11}{c}{\\bfseries\\scriptsize Weight calculation method}\\\\")
local_tab = np.zeros((len(streams), len(WEIGHT_CALCULATION), 2))
for j, s in enumerate(streams):
    #h.prepfig("Weight calculation method impact on %s" % s)
    for i, t in enumerate(WEIGHT_CALCULATION):
        resc = results_cube[:,:,i,:,j,:,:]
        mean, vec, std = h.mean_in_subcube(resc)
        local_tab[j,i,:] = (mean, std)
        #plt.plot(vec, label=t, c=cs[i])
        #plt.plot(np.ones(199) * mean, linestyle='-', lw=.5, c=cs[i][:3])
    #plt.savefig("pap/w_%i_%i.png" % (j, i))
    #plt.close('all')
h.present_loctab(local_tab, WEIGHT_CALCULATION)

h.say(" - aging calculation")
print("\\midrule\\multicolumn{11}{c}{\\bfseries\\scriptsize Aging method}\\\\")
local_tab = np.zeros((len(streams), len(AGING_METHOD), 2))
for j, s in enumerate(streams):
    #h.prepfig("Aging method impact on %s" % s)
    for i, t in enumerate(AGING_METHOD):
        resc = results_cube[:,:,:,i,j,:,:]
        mean, vec, std = h.mean_in_subcube(resc)
        local_tab[j,i,:] = (mean, std)
        #plt.plot(vec, label=t, c=cs[i])
        #plt.plot(np.ones(199) * mean, linestyle='-', lw=.5, c=cs[i][:3])
    #plt.savefig("pap/w_%i_%i.png" % (j, i))
    #plt.close('all')
h.present_loctab(local_tab, AGING_METHOD)

print("\\bottomrule\\end{tabular}")
