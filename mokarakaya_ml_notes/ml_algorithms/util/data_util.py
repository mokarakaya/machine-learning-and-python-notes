import pandas as pd
import numpy as np


datasets = '~/datasets'


def read_iris_data(train_ratio):
    df = pd.read_csv('{}/iris.data'.format(datasets))
    mask = np.random.rand(len(df)) < train_ratio
    df_train = df[mask]
    df_test = df[~mask]

    return df_train, df_test
