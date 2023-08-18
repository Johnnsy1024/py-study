import numpy as np
import torch
import os
import pickle as pkl
from init_feature_label import GenFeatureLabel
from torch.utils.data import Dataset, DataLoader

__all__ = ['TrainDataSet', 'split_train_test']


class TrainDataSet(Dataset):
    def __init__(self, train_idx):
        GenFeatureLabel()  # 持久化一切所需数据：词汇表、训练特征、训练标签
        super().__init__()
        current_path = os.path.dirname(__file__)
        self.feature = np.load(os.path.join(current_path, 'src/feature.npy'))[train_idx]
        self.label = np.load(os.path.join(current_path, 'src/label.npy'))[train_idx]
        with open(os.path.join(current_path, 'src/THUCNews/vocab.pkl'), 'rb') as f:
            self.vocab = pkl.load(f)

    def __getitem__(self, idx):
        return torch.LongTensor(self.feature)[idx], torch.LongTensor(self.label)[idx]

    def __len__(self):
        return len(self.feature)


class TestDataSet(Dataset):
    def __init__(self, test_idx):
        GenFeatureLabel()  # 持久化一切所需数据：词汇表、训练特征、训练标签
        super().__init__()
        current_path = os.path.dirname(__file__)
        self.feature = np.load(os.path.join(current_path, 'src/feature.npy'))[test_idx]
        self.label = np.load(os.path.join(current_path, 'src/label.npy'))[test_idx]
        with open(os.path.join(current_path, 'src/THUCNews/vocab.pkl'), 'rb') as f:
            self.vocab = pkl.load(f)

    def __getitem__(self, idx):
        return torch.LongTensor(self.feature)[idx], torch.LongTensor(self.label)[idx]

    def __len__(self):
        return len(self.feature)


def split_train_test(train_size_ratio: float):
    current_path = os.path.dirname(__file__)
    raw_data = np.load(os.path.join(current_path, 'src/feature.npy'))
    raw_data_len = len(raw_data)
    train_index = np.random.choice(np.arange(raw_data_len), int(train_size_ratio * raw_data_len),
                                   replace=False)  # "replace=False" means there will not be duplicate item
    test_index = np.delete(np.arange(raw_data_len), train_index)
    return train_index, test_index


if __name__ == '__main__':
    train_idx, test_idx = split_train_test(0.9)
    train_data = TrainDataSet(train_idx)
    test_data = TestDataSet(test_idx)

    trainloader = DataLoader(train_data, 200)
    testloader = DataLoader(test_data, 200)



