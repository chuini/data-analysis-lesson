#绘制一条蓝色的正弦虚线
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#用来显示负号


x = np.linspace(0,2*np.pi,50)
y = np.sin(x)
plt.plot(x,y,'bp--')
plt.show()
