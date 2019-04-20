from random import randint

def hongbao(total,num):
    
    lst1 = [] #空列表
    rest = total
    for i in range(1,num):
        b=randint(1,rest-(num-i+1))
        a = randint(1,b)
        rest -= a
        lst1.append(a)
    lst1.append(rest)
    return lst1
print(hongbao(2000,20))
