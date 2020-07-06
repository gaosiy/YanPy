# exit os._exit()线程中退出
# sys.exit() 主线程中退出
# import sys
# sys.exit('error')

# round and int取整
# int(): 向下取整3.7取3；
# math.ceil(): 向上取整3.2取4；
# round(): 四舍五入；
# math.modf(): 取整数部分和小数部分，返回一个元组:(小数部分,整数部分)。注意小数部分的结果有异议
import math
flo1 = 3.1415
flo2 = 3.500
flo3 = 3.789
print(int(flo1),math.ceil(flo1),round(flo1),math.modf(flo1))
print(int(flo2),math.ceil(flo2),round(flo2),math.modf(flo2))
print(int(flo3),math.ceil(flo3),round(flo3),math.modf(flo3))