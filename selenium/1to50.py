from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50/')
driver.implicitly_wait(150) # 브라우저의 로딩까지 대기

num = 1

def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]') # div 1-25까지 있으므로 *를 통해서 패턴을 줌 !단, 해당 태그안에 추가적으로 태그가 있어야 가능

    for btn in btns:
        print(btn.text)
        if btn.text == str(num):
            btn.click()
            num += 1
            return


# print(driver.find_element_by_xpath('//*[@id="grid"]/div'))

while num<=50:
    clickBtn()