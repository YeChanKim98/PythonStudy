from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
data01 = bs(html.text,'html.parser')
data02 = data01.find('div',{'class':'list_area daily_all'})
data03 = data02.findAll('ul') # 리스트에 넣어서 인덱스를 통한 요일 조정 가능

day = 100
choice = input("Day? ")

if choice == '월' :
    day = 0
elif choice == '화' :
    day = 1
elif choice == '수' :
    day = 2
elif choice == '목' :
    day = 3
elif choice == '금' :
    day = 4
elif choice == '토' :
    day = 5
elif choice == '일' :
    day = 6
data04 = data03[day].findAll('a',{'class':'title'})

title_list=[] #정보를 이용하기 유용하게 변수에 입력

for i in range(len(data04)) :
    title_list.append(data04[i].text)