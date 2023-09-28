# -*- coding: utf-8 -*-
"""Income Classsification Case Study.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BOXR1_uEBjknzTM6vjZNwlMuYGzUGuE4
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("/content/income(1).csv")
df.head()

df1 = df.copy()

#EDA

print(df1.info())

df1.isnull().sum()

df1.describe()

df1.describe(include="O")

df1["JobType"].value_counts()

df1["EdType"].value_counts()

df1["maritalstatus"].value_counts()

df1["occupation"].value_counts()

df1["relationship"].value_counts()

df1["race"].value_counts()

df1["nativecountry"].value_counts()

np.unique(df1["JobType"])

np.unique(df1['occupation'])

data = pd.read_csv("/content/income(1).csv", na_values=[" ?"])

data.isnull().sum()

missing= data[data.isnull().any(axis=1)]

data1 = data.dropna(axis=0)

correlation = data1.corr()

data1.columns

gender = pd.crosstab(index= data["gender"], columns= "count", normalize = True)
gender

genders_salsat = pd.crosstab(index= data1['gender'], columns= data1["SalStat"], margins= True, normalize = "index")
genders_salsat

data1["SalStat"] = data1["SalStat"].astype("category")
SalSat = sns.countplot(data= data1, x="SalStat")
plt.show()

plt.hist(data1["age"],bins=10, color= "green", edgecolor= "white")

sns.boxplot(x="SalStat",y= "age", data = data1)
data1.groupby("SalStat")["age"].median()

#JobType Vs Salary Status  (Bar plot)
# Education Vs Salary Status
#Occupation Vs Salary Status
#capitalgain & capitalloss (Histogram)
#Hoursper week Vs Salary Status (Box Plot)

sns.countplot( y="JobType", data=data1, hue="SalStat")

sns.countplot(y="EdType", data= data1, hue="SalStat")

sns.countplot(y="occupation", data= data1, hue="SalStat")

sns.distplot(data1["capitalloss"],kde=False)

sns.distplot(data1["capitalgain"],kde=False)

sns.boxplot(y="hoursperweek", x= "SalStat", data=data1)

#Logistic Regression
#integer encoding
data1["SalStat"]= data["SalStat"].map({" less than or equal to 50,000":0," greater than 50,000":1})
print(data1['SalStat'])

new_data = pd.get_dummies(data1, drop_first= True)

columns_list = list(new_data.columns)
print(columns_list)

features = list(set(columns_list)-set(["SalStat"]))
print(features)

y = new_data["SalStat"].values
print(y)

x= new_data[features].values
print(x)

train_x, test_x, train_y, test_y= train_test_split(x,y, test_size=0.3, random_state=0)

logistic = LogisticRegression()

logistic.fit(train_x, train_y)
logistic.coef_

logistic.intercept_

prediction = logistic.predict(test_x)
print(prediction)

confusion_matriix = confusion_matrix(test_y, prediction)
print(confusion_matriix)

accuracy = accuracy_score(test_y, prediction)
print(accuracy)

print("Misclassified samples: %d" % (test_y != prediction).sum())

#Logistic Regression - Removing Insignificant Variables
data1["SalStat"]= data["SalStat"].map({" less than or equal to 50,000":0," greater than 50,000":1})
print(data1['SalStat'])

cols = ["gender","nativecountry","race","JobType"]
df2= data1.drop(cols, axis=1)
df2

df2 = pd.get_dummies(data1, drop_first= True)

columns_list2 = list(df2.columns)
print(columns_list2)

features = list(set(columns_list2)-set(["SalStat"]))
print(features)

y = df2["SalStat"].values
print(y)

x= df2[features].values
print(x)

train_x, test_x, train_y, test_y= train_test_split(x,y, test_size=0.3, random_state=0)

logistic.fit(train_x, train_y)

pred = logistic.predict(test_x)
accur = accuracy_score(test_y, pred)
print(accur)

con_mat= confusion_matrix(test_y, pred)
print(con_mat)

#KNN
from sklearn.neighbors import KNeighborsClassifier

KNN_classifier = KNeighborsClassifier(n_neighbors=5)

KNN_classifier.fit(train_x,train_y)

pred_ict= KNN_classifier.predict(test_x)

confusion = confusion_matrix(test_y, pred_ict)
print("\t", "Prediction values")
print("Original values", "\n", confusion)

accuracy= accuracy_score(test_y, pred_ict)
print(accuracy)

print("Misclassified samples: %d" % (test_y != pred_ict).sum())

#effect of k value on classifier
Misclassified_sample = []
for i in range(1,20):
  knn = KNeighborsClassifier(n_neighbors=i)
  knn.fit(train_x, train_y)
  pred_i = knn.predict(test_x)
  Misclassified_sample.append((test_y != pred_i).sum())

print(Misclassified_sample)



