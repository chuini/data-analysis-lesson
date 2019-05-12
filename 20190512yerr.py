#绘制误差棒图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#用来显示负号


error = np.random.randn(10)#定义误差列
y = pd.Series(np.sin(np.arange(10)))#均值数据列
y.plot(yerr = error)
plt.show()

