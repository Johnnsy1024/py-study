from sklearn.naive_bayes import GaussianNB
import numpy as np
import matplotlib.pyplot as plt


X = np.random.random(size=(1000, 800))
Y = np.random.randint(low=0, high=3, size=(1000,))
m = GaussianNB()
m.fit(X, Y)

fig = plt.figure(dpi=400)
ax = fig.add_subplot(111)
colors = {0: 'green', 1: 'red'}
res = m.predict(X)
print(np.sum(np.where(res == Y, 1, 0)) / len(Y))
# ax.scatter(X[:, 0], X[:, 1], color=colors[])
