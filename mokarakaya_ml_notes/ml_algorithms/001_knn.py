"""
KNN algorithm to solve a classification problem.
The example uses iris data set.
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from sklearn.metrics import accuracy_score
from mokarakaya_ml_notes.ml_algorithms.util import data_util

train_ratio = 0.8
k = 9
feature_num = 4

df_train, df_test = data_util.read_iris_data(train_ratio)

similarities = cosine_similarity(df_test.iloc[:, 0:feature_num], df_train.iloc[:, 0:feature_num])
print(similarities.shape)

nn = np.argsort(similarities * -1)
print(nn.shape)

knn = nn[:, :k]
print(knn.shape)
labels = np.array([df_train.iloc[:, feature_num:].values[a].flatten() for a in knn])
print(labels.shape)
counter = np.array(list(map(Counter, labels)))
print(counter.shape)
predictions = np.array([c.most_common()[0][0] for c in counter])
print(predictions.shape)
accuracy = accuracy_score(df_test.iloc[:, feature_num:].values, predictions)
print(accuracy)


