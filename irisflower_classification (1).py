# -*- coding: utf-8 -*-
"""irisflower classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oAadA2ectve_7tOZjvebsgZ5qUy4HfXS
"""

import pandas as pd
dataset = pd.read_csv("/content/IRIS.csv")
dataset.head()

dataset.shape

dataset.dtypes

dataset.describe()

print("Target Labels" ,dataset["species"].unique())

import plotly.express as px
fig = px.scatter(dataset, x="sepal_width",y="sepal_length", color="species")
fig.show()

x = dataset.drop("species", axis=1)
y = dataset["species"]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.2, 
                                                    random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)

import numpy as np
x_new = np.array([[5 , 2.9, 1 , 0.2]])
prediction = knn.predict(x_new)
print("prediction:{}".format(prediction))