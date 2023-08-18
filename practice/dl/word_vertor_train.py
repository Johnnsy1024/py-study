import torch

vocab_size = 1
vocab = ['天安门']
label = 0

class EmbedTrain(torch.nn.Module):
    def __init__(self):
        super(EmbedTrain, self).__init__()
        self.linear1 = torch.nn.Linear(10, 20)
        self.linear2 = torch.nn.Linear(20, 1)
        self.embedding = torch.nn.Embedding(1, 10)
    def forward(self, x):
        x = self.embedding(x)
        x = self.linear1(x)
        x = self.linear2(x)
        return x

m = EmbedTrain()
loss = torch.nn.MSELoss()
opt = torch.optim.SGD(m.parameters(), lr=0.001)
print('before')
print('------------')
for i in m.embedding.parameters():
    print(i)

for i in range(1000):
    output = m(torch.LongTensor([0]))
    opt.zero_grad()
    y_true = torch.Tensor([0])
    l = loss(output, y_true)
    print(l.item())
    l.backward()
    opt.step()

print('after')
print('------------')
for i in m.embedding.parameters():
    print(i)