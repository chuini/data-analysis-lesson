#计算两个列向量的相关系数
import pandas as pd


d = pd.DataFrame([range(1,8),range(2,9)])
print(d)
d.corr(method ='pearson')
s1 = d.loc[0]
s2 = d.loc[1]
print(s1)
print(s2)
print(s1.corr(s2,method= 'pearson'))

