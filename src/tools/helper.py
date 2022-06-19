import requests
from bs4 import BeautifulSoup as BS
import re

def parser_news(url):
    if url:
        resp = requests.get(url)

        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_ul = soup.find('body')
            if soup:
                li_lst = main_ul.find_all('table', attrs={'width': '95%'})
                b = []
                for li in li_lst:
                    headers = li.find_all('font', attrs={'size': '3'})
                    a = []
                    for i in range(len(headers)):
                        a.append([])
                    cnt = 0
                    for header in headers:
                        headline = header.find_all('a')
                        sentence = str(headline[0]).split('>')[0]
                        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
                        a[cnt].append(s[0])
                        news = header.find_all('b')
                        news = re.sub(r'"', "'", str(news[0]))
                        a[cnt].append(re.sub(r'\<[^>]*\>', '', news))
                        cnt += 1

                    images = li.find_all('td', attrs={'width': '90'})
                    cnt = 0
                    for image in images:
                        img = image.find_all('img', attrs={'width': '80'})
                        img = str(img).split(' ')
                        if len(img) > 1:
                          img=img[3]
                          img = img[5:28]
                          img = 'http://mosday.ru/news/' + str(img)
                        else:
                            img = ''
                        if cnt < 25:
                            a[cnt].append(img)
                        cnt += 1

                    times = li.find_all('font', attrs={'face': 'Arial'})
                    cnt = 0
                    for time in times:
                        time = time.find('b')
                        time = re.sub(r'\<[^>]*\>', '', str(time))
                        a[cnt].append(time)
                        cnt += 1

                    items = li.find_all('font', attrs={'face': 'Times New Roman'})
                    cnt = 0
                    for item in items:
                        item = item.find_all('i')
                        item = re.sub(r'\<[^>]*\>', '', str(item[0]))
                        item = re.sub(r'"', "'", item)
                        a[cnt].append(item)
                        cnt += 1
                    b.append(a)
    return b