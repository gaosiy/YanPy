import itertools
import pandas as pd
import numpy as np
# list(itertools.product(['A', 'B'], ['C', 'D'], ['E','F','G']))
# 或者使用
# 组合多组参数，生成唯一的index。
all_list = [['A', 'B'], ['C', 'D']]
A = list(itertools.product(*all_list))
print(A)
B = pd.Series(A)
print(B)

# 离散化连续数据
state_discrete_bins = 20
bp = 0.1
bp_extent = [0.05, bp, 0.26]
state_space = np.arange(0, state_discrete_bins, 1)
out = pd.cut(bp_extent, state_discrete_bins, labels=state_space)
state = out[1]
print(state)