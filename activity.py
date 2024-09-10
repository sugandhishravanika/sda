# -*- coding: utf-8 -*-
"""Activity

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QTQeajGcEZ7lOSlvZHLQ-sz0loG9WXys

import tkinter as tk
from tkinter import messagebox
import mysql.connector

def submit():
    name = name_entry.get()
    reg = reg_entry.get()

    if name and reg:
        try:
            db_config = {
                "host": "localhost",
                "user": "root",
                "password": "BVVS",
                "database": "ankita"
            }
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            query = "INSERT INTO library (name, reg) VALUES (%s, %s)"
            values = (name, reg)
            cursor.execute(query, values)

            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Data submitted successfully!")
            clear_fields()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

def clear_fields():
    name_entry.delete(0, tk.END)
    reg_entry.delete(0, tk.END)

def delete():
    reg = reg_entry.get()

    if reg:
        try:
            db_config = {
                "host": "localhost",
                "user": "root",
                "password": "BVVS",
                "database": "ankita"
            }
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            query = "DELETE FROM library WHERE reg = %s"
            values = (reg,)
            cursor.execute(query, values)

            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Data deleted successfully!")
            clear_fields()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    else:
        messagebox.showwarning("Error", "Please enter the registration number.")

def alter():
    name = name_entry.get()
    reg = reg_entry.get()

    if name and reg:
        try:
            db_config = {
                "host": "localhost",
                "user": "root",
                "password": "BVVS",
                "database": "ankita"
            }
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            query = "UPDATE library SET name = %s WHERE reg = %s"
            values = (name, reg)
            cursor.execute(query, values)

            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Data updated successfully!")
            clear_fields()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

root = tk.Tk()
root.title("Database GUI")

name_label = tk.Label(root, text="name:")
reg_label = tk.Label(root, text="Registration:")

name_entry = tk.Entry(root)
reg_entry = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=submit)
clear_button = tk.Button(root, text="Clear", command=clear_fields)
delete_button = tk.Button(root, text="Delete", command=delete)
alter_button = tk.Button(root, text="Update", command=alter)

name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
reg_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

name_entry.grid(row=0, column=1, padx=10, pady=10)
reg_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button.grid(row=2, column=0, columnspan=1, pady=10)
clear_button.grid(row=2, column=1, columnspan=1, pady=10)
delete_button.grid(row=3, column=0, columnspan=1, pady=10)
alter_button.grid(row=3, column=1, columnspan=1, pady=10)

root.mainloop()

WEEK-3
Consider a dataset and infer the relations with the help of different plots
"""



import pandas as pd
import matplotlib.pyplot as plt
mtcars=pd.read_csv("/content/mtcars.csv")
mtcars.head()

plt.hist(mtcars['mpg'],bins=10)
plt.hist(mtcars['hp'],bins=10)
plt.show()

plt.scatter(x='mpg',y='hp',data=mtcars)
plt.xlabel("miles per gallon")
plt.ylabel("horse power")
plt.show()

import matplotlib.pyplot as plt
plt.boxplot(mtcars['mpg'])
plt.show()

import matplotlib.pyplot as plt
x=mtcars['hp']
y=mtcars['wt']
plt.bar(x,y,width=5)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
titanic=pd.read_csv("/content/titanic.csv")
titanic.head()

plt.hist(titanic['Pclass'],width=10)
plt.show()

plt.scatter(x='Age',y='Parch',data=titanic)
plt.xlabel("Age")
plt.show()

import matplotlib.pyplot as plt
plt.boxplot(titanic['PassengerId'])
plt.show()

import matplotlib.pyplot as plt
x=titanic['PassengerId']
y=titanic['Parch']
plt.bar(x,y,width=5)
plt.show()

