
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import pprint

action_count = input('삭제 횟수 입력(회당 15건) : ') # 삭제 횟수 카운터

#드라이버 로딩
driver = webdriver.Chrome('chromedriver.exe')
driver.set_window_size(1080,1100)
driver.set_window_position(1350,200)

##사용할 변수 선언
#네이버 로그인 주소
url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
id='ssy5577'
pw='P@singW_&3v'

#네이버 로그인 페이지로 이동
driver.get(url)
time.sleep(2) #로딩 대기

#아이디 입력폼
tag_id = driver.find_element_by_name('id')
#패스워드 입력폼
tag_pw = driver.find_element_by_name('pw')

# id 입력
# 입력폼 클릭 -> paperclip에 선언한 id 내용 복사 -> 붙여넣기
tag_id.click()
pyperclip.copy(id)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
# 입력폼 클릭 -> paperclip에 선언한 pw 내용 복사 -> 붙여넣기
tag_pw.click()
pyperclip.copy(pw)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

#로그인 버튼 클릭c
login_btn = driver.find_element_by_id('log.login')
login_btn.click()
time.sleep(2)

#로그인이 실패했을 경우 - 예: 아이디나 패스워드 불일치
try:
    #로그인 실패창
    login_error = driver.find_element_by_css_selector('#err_common > div > p')
    print('로그인 실패 > ', login_error.text)
except:
    print('로그인 성공')
    driver.find_element_by_id('new.dontsave').click() # 로그인 시 신규 접속 미등록
    
driver.find_element_by_link_text("메일").click() # 네이버 메일 접속
driver.find_element_by_xpath('//*[@id="listBtnMenu"]/div[1]/button[6]').click() # 필터선택
driver.find_element_by_xpath('//*[@id="changeViewFilterLayer"]/div/ul[1]/li[6]').click() # 필터링 : 안읽은 메일
no_read_mail = driver.find_element_by_xpath('//*[@id="0_fol"]/span/a[2]/em').text  # 현재 않읽은 메일 수
# 기본 15개 메일 목록 출력
del_mail = 0 # 삭제한 메일
cnt = 0 # 반복카운트
print('현재 않읽은 메일 수 :',no_read_mail)
if no_read_mail != 0 :
    for cnt in range(int(action_count)) :
        driver.find_element_by_xpath('//*[@id="mailCheckAll"]').click() # 메일 전체 선택
        driver.find_element_by_xpath('//*[@id="listBtnMenu"]/div[1]/span[2]/button[2]').click() # 삭제 클릭
        del_mail += 15
        print(cnt+1,'번째 삭제 실행')
        time.sleep(1)

now_mail = int(action_count)
now_mail = int(no_read_mail)-(int(cnt)+1)*15
print('\n[삭제완료]\n삭제 횟수 : '+str(action_count)+'\n삭제 건수 : '+str(del_mail)+'\n잔여 않읽은 메일 수 : '+str(now_mail))

os.system("pause")