from mokarakaya_ml_notes.ml_algorithms.util import data_util
from sklearn.tree import DecisionTreeRegressor


def run():
    train_ratio = 0.8
    df_train, df_test = data_util.read_wine_quality_data(train_ratio)
    df_train_x = df_train.iloc[:, :-1]
    df_train_y = df_train.iloc[:, -1:]

    test_x = df_test.iloc[:, :-1].values
    test_y = df_test.iloc[:, -1:].values.flatten()

    reg = DecisionTreeRegressor().fit(df_train_x, df_train_y)
    print(
        "dataset: wine, algo: decision tree regression, score:",
        reg.score(test_x, test_y),
    )  # 0.31
