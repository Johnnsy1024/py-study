"""
通过计算数据矩阵的协方差矩阵，然后得到协方差矩阵的特征值特征向量，选择特征值最大(即方差最大)的k个特征所对应的特征向量组成的矩阵。
这样就可以将数据矩阵转换到新的空间当中，实现数据特征的降维。
由于得到协方差矩阵的特征值特征向量有两种方法：特征值分解协方差矩阵、奇异值分解协方差矩阵
所以PCA算法有两种实现方法：基于特征值分解协方差矩阵实现PCA算法、基于SVD分解协方差矩阵实现PCA算法(区别就在于求特征值和特征向量时采用的方法)
"""

from sklearn import datasets
import numpy as np

iris = datasets.load_iris()

X = iris.data
Y = iris.target


#  手动实现PCA
def pca_from_scratch(x: np.array, k: int) -> np.array:
    """

    :param x: 原始数据集 shape:[n_sample, n_features]
    :param k: 降至的维度
    :return: 降维后的数据集
    """
    from sklearn.preprocessing import Normalizer

    cov_matrix = np.cov(x.T)  # np.cov需要传入的是[n_features, n_sample]
    eig_values, eig_vectors = np.linalg.eig(cov_matrix)
    n = Normalizer()
    eig_vectors = n.fit_transform(eig_vectors.T)
    eig_list = [(eig_values[i], eig_vectors[i]) for i in range(len(eig_values))]
    eig_list.sort(key=lambda y: y[0], reverse=True)
    eig_vector = np.array([eig_list[i][1] for i in range(len(eig_list))][:k])
    res = np.matmul(eig_vector, x.T)
    return res.T


def pca(x: np.array, k: int) -> np.array:
    from sklearn.decomposition import PCA

    p = PCA(n_components=k)
    res = p.fit_transform(x)
    return res


print(pca_from_scratch(x=X, k=2))
print('\n')
print('\n')
print('\n')
print(pca(x=X, k=2))
# from sklearn.decomposition import PCA
#
# pca = PCA(n_components=2)
# new_X = pca.fit_transform(X)
# np.testing.assert_array_equal(0.0, np.matmul(new_X[:, 0], new_X[:, 1]))
