#使用matplotlib绘制饼图

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#用来显示负号


labels = 'Frogs','hogs','dogs','logs'
sizes = [15,30,45,10]
colors = ['yellowgreen','gold','lightskyblue','lightcoral']
explode = (0,0.1,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True , startangle=90)
plt.axis('equal')
plt.show()
