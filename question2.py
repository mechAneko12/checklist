import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris_dataset = load_iris()

X = iris_dataset['data']
y = iris_dataset['target']


X_new = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)


def f(x, b):
    return 1.0 / (1.0 + np.exp(-np.dot(x, b.T)))


if __name__ == '__main__':
    print(f(X_new, np.random.normal(0, 1, (1, X_new.shape[1]))))
