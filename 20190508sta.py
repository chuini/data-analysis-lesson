#from __future__ import print_function
import pandas as pd

data = pd.read_excel('2.xls')
pd.read_csv('2.csv',encoding = 'utf-8')
dataa = data[data[u'sales(yuan)']>30000]
dataaa = data[data[u'sales(yuan)']<30000]

statistics = dataa.describe()

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min']
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%']

print (statistics )
print (dataaa.describe())
