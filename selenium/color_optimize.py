from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(100)

start = time.time()
while time.time() - start <= 60  :
    try :
        btn = driver.find_element_by_class_name("main")
        btn.click()
    except :
        pass # 예외 발생시 아무것도 안 함