import pandas as pd
data = {'name' : ['James','pandu','Ram'],'Score' : [45,78,90],'Qualify' : ['yes','no','yes'],'Attempts' : [1,2,3]}
label = ['A','B','C']
df = pd.DataFrame(data,label)
print("series : ")
print(df)
df.replace({'name' : {'James' : 'Suresh'}},inplace = True)
print("Replace is : ")
print(df)
df['Age'] = [10,20,30]
print("Add a new colums is : ")
print(df)
f = df.columns.tolist()
print("Colum list : ",f)


