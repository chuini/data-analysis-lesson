# 绘制样本数据的箱型图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = np.random.randn(1000)
d = pd.DataFrame([x,x+1]).T
d.plot(kind = 'box')
plt.show()
