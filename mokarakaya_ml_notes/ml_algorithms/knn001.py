"""
KNN algorithm to solve a classification problem.
The example uses iris data set.
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from sklearn.metrics import accuracy_score
from mokarakaya_ml_notes.ml_algorithms.util import data_util
import pandas as pd


def run():
    train_ratio = 0.8
    k = 10

    df_X_train, df_y_train, df_X_test, df_y_test = data_util.read_iris_data(train_ratio)

    similarities = cosine_similarity(df_X_train, df_X_test).T
    nn = np.argsort(similarities * -1)[:, :k]
    nn = pd.DataFrame(nn).applymap(lambda x: df_y_train.iloc[x])
    predictions = [Counter(row).most_common()[0][0] for _, row in nn.iterrows()]
    accuracy = accuracy_score(df_y_test.values, predictions)
    print("dataset: iris, algo: knn, score:", accuracy)  # 0.9666666666666667
