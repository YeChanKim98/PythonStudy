from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter # 변수의 요소값이 몇개인지 반환해주는 함수
import time

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(100) # 브라우저의 로딩까지 대기

# 내부태그가 존재하지 않으므로 그냥 xpath만 일치하면 전부 받아오도록 함
btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')

def search_color() :

         # 컴포지션 : btns의 각 요소를 btn으로 받은 후 특정 css값을 받아 리스트 변수에 입력
        btns_rgba = [ btn.value_of_css_property('background-color') for btn in btns]


        result = Counter(btns_rgba) # 카운터로 각 인자의 갯수를 확인 : 갯수가 1인 것이 목표

        #value가 1인 것 탐색
        for key, value in result.items(): # 쌍을 key와 value의 두 변수에 넣어서 동작
            if value == 1:
                answer = key
                break
        else:
            answer = None
            print("Search Fail.") # 모든 값이 2개 이상 존재할 시

        if answer :
            index = btns_rgba.index(answer) # 1개만 있는 rgb값을 가진곳의 인덱스값을 반환
            btns[index].click() # 해당 인덱스를 지닌 태그를 클릭

start = time.time() # 현재 UTC기준시간을 변수에 입력
while time.time() - start <= 60  : # 현재시간 - 시작시간이 60초 이상의 차이가 나면 중지.
    search_color()