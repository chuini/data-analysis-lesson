import pandas as pd

s = pd.Series([1,2,3],index=['a','b','c'])
d = pd.DataFrame([[1,2,3],[4,5,6]],columns = ['a','b','c'])
d2 = pd.DataFrame(s)

x=d.head()
y=d.describe()
pd.read_excel('2.xls')
pd.read_csv('2.csv',encoding = 'utf-8')
print(x)
print(y)
 