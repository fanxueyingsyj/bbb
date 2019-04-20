str=input("请输入两个正整数：")
a,b=str.split(' ',1)
A=eval(a)
B=eval(b)
lst=[A,B]
sorted(lst)
m=lst[0]
n=lst[1]
l=n%m
while l!=0:
    n=m
    m=l
    l=n%m
else:
    print("最大公约数为:",m)
x=int(A*B/m)
print("最小公倍数为:",x)
