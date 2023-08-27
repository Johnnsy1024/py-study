from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt


X = np.random.random(size=(1000, 100))
Y = np.random.randint(low=0, high=2, size=(1000,))
m = SVC(C=2)
m.fit(X, Y)

res = m.predict(X)
print(np.sum(np.where(res == Y, 1, 0)) / len(Y))
# ax.scatter(X[:, 0], X[:, 1], color=colors[])

