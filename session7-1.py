import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

#load the train and test datasets to create two DataFrames

train_url="http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train=pd.read_csv(train_url)
test_url= "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test=pd.read_csv(test_url)

train.fillna(train.mean(),inplace=True)
train=train.drop(['Name','Ticket','Cabin','Embarked'],axis=1)
test=test.drop(['Name','Ticket','Cabin','Embarked'],axis=1)
labelEncoder=LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex']=labelEncoder.transform(train['Sex'])
test['Sex']=labelEncoder.transform(test['Sex'])
X=np.array(train.drop(['Survived'],1).astype(float))
Y=np.array(train['Survived'])
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
print(train.head())
print(train.describe())
print(train.columns.values)
#print(train.isna().head)
print(train.isna().sum())
print(train.info())
print("*****test data*******")
print(test.head())
print(test.describe())
test.fillna(test.mean(),inplace=True)
#print(test.isna().head)
print(test.isna().sum())
print(test.info())
#print(X)
#print(Y)
