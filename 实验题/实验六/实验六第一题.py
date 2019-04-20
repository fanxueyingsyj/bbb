def days(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    d = month_days[month-1]
    if month==2 and ((year%4==0 and year%100!=0) or year%400==0):
        d=d+1
    return d

def layout(first,d):  #将1日到d号依次填入到frame正确的位置里
    frame=[""]*42  #42个空串构成的列表
    if first == 0:
        first = 7
    frame[first-1] = '1'
    j = first  #填的位置
    for i in range(2,d+1): #依次将2日到d日填入正确的位置
        frame[j] = str(i)
        j = j+1
    return frame

def printMonth(frame): #输出列表frame
    for i in range(42):
        print("{:>3s} ".format(frame[i]),end='')
        if (i+1)%7==0:
            print()

def oneMonth(year,month,first): #输出year年month月的日历，已经知道这月1号是星期几
    d = days(year,month) #返回这year年month月一共有多少天
    frame = layout(first,d) #返回frame列表，month月1日到d日依次填入到列表中正确的位置
    printMonth(frame)
    return (first+d)%7

def heading(month):
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    print("          {}         ".format(months[month-1]))
    print('Mon Tue Web Thu Fri Sat Sun')
    
def printCalendar(year,weekday):  #weekday：year年1月1日是星期几    
    print()
    print("=========="+str(year)+"==========")
    first = weekday #代表当前月1日是星期几
    for month in range(1,13):  #输出每个月的日历
        heading(month) #输出每个月日历的抬头，输出month月的日历，输出完毕后可以推断下个月1日是星期几
        first =  oneMonth(year,month,first)  #输出month月的日历

def leapyears(year):  #统计从1990年(含1990年)到年份year(不含year年)有多少个闰年，并返回闰年数
    count = 0
    for y in range(1900,year):
        if (y%4==0 and y%100!=0) or y%400==0:
           count = count + 1
    return count

def firstDay(year):  #提供year，返回year年1月1日是星期几
    k = leapyears(year)
    n = (year-1900)*365 + k
    return (1+n)%7   #0~6:约定好，0代表星期天，1代表星期一

def getYear():
    print("本程序打印年历")
    return int(input("请输入年份（1900后）："))

def main():  #程序入口
    year = getYear()  #I：输入
    weekday = firstDay(year) #提供year，输出year年1月1号是星期几
    printCalendar(year,weekday) #输出year年的年历，要求知道year年1号是星期几(用w表示)
    
main()
