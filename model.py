# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree

def model_function():
    dataset = pd.read_csv('final_table.csv')

    with open('final_table.csv', 'r') as fl:
        data = fl.readlines()
    lines = len(list(data))
    lines = lines - 2

    cols = ['productcategory', 'dob', 'maritalstatus', 'maxeducationlevel', 'primaryocc',
            'primarylanguage', 'annualincome', 'leadquality']

    dataset = dataset.fillna(" ")
    dataset.fillna(dataset.mode())

    dataset[cols] = dataset[cols].apply(LabelEncoder().fit_transform)

    X = dataset.iloc[:lines, [13, 4, 12, 11, 10, 9, 14]].values
    y = dataset.iloc[:lines, -2].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

    st_X = StandardScaler()
    X_train = st_X.fit_transform(X_train)
    X_test = st_X.transform(X_test)

    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    predict = clf.predict(X_test)

    Z = dataset.iloc[-1:, [13, 4, 12, 11, 10, 9, 14]].values
    output = clf.predict(Z)
    return output