from sklearn import datasets
wine=datasets.load_wine()
print("Features: ",wine.feature_names)
print("Labels: ",wine.target_names)
print(wine.data.shape)
print(wine.data[0:7])
print(wine.target)
#from sklearn.cross_validation import train_test_split
#from sklearn import  preprocessing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(wine.data,wine.target,test_size=0.3,random_state=109)
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(X_train,Y_train)
y_pred=gnb.predict(X_test)
from sklearn import metrics
print("Accuracy: ",metrics.accuracy_score(Y_test,y_pred))
