import torch
import torch.nn as nn


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.lstm1 = nn.LSTM(input_size=50, hidden_size=64, batch_first=True)
        self.time_embedding = nn.Embedding(64, 50)
        self.lstm2 = nn.LSTM(input_size=128, hidden_size=100, batch_first=True)
        self.space_embedding = nn.Embedding(475, 128)
    
    def forward(self, time, space):
        """_summary_

        Args:
            time (_type_): 时间输入
            space (_type_): 空间输入
            时间和空间输入的前两个维度大小必须一致

        Returns:
            _type_: _description_
        """
        ti = self.time_embedding(time)
        sp = self.space_embedding(space)
        time_feature = self.lstm1(ti)[0]
        space_feature = self.lstm2(sp)[0]
        feature = torch.concat([time_feature, space_feature], dim=-1)
        return feature

time_embedding = nn.Embedding(64, 50)
time = torch.randint(low = 0, high = 64, size=(10, 64))
space = torch.randint(low = 0, high = 475, size=(10, 64))

m = Model()
f = m(time, space)
pass