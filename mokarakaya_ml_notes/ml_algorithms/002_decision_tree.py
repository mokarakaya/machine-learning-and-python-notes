import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from sklearn.metrics import accuracy_score
from mokarakaya_ml_notes.ml_algorithms.util import data_util

train_ratio = 0.8
k = 9

x_train, y_train, x_test, y_test = data_util.read_iris_data(train_ratio)


def transform_to_categories(x_train):
    means = x_train.mean()
    x_train_t = np.where((x_train < means), 'Low', 'High')
    return x_train_t


x_train = transform_to_categories(x_train)
x_test = transform_to_categories(x_test)

def train_complete():
    return True


def find_best_split():
    pass


class Node:
    def __init__(self, name):
        self.name = name
        self.links = {}

while not train_complete():
    find_best_split()
    node = Node('test')

