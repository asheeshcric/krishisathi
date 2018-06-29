# Sample code for checking the score of the dataset by using various ML models

#Here, only the score of LogisticRegression is tested i.e 0.51
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data= pd.read_csv('datasets.csv')
X=data.iloc[:,0:4]
y=data.iloc[:,-1]
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.3, random_state=42)
lr= LogisticRegression()
lr.fit(X_train,y_train)
y_predict= lr.predict(X_test)
score=accuracy_score(y_test,y_predict)
print(score)