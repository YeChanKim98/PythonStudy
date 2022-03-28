from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
data01 = bs(html.text,'html.parser')
data02 = data01.find('div',{'class':'list_area daily_all'})
data03 = data02.findAll('ul') # 리스트에 넣어서 인덱스를 통한 요일 조정 가능

li_list=[]
for data in data03:
    li_list.extend(data.findAll('li'))

for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    print(title,img_src)