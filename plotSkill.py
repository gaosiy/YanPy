import numpy as np
import matplotlib.pyplot as plt #导入
import seaborn as sns

def getdata():
    basecond = [[18, 20, 19, 18, 13, 4, 1],
                [18, 20, 19, 18, 13, 4, 1]]
    # basecond = [18, 20, 19, 18, 13, 4, 1]

    cond1 = [[18, 19, 18, 19, 20, 15, 14],
             [19, 20, 18, 16, 20, 15, 9],
             [19, 20, 20, 20, 17, 10, 0],
             [20, 20, 20, 20, 7, 9, 1],
             [20, 20, 20, 20, 7, 9, 1]]
    #
    # cond2 = [[20, 20, 20, 20, 19, 17, 4],
    #          [20, 20, 20, 20, 20, 19, 7],
    #          [19, 20, 20, 19, 19, 15, 2]]
    #
    # cond3 = [[20, 20, 20, 20, 19, 17, 12],
    #          [18, 20, 19, 18, 13, 4, 1],
    #          [20, 19, 18, 17, 13, 2, 0],
    #          [19, 18, 20, 20, 15, 6, 0]]

    # return basecond, cond1, cond2, cond3
    return basecond, cond1

data = getdata()
fig = plt.figure()
xdata = np.array([0, 1, 2, 3, 4, 5, 6])/5
linestyle = ['-', '--', ':', '-.']
color = ['r', 'g', 'b', 'k']
label = ['algo1', 'algo2', 'algo3', 'algo4']


for i in range(2):
    sns.tsplot(time=xdata, data=data[i], color=color[i], linestyle=linestyle[i], condition=label[i])

plt.ylabel("Success Rate", fontsize=25)
plt.xlabel("Iteration Number", fontsize=25)
plt.title("Awesome Robot Performance", fontsize=30)
plt.show()