# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(random_state=0)
# X = [[ 1,  2,  3],[11, 12, 13]]

# y = [0, 1]

# print(X, y)

# clf.fit(X, y)

# pred = clf.predict(X)

# clf.predict([[4, 5, 6], [14, 15, 16]])

# print(clf)
# print(pred)

# from sklearn.preprocessing import StandardScaler

# X = [[0, 15],[1, -10]]

# StandardScaler().fit(X).transform(X)

import pandas as pd
import os

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

init_path = '/Users/blakenicholson/documents/personal/coding/handson-ml/'

HOUSING_PATH = os.path.join(init_path,"datasets", "housing")


def load_melbhousing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "melb_data.csv")
    return pd.read_csv(csv_path)

housing_data = load_melbhousing_data()

print(housing_data.head())
# print(housing_data.info())
# print(housing_data["Suburb"].value_counts())
print(housing_data.describe())

%matplotlib inline
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(20,15))
save_fig("attribute_histogram_plots")
plt.show()

# create a pipeline object
pipe = make_pipeline(
	StandardScaler(),
	LogisticRegression()
)

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# fit the whole pipeline
pipe.fit(X_train, y_train)

score = accuracy_score(pipe.predict(X_test), y_test)

print(score)
