# wae

Aging: constant
PP: True
Theta: .1

EvaluateInterleavedTestThenTrain -l (meta.AccuracyUpdatedEnsemble1 -l bayes.NaiveBayes -n 5.0 -r 10.0) -s (ArffFileStream -f /Users/xehivs/Documents/science/research/wae/streams/sd_s_hyp_r1_s_hyp_r2.arff) -e (WindowClassificationPerformanceEvaluator -w 500) -i 100000 -f 500 -q 500 -d /Users/xehivs/Desktop/abcd.csv
