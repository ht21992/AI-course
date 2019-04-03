import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
colnames=['sepal-length','sepal-width','petal-length','petal width','Class']
irisdata=pd.read_csv(url,names=colnames)
x=irisdata.drop('Class',axis=1)
y=irisdata['Class']
"""print(irisdata.head)
print(irisdata.tail)
print(irisdata.shape)"""
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30)
#print(x_train.head)
"""from sklearn.svm import SVC
svclassifier=SVC(kernel='poly',degree=8)
svclassifier.fit(x_train,y_train)
y_pred=svclassifier.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix"""
#print(classification_report(y_test,y_pred))
#print(confusion_matrix(y_test,y_pred))
"""from sklearn.svm import SVC
svclassifier=SVC(kernel='rbf')
svclassifier.fit(x_train,y_train)
y_pred=svclassifier.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_pred))
#print((confusion_matrix(y_test,y_pred)))"""
from sklearn.svm import SVC
svclassifier=SVC(kernel='sigmoid')
svclassifier.fit(x_train,y_train)
y_pred=svclassifier.predict(x_test)
from sklearn.metrics import classification_report, confusion_matrix
print((classification_report(y_test,y_pred)))
#print(confusion_matrix(y_test,y_pred))