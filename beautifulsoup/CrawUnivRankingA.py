# CrawUnivRankingA.py
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string,tds[3].string,tds[4].string,tds[5].string,tds[6].string])


def printUnivList(ulist, num):
    # print("{:^10}\t{:^6}\t{:^10}".format("名次", "公办大学", "民办大学","独立学院"))
    for i in range(num):
        u = ulist[i]
        print("{:^6}\t{:^10}\t{:^6}\t{:^10}\t{:^6}\t{:^15}\t{:^6}".format(u[0], u[1], u[2],u[3], u[4], u[5], u[6]))


def main():
    uinfo = []
    url = 'https://edu.sina.com.cn/gaokao/2020-04-03/doc-iimxyqwa4875755.shtml'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 10)  # 10 univs


main()