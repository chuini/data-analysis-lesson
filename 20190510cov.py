#计算随机矩阵的协方差
import pandas as pd
import numpy as np
d = pd.DataFrame(np.random.randn(6,5))
print(d)

print(d.cov())

print(d[0].cov(d[1]))
print(d.describe())
