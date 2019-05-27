import pandas as pd
import numpy as np
data=pd.read_csv("master.csv",skiprows=0)
"""
----->>>>> if i write code like below data type of year  will become object???
cols=["country","age","year","sex"]
data=pd.read_csv("master.csv",names=cols,sep=",")

"""

list_to_drop=["suicides_no","population","suicides/100k pop","country-year","HDI for year"," gdp_for_year ($) ","generation"]
data=data.drop(list_to_drop,axis=1)
#print(data.isna().sum())
#print(data.info())
#print(data.sample(5)(
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
le.fit(data["country"])
data["country"]=le.transform(data["country"])
le.fit(data["sex"])
data["sex"]=le.transform(data["sex"])
le.fit(data["age"])
data["age"]=le.transform(data["age"])
#print(data.info())

import matplotlib.pyplot as plt
fig,ax=plt.subplots(2,2)
ax[0,0].hist(data["year"],10,fc="red",ec="black",alpha=10)
ax[0,0].set_xlabel("year")
ax[0,0].set_ylabel("frequency")
"""from 2000 until 2015 we had more more suicides"""
ax[0,1].hist(data.sex,fc="blue",ec="black",alpha=0.5)
ax[0,1].set_xlabel("sex")
ax[0,1].set_ylabel("frequency")
ax[1,0].hist(data.country,20,fc="gray",ec="black")
ax[1,0].set_xlabel("country")
ax[1,0].set_ylabel("frequency")
"""country number 40 and 99 have most suicide """
ax[1,1].scatter(data.country,data["gdp_per_capita ($)"])
"""this shows that countries with better economic situation have less suicide"""
ax[1,1].set_xlabel("country")
ax[1,1].set_ylabel("gdp per capita")
#plt.show()
featuers=data.drop("country",axis=1)
label=data["country"]


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(featuers,label,test_size=0.3,random_state=5)
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
DTC=DecisionTreeClassifier(criterion="entropy",max_depth=18)
#svclassifier=SVC(kernel="rbf",gamma="auto")
DTC.fit(x_train,y_train)
predict=DTC.predict(x_test)
from sklearn.metrics import accuracy_score
"""DTC with max depth=18 and SVC with rbf kernel both have 0.999 accuracy"""
print(round(accuracy_score(y_test,predict),3))
print(predict)
