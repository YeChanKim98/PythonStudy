from selenium import webdriver
import re, os
import time
from urllib.request import urlretrieve

options = webdriver.ChromeOptions() #옵션지정 함수를 변수로 지정
options.add_argument('headless') # 변수에 headless라는 창 숨기기 옵션부여
# headless 사용시 주의 : 동적페이지의 경우 사용자의 상황에 따라 내용이 수정되는데
# headless를 사용하면, 현재 사용자의 상태를 모르므로 기본값이 나오게 된다. 즉, 한글이 영어로 나오거나 기타 문제를 야기할 수 있다.

driver = webdriver.Chrome('chromedriver' , options=options) # 옵션사용
driver.get('https://www.twitch.tv/eyejoker7/clip/BovineUgliestMouseRlyTho-Pv9Q_iAl7to70aFj?filter=clips&range=30d&sort=time') # 클립주소

time.sleep(3)

try:
    if not (os.path.isdir('video')):
        os.makedirs(os.path.join('video'))
except OSError as e: # 예외처리
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

video_url = driver.find_element_by_tag_name('video').get_attribute('src')
name_url = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h2').get_attribute('title')
title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', name_url)
urlretrieve(video_url, './video/' + title + '.mp4')

driver.close()