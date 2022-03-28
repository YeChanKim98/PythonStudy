from selenium import webdriver # 웹 가동
from selenium.webdriver.common.keys import Keys # 특수키 및 각종 키들을 변수로 사용 할 수 있다

browser = webdriver.Chrome('../../../Driver_module/chromedriver.exe')
browser.get('Target URL')

# xpath 사용시, 따옴표 안에 따옴표가 오게되면 에러가 생길 수 있으므로, 가장 큰 따옴표안에 //를 넣어서 내부에 있는 따옴표를 문자로써만 읽게한다.
link = browser.find_element_by_link_text('target') # 링크가 들어간 target 이라는 텍스트 요소르 지정
link.get_attribute('href') # 링크 텍스트의 링크값 반환(요소 지정을 통한 해당 요소 값 반환)
link.click() # 링크 클릭

search = browser.find_element_by_id('search_window') # 입력창 찾기(예시코드는 검색창을 가리킴)
search.send_keys('search_keyword') # 지정한 인풋창 및 요소에 입력하고자 하는 키 전송
search.clear() # 인풋창에 입력된 값 제거

screen_shot = browser.save_screenshot('scsh.jpg') # 현재 창을 지정한 이름으로 스샷저장한다

# 엘리멘트로만 지정 후 어떠한 검색 조건인지 지정이 가능
browser.find_element(By.ID,'target')
browser.find_element(By.XPATH,'target')

browser.close() # 현재 탭 종료
browser.quit() # 브라우저 종료

# 원하는 요소가 iframe 안에 있을 때는 일반적인 방법으로 find_ele 를 통해서 찾을 수 없다.
# 따라서 원하는 요소가 있는 iframe 으로 작업범위를 지정해주어야한다
browser.switch_to_frame('frameID') # 프레임 아이디를 통해서 해당 영역에서 작업이 가능하다
# 원하는 프레임으로 접근하면 기존에 작동하지 않던 xpath 가 작동할 것이다!
browser.switch_to.default_content() # 프레임 안에서 작업 후 다시 원래 프레임(기본 콘텐츠)으로 빠져나온다

radio = browser.find_element_by_xpath('xpath') # 원하는 라디오 버튼을 변수에 지정
radio.is_selected() # 해당 요소가 선택된 상태인지 T/F로 반환

# Xpath에서 셀렉트의 옵션 선택 방법
# 1. 인덱스를 통한 옵션 선택 : 일반적으로 /option[0]의 방식으로 리스트 처럼 인덱스를 통해서 옵션에 접근이 가능하다
# 2. 텍스트값 지정을 통한 옵션 선택 : /option[text()="value"] 정수형 인덱스가 아닌 텍스트 속성의 값을 통해서 옵션을 선택한다
# 3. 텍스트값 패턴을 통한 옵션 선택 : /option[text(), "pattern"] 완전히 일치하는 값이 아닌 지정한 타입에, 지정한 문구를 보유한 옵션을 선택한다

# 자바스크립트 실행
browser.execute_script('window.scrollTo(0,1080)') # 스크롤을 내리도록 스크립트를 작성하여 실행
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 동적 스크롤을 통한 스크롤링 -> 고정값이 아닌 스크롤의 높이값을 받아와서 해당 값만큼(최대) 내린다
scroll_height = browser.execute_script('return document.body.scrollHeight') # 현재 페이지의 스크롤 높이를 반환받아서 변수에 저장

# 핸들 컨트롤 : 브라우저 창(탭)마다 고유한 핸들이 부여된다. 이를통해 여러작업을 제어할 수 있다
handle = browser.current_window_handle # 핸들정보 저장
browser.switch_to.window(handle) # 핸들 정보를 이용해서 지정 창(탭)으로 전환
browser.close() # 현재창을 닫고
browser.switch_to.window(handle) # 원래 창으로 복귀