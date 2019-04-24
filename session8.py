weathear=['Sunny','Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy']
temp=['Hot','Mild','Hot','Cool','Hot','Mild','Hot','Cool']
play=['No','No','Yes','No','No','Yes','No','Yes']

from sklearn import  preprocessing
le=preprocessing.LabelEncoder()
weathear_encoded=le.fit_transform(weathear)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
features=list(zip(weathear_encoded,temp_encoded))
print(weathear_encoded)
print(temp_encoded)
print(label)
print(list(features))
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,2]])
print('Predicted value: ',predicted)