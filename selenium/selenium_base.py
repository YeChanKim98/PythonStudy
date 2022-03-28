from selenium import webdriver #셀레니움 중 웹 드라이버를 임포트
import time
from selenium.webdriver.common.keys import Keys # 엔터 컨트롤 등의 특수키를 이용하기 위한 임포트

driver = webdriver.Chrome('chromedriver') # 크롬함수가 따로 있으며, 드라이버만 잡아주면 된다 : 경로가 다르면 풀 경로를 작성(확장자 생략가능)
driver.get("https://www.youtube.com/") # 드라이버를 통해 작업할 웹 주소 연결

time.sleep(1) # 너무 빠르면 로봇임을 추측할 수 있으므로 자연스럽게 딜레이를 부여한다
#사실 전용함수가 있음

# 검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//*[@id="search"]') # 개발자도구를 통해서(우클릭 - 카피 - xpath) 검색창의 xpath를 카피해서 이용

# search 변수에 저장된 곳에 값을 전송
search.send_keys()
time.sleep(1)

# 입력했으니 엔터를 쳐야한다 : 각 키를 입력하기위한 상수가 정의 되어있음
search.send_keys(Keys.ENTER)