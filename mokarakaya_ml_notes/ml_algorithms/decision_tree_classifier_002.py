from mokarakaya_ml_notes.ml_algorithms.util import data_util
from sklearn import tree


def run():
    train_ratio = 0.8
    df_X_train, df_y_train, df_X_test, df_y_test = data_util.read_iris_data(train_ratio)
    clf = tree.DecisionTreeClassifier()
    clf.fit(df_X_train, df_y_train)
    print(
        "dataset: iris, algo: decision tree classification, score:",
        clf.score(df_X_test, df_y_test),
    )  # 0.9615
