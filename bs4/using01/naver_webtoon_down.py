from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os # 각 웹 요청 / 정규식 / 시스템 명령어 모듈
from urllib.request import urlretrieve #링크와 목적폴더를 주어 목적폴더안에 링크에 해당하는 링크를 지정한 이름으로 다운 받을 수 있다

try:
    if not (os.path.isdir('image')): #경로에 image라는 디렉터리가 없을 경우 조건문 활성화
        os.makedirs(os.path.join('image')) # image폴더 생성
except OSError as e: # 예외처리
    if e.errno != errno.EEXIST: # 파일이 존재한다는 에러가 아닐경우 활성화
        print("폴더 생성 실패!")
        exit()

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#요일별 웹툰영역 추출하기
data1_list=soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

#전체 웹툰 리스트
li_list = []
for data1 in data1_list:
    #제목+썸내일 영역 추출
    li_list.extend(data1.findAll('li')) #해당 부분을 찾아 li_list와 병합
# pprint(li_list)

#각각 썸네일과 제목 추출하기
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title) #정규식 조건에 부합하는 문자는 공백으로 치환
    print(title,img_src)
    urlretrieve( img_src , './image/'+title+'.jpg') #다운받을 파일주소, 파일경로+파일명+확장자