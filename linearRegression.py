#导包
import numpy as np
from sklearn import linear_model

# 回归求斜率 导入模型，模型参数默认
LR = linear_model.LinearRegression()
lx = [1,2,3,4,5]
ly = [-61.6907,-52.2,-46.29,-41.96,-38.57]

lx = np.array(lx).reshape(-1,1)
ly1 = np.array(ly).reshape(-1,1)
print(ly)
#训练模型
LR.fit(lx,ly)

#打印截距
print('intercept_:%.3f' % LR.intercept_)
#打印模型系数
print('coef_:%.3f' % LR.coef_)