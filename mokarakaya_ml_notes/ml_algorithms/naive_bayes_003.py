"""
Naive bayes algorithm to solve spam classification problem.
"""

from sklearn.metrics import accuracy_score
from mokarakaya_ml_notes.ml_algorithms.util import data_util
from sklearn.naive_bayes import MultinomialNB


def run():
    train_ratio = 0.8

    df_X_train, df_y_train, df_X_test, df_y_test = data_util.read_spam_data(train_ratio)
    model_sk = MultinomialNB()
    model_sk.fit(df_X_train, df_y_train)

    predictions_sk = model_sk.predict(df_X_test)

    accuracy = accuracy_score(df_y_test, predictions_sk)
    print("dataset: spam, algo: naive bayes, score:", accuracy)  # 0.9806629834254144
