from PIL import ImageGrab
import pyautogui, time # 게임조작시 딜레이를 매크로와 맞추기 위한 타임모듈

 # 게임 상 라인이 좌, 우 두 곳 이며, 이를 저장해서 경로를 분석
 # 바로 위 경로에 장애물이 있으며 False 없으면 True를 저장.
 # 이동 시 다음 트랙을 보고 True일 시에만 이동

 # 800X600 해상도 454,746에 게임 창이 위치할 경우에 한정한 소스
 # 심화 : 창 좌표를 딴 후 해상도를 계산하고 트랙의 좌표를 자동으로 계산하여 초기화 -> 완전 자동화

# 라인분석
left_track = []
right_track = []

# 현재 플레이어 위치이며, 좌측에서 시작하므로 초기값은 left
side = "left"

# 좌상X,Y / 우하X,Y로 인식 범위를 지정한다
left_point=(761, 1032, 784, 1079)
right_point=(955, 1032, 977, 1079)
replay_bnt=(864,1289)

# 리플레이 버튼 클릭
def replay() :
    pyautogui.click(replay_bnt)
    time.sleep(2)

# 트랙 위치 잡기
def init() :
    replay() # 어차피 시작해야하므로 플레이함수를 넣어줌
    # 검사할 영역을 받아와 변수에 저장
    global left_init, right_init # 함수 외부에서 사용을 위한 전역선언
    left_init = ImageGrab.grab(left_point)
    right_init = ImageGrab.grab(right_point)
    
    # 작동검사를 위한 실 파일 저장
    # left_init.save('left.jpg')
    # right_init.save('right.jpg')
    
    # 처음에는 장애물이 없으므로 양쪽다 트루로 초기화
    left_track.append(True)
    right_track.append(True)


def getTrack() :
    # 다다음 트랙을 캡쳐
    look_left = ImageGrab.grab(left_point)
    look_right = ImageGrab.grab(right_point)

    # 기존 표본과 비교값을 트랙에 추가 : 비교적 시간이 오래 걸리는 작업
    left_track.append(look_left==left_init)
    right_track.append(look_right==right_init)
    
    # 장애물 여부에 따른 True, False값 작동 확인
    # print("Left :",left_track)
    # print("Right :",right_track)

def cut() :
    global side
    L,R = left_track.pop(0), right_track.pop(0)
    if L and R : # 양쪽 다 장애물이 없을 경우 : 현재 자신의 위치에서 속행
        pyautogui.press(side)
    elif L : # 왼쪽 장애물 없음
        pyautogui.press('left')
        side='left'
    elif R : # 오늘쪽 장애물 없음
        pyautogui.press('right')
        side='right'

# Main
init()
while True :
    getTrack()
    cut()