import pandas as pd
#data=['Geeks','for','Geeks','and','you']
#data1={'name':['Ali','Jhon',"Andrew"],'age':[22,23,44]}
#df=pd.DataFrame(data)
#ls=["Ali","Jhon","Andrew"]
#df=pd.DataFrame(data1,index=ls)

#print(df.loc["Jhon"])
#print(df.iloc[2])
#print(df['name'])
#print(df.iloc[1,1])
#print(df)
#print(df.mean())
#print(df.sum())
#import  matplotlib.pyplot as plt
#df.plot.bar(stacked=True)
#df.iloc[:,1].plot()
#plt.show()
#df.to_csv("a.csv")
df=pd.read_csv('a.csv',index_col=0)
print(df)