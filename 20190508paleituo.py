import pandas as pd

data = pd.read_excel('1.xls')
pd.read_csv('1.csv',encoding = 'utf-8')

data = data[u'profit'].copy()
#data.sort(ascending = False)

import matplotlib.pyplot as plt
#plt.rcPasams['font.sans-serif'] = ['SimHei']
#plt.rcParams['axes.unicode_minus'] = False

plt.figure()
data.plot(kind='bar')
plt.ylabel(u'profit')


plt.show()

