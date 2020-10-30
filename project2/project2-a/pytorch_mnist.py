"""
Google Colaboratoryで実行しました。
"""
!pip install pycodestyle flake8 pycodestyle_magic
%load_ext pycodestyle_magic



# %%flake8
# % matplotlib inline

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch.nn.functional as F


class MyNet(torch.nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.fc1 = torch.nn.Linear(28* 28, 256)
        self.fc2 = torch.nn.Linear(256, 128)
        self.fc3 = torch.nn.Linear(128, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = torch.sigmoid(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)

        return x


def load_MNIST(batch=128, intensity=1.0):
    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5, ), (0.5, ))])
    train_set = datasets.MNIST(root='./data',
                               train=True,
                               download=True,
                               transform=transform)
    test_set = datasets.MNIST(root='./data',
                              train=False,
                              transform=transform)

    train_loader = torch.utils.data.DataLoader(train_set,
                                               batch_size=batch,
                                               shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_set,
                                              batch_size=batch,
                                              shuffle=True)

    return {'train_data': train_loader, 'test_data': test_loader}



# %%flake8
if __name__ == '__main__':
    epoch = 20
    net: torch.nn.Module = MyNet()
    loaders = load_MNIST()

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(net.parameters(), lr=0.5)

    for e in range(epoch):
        """train"""
        correct_train = 0
        total_train = 0
        net.train(True)
        for i, (data, target) in enumerate(loaders['train_data']):
            data = data.view(-1, 28*28)

            optimizer.zero_grad()
            output = net(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            if i % 100 == 0:
                pred = output.argmax(dim=1, keepdim=True)
                correct_train = pred.eq(target.view_as(pred)).sum().numpy()
                total_train = target.size(0)
                print('{}epoch, Train Loss:{}, Train Accuracy:{}'.format(e+1,
                                                                         loss.item(),
                                                                         correct_train/total_train))
        """test(accuracy)"""
        # net.eval()
        net.train(False)
        correct = 0
        total = 0
        with torch.no_grad():
            for data, target in loaders['test_data']:
                data = data.view(-1, 28 * 28)
                output = net(data)
                pred = output.argmax(dim=1, keepdim=True)
                correct += pred.eq(target.view_as(pred)).sum().numpy()
                total += target.size(0)
        print('Test Accuracy: {}'.format(correct / total))
