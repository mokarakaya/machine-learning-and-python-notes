import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder

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
    cont_features = np.random.normal(mean, std, data_size*2)
    idx = np.random.randint(0, cont_features.size -1, int(cont_features.size * 0.1))
    cont_features[idx] = np.nan
    cont_features = cont_features.reshape(data_size, 2)
    cat_features = np.random.choice(["a", "b", "u"], data_size*2, p=p).reshape(data_size, 2)
    y_labels = np.random.choice([0, 1], data_size, p=y_p)
    return cont_features, cat_features, y_labels

def create_dataset():
    cont_features1, cat_features1, y_labels1 = data_generator(50, 2, 0.1, [0.3, 0.6, 0.1], [0.3, 0.7])
    cont_features2, cat_features2, y_labels2 = data_generator(50, 3, 0.1, [0.6, 0.3, 0.1], [0.7, 0.3])
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

def main():
    data = create_dataset()
    print(data)

    cont_features = data[:, :2].astype(float)
    cat_features = data[:, 2:4]
    y_labels = data[:, -1]

    col_trans = ColumnTransformer([
        ("col", SimpleImputer(), [0,1])
    ])
    cont_features = col_trans.fit_transform(cont_features)

    col_trans = ColumnTransformer([
        ("col", OneHotEncoder(), [0,1])
    ])
    cat_features = col_trans.fit_transform(cat_features)
    X = np.hstack((cont_features, cat_features))
    print(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y_labels, test_size=0.3, random_state=random_state)
    train_logistic_regression(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
