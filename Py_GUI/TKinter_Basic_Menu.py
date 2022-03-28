from tkinter import *
import tkinter.ttk as ttk # 프로그래스바는 해당 모듈을 임포트 해야함
import time
root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x300+1400+790")

def print01():
    print('First!')

def print02():
    print('Second!')

def print03():
    print('First!')

def print04():
    print('Second!')

# 메뉴 목록을 담기위한 큰 메뉴틀 작성
menu = Menu(root)

# 메뉴안에 카테고리 별로 담을 메뉴를 하나 생성
# 테어오프는 0,1,True,alse로 on/off가 가능하며, 사용시 메뉴에 절취선이 생기며, 클릭하면 창을 분리하여 사용할 수 있다 : 디폴트 1
mf = Menu(menu, tearoff=0)
# 목적지를 root로 담아도 작동은 함
mf.add_command(label='First',command=print01)
mf.add_command(label='Second',command=print02)
mf.add_separator() # 구분선
mf.add_command(label='One',command=print03)
mf.add_command(label='Two',command=print04)
mf.add_checkbutton(label='Check_TEST')
mf.add_separator()
mf.add_command(label='Remove_All',stat='disable') # 비활성화
mf.add_separator()
mf.add_command(label='Close_All',command=root.quit) # 창 닫기

mf2 = Menu(menu, tearoff=0)

# 제작한 카테고리메뉴를 큰 메뉴틀에 'File'이라는 이름으로 명시하여 추가
menu.add_cascade(label="File", menu=mf)
menu.add_cascade(label="Help", menu=mf2)
# 현재 윈도우의 메뉴 요소는 menu객체에서 받아옴을 명시
root.config(menu=menu)
root.mainloop()