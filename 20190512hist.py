#绘制二维条形直方图
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
plt.hist(x,10)
plt.show()
