# use numpy create MxN matrix, 5*10
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
import numpy as np
import matplotlib.pyplot as plt

# create array
s = np.zeros(10)
# create matrix
s = np.zeros((5, 10))

# use specify row and column
# change num 0 row and all column
s[0, :] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 求解复数的模和相位，模为平方和开根号，相位为arctan(b/a),rad
x = 4 + 6j
fz, xw = np.abs(x), np.angle(x)

# python 一维数组的秩为（x,）
# python 一维数组reshape时无法调用 .reshape，需要使用np.reshape的形式，如果是numpy创建的数组则可以直接reshape
z = [1, 2, 3, 4, 5]
z = np.reshape(z, (5, 1))
print(np.shape(z))

x = np.zeros(5)
x = x.reshape((5, 1))
print(np.shape(x))

# 生成100个点，间距为0.5
t = np.arange(100) * 0.5
t = np.arange(1, 10, 1, dtype=np.int8)

# 求数组中部分数据的均值
a = np.arange(6)
part = a[2:6]  # [2 3 4 5]
mean = np.mean(part)
