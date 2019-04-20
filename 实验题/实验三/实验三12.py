from math import sqrt
x=eval(input("请输入一个整数："))
f=1
for i in range(2,int(sqrt(x)+1)):
    y=x%i
    if(y==0):
        f=0
        break
if f==1:
    print("Yes")
else:
    print("No")
