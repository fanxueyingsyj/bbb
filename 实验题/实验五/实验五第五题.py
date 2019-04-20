#import csv
fo=open("实验五第五题.csv","a")
ls=["jbjii 123","\n hghg 124"]
fo.write("".join(ls)+"\n")
fo.close()

f=open("实验五第五题.csv","r")
lst=[]
for line in f:
    line = line.replace("\n","")
    lst = line.split(",")
    lns = ""
    for s in lst:
        lns += "{}\n".format(s)
    print(lst)
f.close()

