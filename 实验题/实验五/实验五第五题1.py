import csv
with open('实验五.csv','w',newline='') as f:
    write = csv.writer(f)
    write.writerow(['姓名','学号'])
    write.writerows([['罗玉雨',631306050122],
                      ['李颖赟',631406010101],
                      ['莫天金',631406010102],
                      ['吴国平',631406010103]])
f.close

with open('实验五.csv','r') as fo:
    read = csv.reader(fo)
    for i in read:
        print(i)
fo.close
