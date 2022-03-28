from bs4 import BeautifulSoup as bs
from pprint import pprint  # print의 결과를 정돈하여 출력하여 가독성을 높여주는 패키지
import requests  # 웹 페이지 요청 패키지. java 웹과 비슷함

html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=경기도%20날씨') #원하는 페이지를 requests로 받은 후 변수에 저장
# pprint(html.text) # 출력시 텍스트 속성은 모두 출력하므로 소스가 그대로 출력되어 어지럽다

soup = bs(html.text,'html.parser')  #bs함수를 통해서 (대상,파싱형태)를 파싱한 후 변수에 넣어준다


# 원하는 것은 미세먼지의 정보이므로, 개발자 도구를 열어서 해당 정보를 가진 태그와 그 class를 대상으로 삼는다
data1 = soup.find('div',{'class':'detail_box'}) #soup중 원하는 정보를 추출하기 위해 find함수를 사용하며, div태그에 class값이 detail_box로 매칭되어있는 정보를 찾는다
# find사용시 적합한 결과가 여려개 있을 경우에는 항상 첫번째 결과만 반환한다
# 결과 미세먼지,초미세먼지,오존의 결과를 담은 div의 정보가 잘 담겼다
# 이제 3개를 각 분리하기 위해 html태그를 보면, dd라는 태그에 각 값이 감싸여 있다

data2 = data1.findAll('dd') # dd태그가 3개이므로 findAll을 사용하였으며, class의 속성은 필요가 없으므로 제외하였음
# 결과가 리스트의 형태로 반환됨

for i in range(3):
    print(data2[i].find('span',{'class':'num'}).text) #dd를 넘어 span태그 하나를 두고 3개의 데이터 분리에 성공했다. 결과에서 마지막 태그를 버리기위해 text를 이용
