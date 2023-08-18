import os
import datetime
import torch
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score
import torch.nn.functional as F
import matplotlib.pyplot as plt



class Model:
    def __init__(self, model):
        self.model = model
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def train(self, train_iter: DataLoader, test_iter: DataLoader, epochs=20):
        batch_cnt = len(train_iter)
        model = self.model
        model.to(self.device)
        model.train()  # 将模型调整至训练模式
        optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)
        creterion = torch.nn.CrossEntropyLoss()
        print('')
        model_name = model._get_name()
        tips = f"{model_name} 开始训练"
        print(tips)

        train_loss_list, train_acc_list = [], []
        test_loss_list, test_acc_list = [], []
        for epoch in range(epochs):
            for idx, (x, y) in enumerate(train_iter):
                x = x.to(self.device)
                y = y.to(self.device)

                y_pred = model(x)
                optimizer.zero_grad()
                loss = creterion(y_pred, y)
                y_pred = torch.max(F.softmax(y_pred, dim=-1), dim=-1)[1]  # torch.max() return a tuple, which include the maximum number and index
                acc = accuracy_score(y.cpu().numpy(), y_pred.detach().cpu().numpy())
                loss.backward()
                optimizer.step()
                train_loss_list.append(loss.item())
                train_acc_list.append(acc)

                str_ = f"{model_name} train Epoch:{epoch + 1} / {epochs} batch:{idx + 1}/{batch_cnt} loss:{loss.item() : .4f} acc:{acc * 100 : .4f}%"
                sys.stdout.write('\r' + str_)
                sys.stdout.flush()
            # print(f'Epoch:{epoch+1} / {epochs} mean loss : {}')
            # 每训练完一个epoch,进行一次test
            self.test(model, test_iter, test_loss_list, test_acc_list)

    def test(self, model, test_iter: DataLoader, test_loss_list: list, test_acc_list: list):
        model.eval()
        model_name = model._get_name()
        creterion = torch.nn.CrossEntropyLoss()
        with torch.no_grad():
            for x, y in test_iter:
                x = x.to(self.device)
                y = y.to(self.device)

                y_pred = model(x)
                loss = creterion(y_pred, y)
                y_pred = torch.max(F.softmax(y_pred, dim=-1), dim=-1)[1]
                acc = accuracy_score(y.cpu().numpy(), y_pred.cpu().numpy())
                test_loss_list.append(loss.item())
                test_acc_list.append(acc)
                str_2 = f"{model_name} test loss:{loss.item() : .4f} acc:{acc * 100 : .4f}%"
                sys.stdout.write('\r' + str_2)
                sys.stdout.flush()

    def plot(self, train_loss_list, train_acc_list, test_loss_list, test_acc_list):
        fig = plt.figure(dpi=300)
        ax1 = fig.add_subplot(121)
        l1, = ax1.plot(train_loss_list, color='red', label='train loss')
        ax1_ = ax1.twinx()
        l2, = ax1_.plot(train_acc_list, color='blue', label='train acc')
        plt.legend(handles=[l1, l2])
        ax2 = fig.add_subplot(122)
        l3, = ax2.plot(test_loss_list, color='red', label='test loss')
        ax2_ = ax2.twinx()
        l4, = ax2_.plot(test_acc_list, color='blue', label='test acc')
        plt.legend(handles=[l3, l4])
        plt.tight_layout()
        plt.savefig(f'result/pic/result{datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")}.png')


if __name__ == '__main__':
    from models.transformer import Transformer
    import sys
    import pickle as pkl

    sys.path.append('datas')

    from dataloader_pytorch import TrainDataSet, TestDataSet, split_train_test
    train_index, test_index = split_train_test(0.9)
    train_dataset = TrainDataSet(train_index)
    test_dataset = TestDataSet(test_index)

    train_dataloader = DataLoader(train_dataset, batch_size=200)
    test_dataloader = DataLoader(test_dataset, batch_size=200)

    print('hhh')
    with open('datas/src/THUCNews/vocab.pkl', 'rb') as f:
        vocab = pkl.load(f)
    m = Transformer(len(vocab), seq_len=38, n_class=10, device='cuda', dropout=0.2)
    m = Model(m)
    m.train(train_dataloader, test_dataloader, epochs=5)
    # from datas.dataloader_pytorch import *
    #
    # dataset = MyDataSet()
    # train_data, test_data = split_train_test(dataset, 0.9)
    # vocab_size = len(dataset.vocab)
    #
    # train_iter = DataLoader(dataset, batch_size=50)
    # # test_iter = DataLoader(test_data, batch_size=50)
    # print(len(train_iter))
    #
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # m = Transformer(vocab_size, seq_len=38, n_class=10, device=device, dropout=0.3).to(device)
    # m = Model(m)

    # m.train(train_iter, test_iter, epochs=5)