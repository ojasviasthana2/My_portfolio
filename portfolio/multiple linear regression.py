import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# print("woohooo")

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values  # [rows,col]
y = dataset.iloc[:,-1].values

# Encoding categorical data. State column is not numerical like other columns.
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X = np.array(ct.fit_transform(X))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.show()