"""WEEK-4
Use relevant python packages to compute Central tendency for the parametersDispersionfortheparameters
1.datadistribution
2.Visualizeabovecomputationwithvarioustechniques


"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("/content/tips (1).csv")
data.head()

mean=data['size'].mean()
median=data['total_bill'].median()
mode=stats.mode(data['tip'])
print("centraltendency")
print(mean)
print(median)
print(mode)

data_range=np.ptp(data['size'])
variance=np.var(data['size'])
std_deviation=np.std(data['size'])
iqr=np.percentile(data['size'],75)-np.percentile(data['size'],25)
print("dispersion")
print("data_range",data_range)
print("variance",variance)
print("std_deviation",std_deviation)
print("iqr",iqr)

import seaborn as sns
plt.figure(figsize=(15,5))
plt.subplot(131)
sns.histplot(data['size'],kde=True)
plt.title("Histogramofhp")
plt.subplot(132)
sns.boxplot(x='size',data=data)
plt.title("BoxPlotofsize")
plt.show()

"""WEEK-5
Dealing with missing values with different approaches Outliers
Detecting outliers.
● univariateoutlierdetection
● bivariateoutlierdetection



"""

import numpy as np
import pandas as pd
data=pd.read_csv("/content/iris.csv")
data.head()

missing_values=data.isnull().sum()
print("MissingValues:\n",missing_values)

from scipy import stats # outlier detection
import pandas as pd
import pandas as pd
df=pd.read_csv('/content/iris.csv')
df.describe()
zscore=stats.zscore(df['sepal_width'])
threshold=2
outlier=abs(zscore)>threshold
print(outlier)

import matplotlib.pyplot as plt
import pandas as pd
data = {
'sepal_width': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 1000]
}
df = pd.DataFrame(data)
z_scores = (df['sepal_width'] - df['sepal_width'].mean()) / df['sepal_width'].std()
threshold = 3
outliers = df[(z_scores > threshold) | (z_scores < -threshold)]
plt.figure(figsize=(8, 6))
plt.plot(df.index, df['sepal_width'], 'bo', label='Data Points')
plt.plot(outliers.index, outliers['sepal_width'], 'ro', label='Outliers')
plt.xlabel("Index")
plt.ylabel("sepal_width")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('/content/iris.csv')
plt.scatter(x='sepal_length',y='sepal_width',data=data)
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.show()

"""WEEK-6
split training and testing data sets inPython using train_test_split() of
sci-kitlearn.Explore the optionsof train_test_split()
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris=load_iris()
x,y=iris.data,iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=42)
print("X train data :",x_train)
print("X test data :",x_test)
print("y train data :",y_train)
print("y test data :",y_test)

"""WEEK - 7 Iris dataset from sci-kit learn Perform data exploration,preprocessing and splitting Data Exploration :


[ ]

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('/content/iris.csv')
summary=df.describe()
sample_data=df.head()
missing_values=df.isnull().sum()
print("\nsummary of the dataset:",summary)
print("\nsample data of the dataset:",sample_data)
print("\nchecking missing values in dataset:",missing_values)

print(df.columns)

sns.histplot(df['sepal.length'],bins=10)
plt.title('Histplot of SepalLengthCm column')
plt.show()

sns.countplot(df['sepal.width'])
plt.title('count plot of SepalWidthCm column')
plt.show()

"""Data Splitting :"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris=load_iris()
x,y=iris.data,iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=42)
print("x train data:",x_train)
print("x test data:",x_test)
print("y train data:",y_train)
print("y test data:",y_test)

"""Data preprocessing :"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


numerical_df = df.select_dtypes(include=['float', 'int'])


missing = numerical_df.dropna()
print("Removed the missing values:")
print(missing.head())

correlation = numerical_df.corr()
print("Checking the correlation of the dataset:")
print(correlation)


plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Correlation of Dataset')
plt.show()

print(df.columns)


x = df.drop(columns=['sepal.length'])
print("Removed the sepal.length column:")
print(x.head())

"""2.Build decision tree-based model inpython for like Breast Cancer Wisconsin(diagnostic) dataset from sci-kit learn Or any classification dataset from UCI ,Kaggle."""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
breast=load_breast_cancer ()
x,y=breast.data,breast.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=50)
clf=DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
xtrain=clf.predict(x_train)
xtest=clf.predict(x_test)
print("Accuracy of the Traindata:",accuracy_score(y_train,xtrain))
print("Accuracy of the Test data :",accuracy_score(y_test,xtest))