from tkinter import *
import tkinter.ttk as ttk # 프로그래스바는 해당 모듈을 임포트 해야함
import time
root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x300+1400+790")

# 프레임 제작
# 테두리 형태는 solid, 크기는 1
fr = Frame(root,relief='solid', bd=1)
# fill없이 expand를 사용하며, 기본적으로 주어진 xy값은 그대로 이므로 확장 되지 않는다
# fill both 후 expand 사용시 x값이 최대가 되었지만 실제 버튼의 x값에 맞춘 영역지정으로 인해 사용하지 않던 x축이 최대가 된다
fr.pack(side='left',fill='both',expand=True)

# 태그 앞에 어떤 프레임에 넣을지 인자 값으로 지정할 수 있다
Button(fr,text='First').pack()
Button(fr,text='Second').pack()
Button(fr,text='Third').pack()

root.mainloop()