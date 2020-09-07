import numpy as a
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
import pandas as pd

data = pd.read_csv('ClusterPlot.csv')
ds = pd.DataFrame(data, columns=['V1','V2']).to_numpy()

ms=MeanShift()
ms.fit(ds)
labels = ms.labels_
#cluster_centers = ms.cluster_centers_

n_cluster_ = len(a.unique(labels))

print("Number of clusters: ",n_cluster_)
colors = ['r.','m.','c.','y','m.']

for i in range(len(ds)):
    plt.plot(ds[i][0], ds[i][1],colors[labels[i]],markersize=10)
plt.show()