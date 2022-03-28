import pyautogui as pa
import pyperclip as clip

# 메모장 활성화, 최소화 된 창에는 불가능
aa = pa.getWindowsWithTitle('제목 없음')[0].activate()

#  키보드 입력
# write('문자'[,interval=초]) - 한글자당 interval초만큼의 간격으로 '문자'입력
pa.write('Test Typing With Python', interval=0.1)
# 키 조합
# hotkey(키1, 키2[,키3, 키4, ....]) -> 키1 누르고 2누르고 2때고 1때는 순서로 작동
pa.hotkey('ctrl','a')

# 한글입력 : 함수정의하여 사용하면 편함
clip.copy('한글 타이핑 테스트')
pa.hotkey('ctrl','v')