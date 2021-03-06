import os

import numpy as np
from sklearn import metrics

from cobras_ts.cobras_kshape import COBRAS_kShape
from cobras_ts.commandlinequerier import CommandLineQuerier

ucr_path = '/home/toon/Downloads/UCR_TS_Archive_2015'
dataset = 'ECG200'
budget = 100

data = np.loadtxt(os.path.join(ucr_path,dataset,dataset + '_TEST'), delimiter=',')
series = data[:,1:]
labels = data[:,0]

clusterer = COBRAS_kShape(series, CommandLineQuerier(), budget)
clustering, intermediate_clusterings, runtimes, ml, cl = clusterer.cluster()

print(metrics.adjusted_rand_score(clustering.construct_cluster_labeling(),labels))
















