# coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#——————————————————导入数据——————————————————————
f = open('test.csv')
df = pd.read_csv(f)         #读入股票数据
data = np.array(df['max'])  #获取最高价序列
data = data[::-1]#反转，使数据按照日期先后顺序排列
# 以折线图展示data
plt.figure()
plt.plot(data)
plt.show()