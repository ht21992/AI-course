import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
bankdata=pd.read_csv("bill_authentication.csv")
#print(bankdata.shape)
#print(bankdata.head)
"""bankdata.plot()
plt.show()"""
x=bankdata.drop('Class',axis=1)
y=bankdata['Class']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
#print(x_train.shape)
from sklearn.svm import SVC
svclassifier=SVC(kernel='linear')
svclassifier.fit(x_train,y_train)
y_pred=svclassifier.predict(x_test)
"""plt.plot(y_train)
plt.plot(y_pred)
plt.show()"""
from sklearn.metrics import classification_report,confusion_matrix
#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))