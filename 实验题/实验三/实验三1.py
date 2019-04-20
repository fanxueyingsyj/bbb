year=eval(input("请输入4位整数："))
if year%400==0 or year%4==0 and year%100!=0:
    print("该年为闰年 ")
else:
    print("该年不是闰年（该年为平年）")
