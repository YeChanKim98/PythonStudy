import pyautogui as pa

# 카운트다운 : 콘솔에 출력도 해줌
pa.countdown(1) # 인자는 '초'

# 여러가지 메시지 창
pa.alert('Alert String','Msg_Box_Title')
res = pa.confirm('Confirm String','Msg_Box_Title')
res = pa.prompt('Prompt String','Msg_Box_Title')
print(res)
res = pa.password('Password String','Msg_Box_Title')
print(res)
