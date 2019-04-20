from random import random  #第二个random是函数
points=1000000   #总点数
num=0  #落入到曲线以下的点数
for i in range(points):
    x,y=random(),random()
    if y<x*x:
        num=num+1
print("积分是：{:.5f}".format(num*1.0/points))
