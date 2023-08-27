from sklearn.preprocessing import Normalizer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.randn(10, 10)
sns.heatmap(x)
plt.show()
# Normalizer will normalize the data from dim 1 which means normalize every record through features
normalizer = Normalizer(copy=False)
normalizer.transform(x)
sns.heatmap(x)
plt.show()
