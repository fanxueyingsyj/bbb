from math import *
while 1:
    str=input("")
    e,v=str.split(' ',1)
    D=eval(e)
    V=eval(v)
    if(D==0&V==0):
      break
    d=pow(pow(D,3)-6*V/pi,1/3)
    print("{:.3f}".format(d))
