#!/usr/bin/python
#Import pandas
import pandas as pd

from sklearn import tree

headers = ["sepal_len", "sepal_wid", "petal_len", "petal_wid", "name"]

dataframe = pd.read_csv('iris_training.data', names=headers)

#print(dataframe['name'])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(dataframe[["sepal_len", "sepal_wid", "petal_len", "petal_wid"]],
                dataframe[["name"]])


X= pd.read_csv('iris_testing.data', 
               names=headers, usecols=["sepal_len", "sepal_wid", "petal_len", "petal_wid"])

Y= pd.read_csv('iris_testing.data', 
               names=headers, usecols=["name"])


P = clf.predict(X)

c = 0;
for i in range(0, 49) : 
    if P[i] != Y["name"][i] :
         c = c + 1

print(c, 'out of 50 testing cases are mis-predicted using decision tree.')

