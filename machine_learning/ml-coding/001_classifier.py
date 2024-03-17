import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder
import torch
import torch.nn as nn
import torch.nn.functional as f
from torch.utils.data import Dataset, DataLoader

random_state = 42
np.random.seed(random_state)

"""
Train a classifier by using the data returned by `create_dataset` function.
Data looks like:

```

[
 ['2.9073069528421915' '2.99404746439382' 'a' 'b' '1']
 ['2.9525054688839045' '2.934667076742629' 'u' 'b' '0']
...
]

```

The first two features are continuous features.
The next two features are categorical features.
The last feature is the label.
All fields are in string format due to numpy.

"""


def data_generator(data_size, mean, std, p, y_p):
    cont_features = np.random.normal(mean, std, data_size * 2)
    idx = np.random.randint(0, cont_features.size - 1, int(cont_features.size * 0.1))
    cont_features[idx] = np.nan
    cont_features = cont_features.reshape(data_size, 2)
    cat_features = np.random.choice(["a", "b", "u"], data_size * 2, p=p).reshape(
        data_size, 2
    )
    y_labels = np.random.choice([0, 1], data_size, p=y_p)
    return cont_features, cat_features, y_labels


def create_dataset():
    cont_features1, cat_features1, y_labels1 = data_generator(
        50, 2, 0.1, [0.3, 0.6, 0.1], [0.2, 0.8]
    )
    cont_features2, cat_features2, y_labels2 = data_generator(
        50, 4, 0.1, [0.6, 0.3, 0.1], [0.8, 0.2]
    )
    cont_features = np.concatenate([cont_features1, cont_features2])
    cat_features = np.concatenate([cat_features1, cat_features2])
    y_labels = np.concatenate([y_labels1, y_labels2])
    X = np.hstack((cont_features, cat_features))
    data = np.hstack((X, y_labels.reshape(-1, 1)))
    np.random.shuffle(data)
    return data


def train_logistic_regression(X_train, X_test, y_train, y_test):
    clf = LogisticRegression(random_state=random_state)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    prf = precision_recall_fscore_support(y_test, y_pred)
    print(prf)
    print(confusion_matrix(y_test, y_pred))


def train_neural_network(X_train, X_test, y_train, y_test, epochs=1000):
    class NNClassifier(nn.Module):
        def __init__(self, input_size):
            super(NNClassifier, self).__init__()
            self.fc1 = nn.Linear(input_size, 64)
            self.fc2 = nn.Linear(64, 2)

        def forward(self, x):
            x = f.relu(self.fc1(x))
            x = self.fc2(x)
            return torch.softmax(x, dim=1)

    class NNDataSet(Dataset):
        def __init__(self, X, Y):
            self.X = X
            self.Y = Y
            if len(self.X) != len(self.Y):
                raise Exception("The length of X does not match the length of Y")

        def __len__(self):
            return len(self.X)

        def __getitem__(self, index):
            _x = self.X[index]
            _y = self.Y[index]
            return _x, _y

    model = NNClassifier(X_train.shape[1])
    X_train = torch.tensor(X_train.astype(float), dtype=torch.float32)
    y_train = torch.tensor(y_train.astype(int), dtype=torch.long)
    loader = DataLoader(NNDataSet(X_train, y_train), batch_size=128, shuffle=True)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_fn = torch.nn.CrossEntropyLoss()
    for epoch in range(epochs):
        model.train()
        for x, y in loader:
            optimizer.zero_grad()
            outputs = model(x)
            loss = loss_fn(outputs, y)
            loss.backward()
            optimizer.step()
        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item()}")
    model.eval()
    with torch.no_grad():
        X_test = torch.tensor(X_test.astype(float), dtype=torch.float32)
        y_pred = model(X_test).detach().numpy()
        y_pred = np.argmax(y_pred, axis=1)
        y_test = y_test.astype(int)
        prf = precision_recall_fscore_support(y_test, y_pred)
        print(prf)
        print(confusion_matrix(y_test, y_pred))


def main():
    data = create_dataset()
    print(data)

    cont_features = data[:, :2].astype(float)
    cat_features = data[:, 2:4]
    y_labels = data[:, -1]

    col_trans = ColumnTransformer([("col", SimpleImputer(), [0, 1])])
    cont_features = col_trans.fit_transform(cont_features)

    col_trans = ColumnTransformer([("col", OneHotEncoder(), [0, 1])])
    cat_features = col_trans.fit_transform(cat_features)
    X = np.hstack((cont_features, cat_features))
    print(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_labels, test_size=0.3, random_state=random_state
    )
    train_logistic_regression(X_train, X_test, y_train, y_test)
    train_neural_network(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
