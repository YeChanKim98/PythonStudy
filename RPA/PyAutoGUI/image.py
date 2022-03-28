import pyautogui as pa
import time, sys

# pixelMatchesColor(x,y,(r,g,b)) : 특정 픽셀의 RGB값이 지정한 값과 일치 하는지

def sshot():
    img = pa.screenshot()
    img.save('screen_shot.png')

# 화면에서 지정 이미지와 같은곳의 좌표 및 크기를 받는다
# 출력값 : 왼쪽으로부터 거리, 위로부터 거리, 영역의 가로 크기 , 영역의 세로 크기
# search = pa.locateOnScreen('File.PNG') # 첫번째 한개만 반환
# for i in pa.locateAllOnScreen('File.PNG') : # 모든 값을 순차적으로 반환
#     pa.click(i,duration=0.1)

# PC에 따라 다르지만 화면을 훑어보는 과정이 있기에 '로케이트 온 스크린' 함수 작동시 오래걸릴 수 있다. 따라서 개선이 필요하다
def speed_optimize() :
    # 1. 그레이 스케일(GrayScale) : 흑백처리를 통해 약 30%의 속도 증강이 있다고 한다
    locateOnScreen('file.png', grayscale=True) # 디폴트 True
    # 2. 범위지정 : 검색을 해야할 곳만 검색하도록 검색범위를 지정한다
    locateOnScreen('file.png', region=(x, y, width, height))
    # 3. 정확도 조정 : opencv-python 모듈필요
    locateOnScreen('file.png', confidence=0.999) # 디폴트 0.999(99.9%)

# 타 프로그램의 늦은 로딩으로 인해 이미지를 찾을 수 없을 때 : 지정 시간이 다할 때 까지 계속 찾는다
def algorythem() :
    start = time.time()
    while pa.locateOnScreen('target') is None :
        pa.locateOnScreen('target')
        if time.time() - start > 10 : # 10초 이후에도 못찾을 경우
            print('Time Out')
            sys.exit()
    pa.click(pa.locateOnScreen('target'))

# 윈도우 조작
def Window_Control() :
    # title, size : 창 이름, 창 크기
    # left, right, top, bottom : 각 위치의 절대 좌표
    
    # 현재 엑티브 윈도우 출력
    fw = pa.getActiveWindow() # 사용중인 윈도우
    print(fw)
    
    # 모든 윈도우 정보 출력
    for i in pa.getAllWindows() : # 모든 윈도우
         print(i)
    
    # 타켓 윈도우 조작
    target = pa.getWindowsWithTitle('Chrome')[0] # 특정이름을 가진 윈도우 정보 받아오기
    if target.isActive == False: # 현재 활성화 되어있지 않으면
        target.activate() # 맨 앞으로 활성화
    target.maximize() # 최대화 / 최대화 확인 : isMaximazed()
    target.minimize() # 최소화 / 최th화 확인 : isMinimazed()
    target.restore() # 최소,최대도 아닌 기존 설정 사이즈로 복원
    target.close() # 닫기 / 닫을 때 질문창이 나와도 별도의 동작없음
    

Window_Control()