import os
import helper as h

streams = h.streams()

learners = {
    "AUE": "(meta.AccuracyUpdatedEnsemble1 -l bayes.NaiveBayes -n 5.0 -r 10.0)",
    "AWE": "(meta.AccuracyWeightedEnsemble -l bayes.NaiveBayes -n 5.0 -r 10.0)",
    "DWM": "(meta.DynamicWeightedMajority)",
}



form = "EvaluateInterleavedTestThenTrain -l %s -s (ArffFileStream -f streams/%s) -e (WindowClassificationPerformanceEvaluator -w 500) -i 100000 -f 500 -q 500 -d cmp/%s.csv"

for key in learners:
    for stream in streams:
        learner = learners[key]
        content = form % (learner, stream, ("%s_%s" % (key, stream)))
        cmd = "java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask \"%s\"" % content
        os.system(cmd)
