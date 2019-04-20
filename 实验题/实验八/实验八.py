import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            ab=td.find_all('a')
            for b in ab:
                singleUniv.append(b.string)
        allUniv.append(singleUniv)
def main():
    print("{:^4}{:^40}{:^20}{:^20}{:^20}".format("题号","题目名称","通过率","提交通过数","总提交"))
    ls=[("{:^4}{:^40}{:^20}{:^20}{:^20}".format("题号","题目名称","通过率","提交通过数","总提交"))]
    f.write(' '.join(ls)+'\n')
    #pickle.dump(ls,f)
    url='http://acm.zju.edu.cn/onlinejudge/showProblems.do?contestId=1&pageNumber=1'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    for i in range(8,108):
        l=[]
        u=allUniv[i]
        x=eval(u[2])/eval(u[3])*100
        print("{:^4}{:^40}{:20.2f}%{:^30}{:^30}".format(u[0],u[1],x,u[2],u[3]))
        l=[("{:^4}{:^40}{:20.2f}%{:^30}{:^30}".format(u[0],u[1],x,u[2],u[3]))]
        f.write(' '.join(l)+'\n')
        #pickle.dump(l,f)
f=open('实验八.csv',"a")
main()
f.close()
