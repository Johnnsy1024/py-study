from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

data = load_iris()
t = DecisionTreeClassifier()
t.fit(data.data, data.target)
# print(t._parameter_constraints)
print(t.feature_importances_)