"""1)load data"""

import pandas as pd
orginal_data=pd.read_csv("AppleStore.csv").drop(["Unnamed: 0"],axis=1)


"""2)data exploratory"""

#print (orginal_data.info())
#print (orginal_data.sample(5))
#print (orginal_data.shape)
cols_to_drop=["id","track_name","currency","rating_count_ver","rating_count_tot","user_rating_ver","ver","cont_rating"
              ,"sup_devices.num","ipadSc_urls.num","lang.num","vpp_lic"]
data=orginal_data.drop(cols_to_drop,axis=1)
#print (data.info())
#print (data.isna().sum())


"""3)data preprocessing"""
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["prime_genre"]=le.fit_transform(data["prime_genre"])
data=data.astype(float)
#print (data.info())
import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2)
ax[0].scatter(data["prime_genre"],data["price"])
ax[0].set_xlabel("genre")
ax[0].set_ylabel("price")
ax[1].hist(data["prime_genre"],23,fc="red",ec="black")
ax[1].set_xlabel("genre")
ax[1].set_ylabel("frequency")

#mapped=zip(orginal_data["prime_genre"],data["prime_genre"])
#print (list(mapped))
#print (list(data["prime_genre"].unique()))
#print (len(data["size_bytes"].unique()))
#plt.show()
""" 
 ax[0] shows that most expensive categories are 1-music and  2-games  
 ax[1] shows that top three categories are 1-games  2-entertaiment 3-education
"""


"""   4)features and labels   """


features=data.drop("prime_genre",axis=1)
label=data["prime_genre"]



"""             5)spliting data      """


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(features,label,test_size=0.3,random_state=5)


"""  6) model selection """
from sklearn.tree import DecisionTreeClassifier
from  sklearn.ensemble import RandomForestClassifier
from  sklearn.svm import SVC
from  sklearn.naive_bayes import GaussianNB
#DTC=DecisionTreeClassifier(criterion="gini")
SVclassifier=SVC(kernel="rbf",gamma="auto")
#RFC=RandomForestClassifier(n_estimators=100)
#NB=GaussianNB()


"""  7)model training"""

#DTC.fit(x_train,y_train)
#predict=DTC.predict(x_test)

SVclassifier.fit(x_train,y_train)
predict=SVclassifier.predict(x_test)


#RFC.fit(x_train,y_train)
#predict=RFC.predict(x_test)

#NB.fit(x_train,y_train)
#predict=NB.predict(x_test)

"""     8)model evaluation"""


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predict))


"""  9)model adjustment   """

#imp_features=pd.Series(RFC.feature_importances_,index=features.columns).sort_values(ascending=False)
#print (imp_features)

"""DTC entropy :  0.38
   DTC gini :  0.36  
   svc rbf :  0.53
   svc poly: 0.1
   RFC  100 estimators: 0.39
   RFC  300 estimators: 0.38
   NB  : 0.52
   """



"""10) model usage"""
print (predict)