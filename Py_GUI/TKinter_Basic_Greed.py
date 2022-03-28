from tkinter import *
import tkinter.ttk as ttk # 프로그래스바는 해당 모듈을 임포트 해야함
import time
root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x300+1400+790")

# padx,y는 글자를 기준으로 내부에 마진을 주는데, 만약 글자가 타 버튼에비해 길 경우 혼자 크기가 달라져 외관상 좋지 못함
# 따라서 width와 hight를 사용하는 것이 더 낫다
btn1 = Button(root,text="Btn_01", width=5, height=2)
btn2 = Button(root,text="Btn_02", width=5, height=2)
btn3 = Button(root,text="Btn_03", width=5, height=2)
btn4 = Button(root,text="Btn_04", width=5, height=2)
btn5 = Button(root,text="Btn_05", width=5, height=2)
btn6 = Button(root,text="Btn_06", width=5, height=2)
btn7 = Button(root,text="Btn_07", width=5, height=2)
btn8 = Button(root,text="Btn_08", width=5, height=2)
btn9 = Button(root,text="Btn_09", width=5, height=2)
btn10= Button(root,text="Btn_10", width=5, height=2)
btn11= Button(root,text="Btn_11", width=5, height=2)
btn12= Button(root,text="Btn_12", width=5, height=2)
btn13= Button(root,text="Btn_13", width=5, height=2)
btn14= Button(root,text="Btn_14", width=5, height=2)
btn15= Button(root,text="Btn_15", width=5, height=2)
btn16= Button(root,text="Btn_16", width=5, height=2) # rowspan2
btn17= Button(root,text="Btn_17", width=5, height=2)
btn18= Button(root,text="Btn_18", width=5, height=2) # colspan2

# grid사용시 소스에 pack이 있어서는 안 된다.
# rowspan과 columnspan을 사용할 수 있다
# sticky옵션을 통해 동서남북 방향으로 버튼 크기를 채우기 할 수 있다
# padx,y 옵션을 통해서 마진을 줄 수 있다
btn1.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn2.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn3.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn4.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)
btn5.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn6.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn7.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn8.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)
btn9.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn10.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn11.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn12.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)
btn13.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn14.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn15.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn16.grid(row=3,column=3,rowspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn17.grid(row=4,column=0,columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn18.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()