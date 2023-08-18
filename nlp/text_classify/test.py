import torchvision.datasets as data
from torch.utils.data import DataLoader, Dataset
import torch

input_data = torch.randn(4, 10)
labels = torch.LongTensor([2, 5, 1, 9])

loss = torch.nn.CrossEntropyLoss()
l = loss(input_data, labels)
