from tkinter import *
import tkinter.ttk as ttk # 프로그래스바는 해당 모듈을 임포트 해야함
import time
root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x300+1400+790")

frame = Frame(root)
frame.pack()

# 적용할 대상과 같은 프레임으로 묶어주면 편하게 관리가 가능하다
scb = Scrollbar(frame)
# file 옵션을 통해 x혹은 y축 중 어떠한 방향으로 움직일지 설정
scb.pack(side='right', fill='y')

# 옵션으로 yscrollcommand에 스크롤바 객체를 set해준다
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scb.set)
for i in range(1,32):
    listbox.insert(END, str(i)+'Day')
listbox.pack(side='left')

# 위에서 세로 스크롤바의 모습을 만들었으니 작동 할 수 있게 리스트박스의 yview기능을 준다
scb.config(command=listbox.yview)

root.mainloop()