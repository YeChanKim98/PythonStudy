from tkinter import *
import tkinter.ttk as ttk # 콤보박스는 해당 모듈을 임포트 해야함
root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x300+1400+790")

# 콤보박스 : 리스트박스와는 다르게 리스트 형태의 변수로 표현을 한다
# height는 목록 전개시 보여주는 항목 수
# stat를 통해서 값을 사용자 측에서 임의로 제어할 수 없게 해야한다
val = ['Order :'+str(i) for i in range(1,32)]
cb = ttk.Combobox(root, height=5, values=val, stat="readonly")
# Place Holder : 기본값으로 보내면 그에따른 처리가 없을 시 문제가 생길 수 있으므로 준비 없이는 사용하지 않는 것이 좋다
#cb.set('Select Order')
cb.current(0) # set에 대한 기본값 처리가 없으므로, set을 사용하지 않고 0번 인덱스 값을 노출시킨다
cb.pack()

def get_txt() :
    print(cb.get())
btn = Button(root,text="Go", command=get_txt)
btn.pack()

root.mainloop()