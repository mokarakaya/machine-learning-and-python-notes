import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing

"""
datasets:

iris: https://archive.ics.uci.edu/ml/datasets/Iris
wine-quality: https://archive.ics.uci.edu/ml/datasets/Wine+Quality
spam: original data https://scholarbank.nus.edu.sg/handle/10635/137343 . Cleared version https://www.kaggle.com/ishansoni/sms-spam-collection-dataset/data?select=spam.csv


"""
datasets = "~/datasets"


def __split_train_test(df, train_ratio, mask=None):
    if mask is None:
        mask = np.random.rand(len(df)) < train_ratio
    df_train = df[mask]
    df_test = df[~mask]

    return df_train, df_test


def read_wine_quality_data(train_ratio):
    df = pd.read_csv(
        "{}/wine-quality/winequality-red.csv".format(datasets), delimiter=";"
    )
    return __split_train_test(df, train_ratio)


def read_iris_data(train_ratio):
    df = pd.read_csv("{}/iris/iris.data".format(datasets), header=None)
    df.columns = ["x1", "x2", "x3", "x4", "y"]
    le = preprocessing.LabelEncoder()
    df["y"] = le.fit_transform(df["y"])
    mask = np.random.rand(len(df)) < train_ratio
    df_X_train, df_X_test = __split_train_test(
        df.drop(["y"], axis=1), train_ratio, mask
    )
    df_y_train, df_y_test = __split_train_test(df["y"], train_ratio, mask)
    return df_X_train, df_y_train, df_X_test, df_y_test


def vectorize(df):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df.values)
    X = X.toarray()
    return X


def read_spam_data(train_ratio):
    df = pd.read_csv(
        "{}/spam/spam.csv".format(datasets), encoding="latin-1", delimiter=","
    )
    df = df.iloc[:, :2]
    df.columns = ["class", "message"]
    df_X = vectorize(df["message"])
    mask = np.random.rand(len(df)) < train_ratio
    df_X_train, df_X_test = __split_train_test(df_X, train_ratio, mask)
    df_y_train, df_y_test = __split_train_test(df["class"], train_ratio, mask)
    return df_X_train, df_y_train, df_X_test, df_y_test
