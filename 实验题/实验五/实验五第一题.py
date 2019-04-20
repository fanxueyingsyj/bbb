textFile=open(r"C:\Users\fanxueying\Desktop\名单.txt","rt")
d={}
for line in textFile:
    lst=line.split()
    key=lst[0]
    value=lst[1]
    d[key]=value
textFile.close
