#餐饮销量数据相关性分析
import pandas as pd

data = pd.read_excel('3.xls')
pd.read_csv('3.csv',encoding = 'utf-8')

print (data.corr()[u'a'])

a = data.sum()[u'a']
b = data.mean()[u'a']
c = data.var()[u'a']
d = data.std()[u'a']



print (a)
print (b)
print (c)
print (d)