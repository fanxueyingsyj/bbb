from math import factorial
print("n e")
print("- -----------")
e=0
for i in range(10):
    e=e+1/factorial(i)
    if i==0 or i==1:
        print(i,int(e))
    elif i==2:
        print(i,e)
    elif i>=3:
        print(i,"{:.9f}".format(e))
    
