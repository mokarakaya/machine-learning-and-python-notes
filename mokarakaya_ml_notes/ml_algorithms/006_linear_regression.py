import numpy as np
from mokarakaya_ml_notes.ml_algorithms.util import data_util


def linear_regression(X, y, epochs=1000, learning_rate=0.0001):
    m = float(y.shape[0])
    y = y.values.flatten()
    X = X.values
    theta = np.random.random(X.shape[1])
    b = np.random.random()
    for i in range(epochs):
        y_predicted = np.dot(X, theta.T) + b
        loss = y_predicted - y
        print(np.sum(loss))
        for j in range(X.shape[1]):
            theta_gradient = (1 / m) * sum(X[:, j] * loss)
            theta[j] = theta[j] - (learning_rate * theta_gradient)
        b_gradient = (1 / m) * sum(loss)
        b = b - (learning_rate * b_gradient)

    return theta, b


train_ratio = 0.8
df_train, df_test = data_util.read_wine_quality_data(train_ratio)
df_train_x = df_train.iloc[:, :-1]
df_train_y = df_train.iloc[:, -1:]
theta, b = linear_regression(df_train_x, df_train_y)

print("theta=", theta)
print("b=", b)

test_x = df_test.iloc[:, :-1].values
test_y = df_test.iloc[:, -1:].values.flatten()
predictions = np.dot(theta, test_x.T) + b

avg_error = np.sum(np.abs(predictions - test_y)) / test_y.shape
print('avg_error:', avg_error) #avg_error: [0.78951395]