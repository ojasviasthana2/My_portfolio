import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# print("woohooo")

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values  # [rows,col]
y = dataset.iloc[:,-1].values

# Encoding categorical data. State column is not numerical like other columns.
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X = np.array(ct.fit_transform(X))

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=0)

regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
