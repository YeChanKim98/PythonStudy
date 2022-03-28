from tkinter import *

root = Tk()
root.title('TK inter_Basic_ListBox')

# 체크박스의 값을 담아올 변수를 지정 : Tkinter내장 타입
chkvar = IntVar()
# variable에 값이 담길 변수를 지정
chk = Checkbutton(root,text="CheckBox", variable=chkvar)
chk.pack()

def get_txt() :
    #get으로 받아올 수 있으며, 체크시 1, 비체크시 0 반환
    print(chkvar.get())
btn = Button(root,text="Go", command=get_txt)
btn.pack()

root.mainloop()

