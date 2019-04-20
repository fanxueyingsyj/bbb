import sys
import string #标准库
dct = {} #空字典
for line in sys.stdin :
    if line.strip()=='DICTIONARY_DEFINE_OVER':
        break #构造字典结束
    #如果能执行到这里，意味着line是一行包含若干个正确单词的字符串
    words = line.split() #得到的words是一个列表
    for word in words:
        if len(word)>2:
            #word1是word首位字母不变，中间字母排序以后的单词
            lst1 = list(word)
            lst2 = lst1[1:-1]
            lst2.sort()
            lst1[1:-1] = lst2
            word1=''.join(lst1)
            dct[word1] = word #构造一个键值对
        else:
            dct[word] = word #is I 这种单词
                        #01234567890123456789
for line in sys.stdin : #wtaahsi:"raelly?this fcat is amzanig
    lst3 = list(line)
    #['w','t',......,'i',':'...]
    start,end=100,100 #标志着每个单词的起始位置和末尾位置
    L = len(lst3)
    for i in range(L): #检查每一个字符
        if lst3[i] in string.ascii_lowercase :
            if start == 100:
               start = i #单词起始位置
            else:
               end = 100 #将end还原为初始值
        else: #非单词字符
            if start!=100 and end == 100:
                end = i-1
            else:
                start,end = 100,100
        if start != 100 and end !=100: #找到一个打乱顺序以后的单词
            lst4 = lst3[start:end+1]
            lst5 = lst4[1:-1]
            lst5.sort()
            lst4[1:-1] = lst5 #lst4是中间部分排序以后的“单词”
            lst3[start:end+1] = list(dct[''.join(lst4)])
            start,end = 100,100
    print(''.join(lst3),end='')
