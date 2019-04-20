import sys
savein = sys.stdin  #备份sys.stdin
saveout = sys.stdout  #备份sys.stdout
fi = open("in1.txt", "r")  #以读模式打开一个输入数据文件
fo = open("out1.txt", "w")  #以写模式打开一个输出数据文件
##sys.stdin = fi  #注释这2行代码，则核心处理代码采用标准输入/输出方式
##sys.stdout = fo  #启用这2行代码，则核心处理代码采用文件输入/输出方式，核心处理代码不需作任何改动

#核心处理代码：此处以标准输入/输出方式处理数据
for line in sys.stdin:  #会自动读入多行（一直到文件尾），每一行数据
    print(sum(list(map(int,line.split()))))

sys.stdin = savein  #还原sys.stdin
sys.stdout = saveout  #还原sys.stdout
fi.close()  #关闭文件
fo.close()  #关闭文件
