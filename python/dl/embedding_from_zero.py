import torch
import torch.nn as nn
import numpy as np


def softmax(x: np.array, dim=0):
    total = np.sum(np.exp(x), axis=-1, keepdims=True)
    res = np.exp(x) / total
    return res

class Embedding(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        np.random.seed(1)
        self.embedding_matrix = np.random.random(size=(vocab_size, embedding_dim))

    def forward(self, input_x):
        return self.embedding_matrix[input_x, :]


embedding = Embedding(10, 4)
input_x_1 = [[3, 2, 4, 1, 7], [3, 2, 5, 2, 7]]
print('embedding层参数')
print(embedding.embedding_matrix)
print('input_x_1的embedding向量')
print(embedding(input_x_1))
print('相似度为')
familiarity = np.matmul(embedding(input_x_1)[0], embedding(input_x_1)[1].T)
print(familiarity)
print(np.concatenate([familiarity, familiarity], axis=0))
# input_x_2 = [3, 2, 5, 2, 7]
# print('input_x_2的embedding向量')
# print(embedding(input_x_2))
print('softmax result')
print('--------------------')
# print(softmax(familiarit, 1))
# print(softmax(np.matmul(embedding(input_x_1), embedding(input_x_2).T), dim=-1))
# print('softmax sum')