from sklearn import datasets
import numpy as np
from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler


# StandardScaler execute through example axis, Normalizer execute through feature axis

def compare_between_standard(x: np.array):
    standard_scaler = StandardScaler()
    standard_scaler.fit(x)  # Calculate the  mean and std value through dim 0
    x = standard_scaler.transform(x)
    print(x)

    print('-----------------------')
    normalizer = Normalizer(norm='l2')
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(x)
    normalizer.fit(x)
    x = normalizer.transform(x)
    print(x)

    print('-----------------------')
    min_max_scaler = MinMaxScaler()
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(x)
    min_max_scaler.fit(x)
    x = min_max_scaler.transform(x)
    print(x)


