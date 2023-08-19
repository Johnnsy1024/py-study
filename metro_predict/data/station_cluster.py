from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

m = KMeans(n_clusters=50)
coordinate = np.random.rand(1000, 2)
m.fit(coordinate)
labels = m.labels_

plt.figure(dpi=300)
plt.scatter(coordinate[:, 0], coordinate[:, 1], c=labels)
plt.legend()
plt.show()