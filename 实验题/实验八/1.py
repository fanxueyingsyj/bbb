import requests
import csv
from bs4 import BeautifulSoup 
allProblems = []
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillProblemList(soup):
    trs = soup.find_all('tr')
    for tr in trs:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleProblem = []
        for td in ltd:
            singleProblem.append(td.string)
        allProblems.append(singleProblem)
    del allProblems[0:7]

with open("POJ题目1.csv","w",newline='')as f:
    writer = csv.writer(f)
    writer.writerow(['题号','标题','通过率','日期'])
    for pageNo in range(1,31):
        allProblems=[]
        url = 'http://poj.org/problemlist?volume=%d' % pageNo
        html = getHTMLText(url)
        soup = BeautifulSoup(html,"html.parser")
        fillProblemList(soup)
        #writer.writerows(allProblems)
        print(allProblems)
