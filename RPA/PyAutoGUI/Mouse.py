import pyautogui

# 동작 설정
pyautogui.FAILSAFE=False # 마우스가 모니터의 끝에 있을 때 동작을 정지하는데, 해당 정지없이 명령대로 작동하게 설정 - 기본이 True
pyautogui.PAUSE = 1 # 지정한 초만큼 모든 동작에 디폴트 대기시간을 부여한다

# 마우스이동_절대좌표 : moveTo(X좌표,Y좌표[,duration=초])
# duration으로 지정한 '초'단위 시간동안 좌표로 이동
pyautogui.moveTo(500,500,duration=1)

# 마우스이동_현재커서 기준 상대좌표 : move(X좌표,Y좌표[,duration=초])
# 커서 좌표 받기 : position()
pyautogui.move(500,500,duration=1)
print(pyautogui.position())
pyautogui.move(500,500,duration=1)
print(pyautogui.position())
pyautogui.move(-500,-500,duration=1)
print(pyautogui.position())

# 클릭 : click(X,Y[,duration=초,clicks=int]) / 더블 클릭 : doubleclick()
# duration초만큼의 시간동안 지정좌표로 이동 후 클릭
# 지정한 clicks만큼 클릭한다 -  클릭속도 매우빠름
# mouseDown(), mouseUp()를 합하여 click이다
pyautogui.click(200,200)
pyautogui.click(clicks=500)

# 드래그_상대좌표 : drag(X,Y[,duration=초])
# 현재위치에서 X,Y좌표만큼 드래그, 이동이 너무빨라서 인식을 놓칠 수 있으므로 duration을 주는 것을 추천
pyautogui.drag(100,10,duration=1)

# 스크롤 : scroll(int)
# 지정한 int만큼 스크롤을 움직이며, +는 위 / -는 아래 이다
pyautogui.scroll(300)

# 마우스 정보 : pyautogui.mouseInfo() - 마우스에 관한 전반적 값을 보여주는 프로그램
