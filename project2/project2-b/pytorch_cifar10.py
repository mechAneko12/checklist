"""
Google Colaboratoryで実行しました。
"""
!pip install pycodestyle flake8 pycodestyle_magic
%load_ext pycodestyle_magic

# %%flake8
# % matplotlib inline

import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision import datasets
import torch.nn.functional as F


class MyNet(torch.nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.drop = nn.Dropout2d()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.conv3 = nn.Conv2d(16, 24, 2)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
        """
        nn.init.xavier_normal_(self.conv1.weight)
        nn.init.xavier_normal_(self.conv2.weight)
        nn.init.xavier_normal_(self.fc1.weight)
        nn.init.xavier_normal_(self.fc2.weight)
        nn.init.xavier_normal_(self.fc3.weight)
        """

    def forward(self, x):
        # x = self.drop(x)
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        # x = self.drop(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        # x = self.drop(x)
        # x = F.relu(self.conv3(x))
        # x = self.pool(x)
        x = x.view(-1, 16 * 5 * 5)
        x = self.fc1(x)
        x = self.drop(x)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def load_MNIST(batch=100):
    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5),
                                    (0.5, 0.5, 0.5))])

    train_set = torchvision.datasets.CIFAR10(root='./data',
                                             train=True,
                                             download=True,
                                             transform=transform)
    train_loader = torch.utils.data.DataLoader(train_set,
                                               batch_size=batch,
                                               shuffle=True,
                                               num_workers=2)

    test_set = torchvision.datasets.CIFAR10(root='./data',
                                            train=False,
                                            download=True,
                                            transform=transform)
    test_loader = torch.utils.data.DataLoader(test_set,
                                              batch_size=batch,
                                              shuffle=False,
                                              num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    return {'train_data': train_loader,
            'test_data': test_loader,
            'classes': classes}


def evaluation(m):
    tp = np.empty((0))
    for k in range(10):
        tp = np.append(tp, m[k][k])
    rec = tp / np.sum(m, axis=1)
    rec_ave = np.mean(rec)
    pre = tp / np.sum(m, axis=0)
    pre_ave = np.mean(pre)
    return 2.0 * (rec_ave * pre_ave) / (rec_ave + pre_ave)

# %%flake8
if __name__ == '__main__':
    epoch = 20
    net: torch.nn.Module = MyNet()
    loaders = load_MNIST()

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(net.parameters(), lr=0.4)
    optimizer = torch.optim.Adadelta(net.parameters(), lr=0.4)

    for e in range(epoch):
        """train"""
        correct_train = 0
        total_train = 0
        net.train(True)
        for i, (data, target) in enumerate(loaders['train_data']):
            optimizer.zero_grad()
            output = net(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            if i % 100 == 0:
                pred = output.argmax(dim=1, keepdim=True)
                correct_train = pred.eq(target.view_as(pred)).sum().numpy()
                total_train = target.size(0)
                acc = correct_train/total_train
                print('{}epoch, Loss:{}, acc:{}'.format(e+1,
                                                        loss.item(),
                                                        acc))
        """test(accuracy)"""
        # net.eval()
        net.train(False)

        matrix = np.zeros((10, 10), float)
        with torch.no_grad():
            for data, target in loaders['test_data']:
                output = net(data)
                pred = output.argmax(dim=1, keepdim=True)
                for j in range(target.size(0)):
                    matrix[int(target[j])][int(pred[j][0])] += 1.0
        print('Test Accuracy: {}'.format(evaluation(matrix)))
