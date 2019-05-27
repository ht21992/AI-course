"""     1)load data   """
import pandas as pd
import numpy as np
orginal_data=pd.read_csv("weatherAUS.csv",low_memory=False)
"""            2)data exploratory      """
#print(orginal_data.info())
#print(data.sample(5))
#print(data.describe())
cols_to_drop=["Date","Evaporation","Sunshine","WindGustDir","WindDir9am","WindDir3pm","WindSpeed9am","WindSpeed3pm",
              "Pressure9am","Pressure3pm","Cloud9am","Cloud3pm","RISK_MM"]
data=orginal_data.drop(cols_to_drop,axis=1)
#print(data.info())
#print(data.isna().sum())

"""          3)preprocessing           """


"""in raintoday column except No or Yes we also have NA """
data["RainToday"].fillna(method="ffill",inplace=True)
data.fillna(data.mean(),inplace=True)
#print(data.isna().sum())
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["Location"]=le.fit_transform(data["Location"])
data["RainTomorrow"]=le.fit_transform(data["RainTomorrow"])
data["RainToday"]=le.fit_transform(data["RainToday"])
#print(data.info())
import matplotlib.pyplot as plt
fig,ax=plt.subplots(2,2,figsize=(5,6))
ax[0,0].hist(data["MaxTemp"],10,fc="red",ec="black")
ax[0,0].set_xlabel("MaxTemp")
ax[0,0].set_ylabel("Frequency")
ax[0,1].scatter(data["Humidity9am"],data["Rainfall"])
ax[0,1].set_xlabel("Humidity9am")
ax[0,1].set_ylabel("Rainfall")
ax[1,0].scatter(data["Temp9am"],data["Temp3pm"])
ax[1,0].set_xlabel("Temp9am")
ax[1,0].set_ylabel("Temp3pm")
ax[1,1].hist(data["Location"],10,fc="blue",ec="black")
ax[1,1].set_xlabel("Location")
ax[1,1].set_ylabel("Frequency")
#plt.show()

"""      4)features and labels     """

features=data.drop("RainTomorrow",axis=1)
label=data["RainTomorrow"]



"""            5)spiliting data   """

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(features,label,test_size=0.3,random_state=5)


"""      6)model selection """

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
RFC=RandomForestClassifier(n_estimators=300)
#GNB=GaussianNB()
#svclassifier=SVC(gamma="auto",kernel="rbf")

"""         7)model training      """
RFC.fit(x_train,y_train)
predict=RFC.predict(x_test)
#GNB.fit(x_train,y_train)
#predict=GNB.predict(x_test)
#svclassifier.fit(x_train,y_train)
#predict=svclassifier.predict(x_test)
"""    8)model evaluation  """

from sklearn.metrics import accuracy_score
print(round(accuracy_score(y_test,predict),2))

"""    9)model adjustment     """
"""
RFC with 100 estimator: 0.87
naive bayes:  0.82
SVM rbf:  0.79

"""


"""   10)model usage   """
print (predict)