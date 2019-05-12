import pandas as pd
import xlrd
import xlwt


data= pd.read_excel('2.xls')
pd.read_csv('2.csv',encoding = 'utf-8')

import matplotlib.pyplot as plt #导入图像库
plt.rcParams['font.sans-serif'] = ['SimHei']#正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #正常显示负号

plt.figure()
p = data.boxplot()#画箱线图
'''x = p['amount'][0].get_xdata()
y = p['amount'][0].get_ydata()
y.sort()'''
'''for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i],xy = (x[i],y[i], xytext = (x[i]+0.05 - 0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy = (x[i],y[i], xytext = (x[i]+0.08,y[i]))'''
plt.show()







