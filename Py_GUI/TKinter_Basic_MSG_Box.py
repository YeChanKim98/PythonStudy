from tkinter import *
import tkinter.messagebox as msgbox # 메세지박스에 대한 임포트
import time

root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x300+1400+790")

# 상황에 맞는 박스 양식의 함수를 통해서 제목, 내용을 표기하여 메시지창을 띄울 수 있다
def info():

    msgbox.showinfo('Alert','Huge Alert')

def warn():
    msgbox.showwarning('Warinning', 'Huge Warinning')

def error():
    msgbox.showerror('Error', 'Huge Error')

def ok_can():
    if msgbox.askokcancel('OK_Cancel', 'OK_Cancel') :
        print('No')
    else :
        print('Yes')
# 기타 많은 메시지 박스 양식을 지원한다

Button(root,command=info,text='Alert').pack()
Button(root,command=warn,text='Warning').pack()
Button(root,command=error,text='Error').pack()
Button(root,command=ok_can,text='Check').pack()

root.mainloop()