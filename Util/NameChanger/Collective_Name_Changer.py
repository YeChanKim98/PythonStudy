import os
import tkinter.font
from tkinter import *
import tkinter.font as font
import tkinter.messagebox as msgbox
import natsort # 숫자 정렬용 모듈 : 숫자 파일명 정렬에 이용
# exe : pyinstaller --noconsole Collective_Name_Changer.py
# 만약 첫번째 파일을 1로 만드려하는데 뒤쪽에 1이 있으면 중복이름으로 에러

def start_chg() :
    try :
        path = sel_path.get() # 경로
        file_list = natsort.natsorted(os.listdir(path));path+='\\' # 파일목록
        # print('소트 후 파일 목록 : ', file_list)  # 점검용

        d = int(digit.get()) if digit.get() else 0 # 자릿수 : 만약 공백이면 0
        n,r = int(var.get()),int(rule.get()) # 시작번호 / 증가규칙
        f = fix.get() if fix.get() else False # 고정부
        k = n # 증가규칙 카운터

        for i in range(0,len(file_list)) :
            name = os.path.splitext(file_list[i])
            new_name = path+(str(k).zfill(d) if not f else f+str(k).zfill(d))+name[1]
            # print(path+file_list[i],' -> ',new_name)
            os.rename(path+file_list[i], new_name)
            k+=r
        msgbox.showinfo('Result', '파일이름 변경 성공('+str(len(file_list))+'개)')
    except (EOFError, NameError, IndexError, FileExistsError,ValueError, OSError, TypeError) as e:
        msgbox.showerror('ERROR',e)

# 사용법
def show_help() :
    inner_root = Tk()
    inner_root.title("사용법")
    inner_frame = Frame(inner_root)
    inner_frame.pack(fill='x', padx=5, pady=5)
    Label(inner_frame, text="사용법",font=("bold",25)).pack(fill='x', padx=5, pady=5)
    Label(inner_frame, text='1. 경로 : 이름을 변경할 파일들이 있는 폴더의 전체경로를 입력',).pack(fill='x', padx=5, pady=5)
    Label(inner_frame, text='2. 고정주 : 공백으로 둘 수 있으며, 앞에 원하는 고정 문구를 추가하길 원할시 입력한다',).pack(fill='x', padx=5, pady=5)
    Label(inner_frame, text='3. 시작 수 : 변경 후 이름을 어느 숫자부터 시작할지 지정한다',).pack(fill='x', padx=5, pady=5)
    Label(inner_frame, text='4-1. 자릿 수 : 자릿수를 지정하면 모자란 부분은 0으로 채우고 넘치는 부분은 무시한다',).pack(fill='x', padx=5, pady=5)
    Label(inner_frame, text='4-2. 자릿 수 : 0이하의 수를 작성하면 무시하고 파일명을 변경한다',).pack(fill='x', padx=5, pady=5)
    Label(inner_frame, text='5. 증가규칙 : 시작수에서 몇씩 증가할 건지 규칙을 추가할 수 있다',).pack(fill='x', padx=5, pady=5)
    inner_root.resizable(False,False)

# GUI
root = Tk()
root.title("Collective_Name_Changer")
root.iconbitmap('shuffle.ico')

# Menu
menu = Menu(root)
mf = Menu(root, tearoff=0)
menu.add_command(label="사용법", command=show_help)

# 경로지정부
frame = Frame(root)
frame.pack(fill='x', padx=5, pady=5)

lb_rule = Label(frame, text="경로", width=5)
lb_rule.pack(side='left',padx=5, pady=5)
sel_path = Entry(frame, text='', width=65)
sel_path.pack(side='left',ipady=2)

# Option_Frame
option_frame = Frame(root)
option_frame.pack(fill='both', padx=5, pady=5)

lb_fix = Label(option_frame, text="고정부", width=5)
lb_fix.pack(side='left',padx=5, pady=5)
fix = Entry(option_frame,width=10)
fix.pack(side='left',ipady=2)

lb_var = Label(option_frame, text="시작 수", width=5)
lb_var.pack(side='left',padx=5, pady=5)
var = Entry(option_frame,width=10)
var.pack(side='left',ipady=2)

lb_digit = Label(option_frame, text="자릿 수", width=5)
lb_digit.pack(side='left',padx=5, pady=5)
digit = Entry(option_frame,width=10)
digit.pack(side='left',ipady=2)
digit.insert(END,'0') # 0이하 자릿수는 기본 출력 / 아닌 값은 입력값의 남은 자릿수를 0으로 패딩

lb_rule = Label(option_frame, text="증가규칙", width=7)
lb_rule.pack(side='left',padx=5, pady=5)
rule = Entry(option_frame,width=10)
rule.pack(side='left',ipady=2)
rule.insert(END,'1')

# Btn_Frame
btn_frame = Frame(root)
btn_frame.pack(fill='both', padx=5, pady=5)

btn_start = Button(btn_frame,width=72,text="Start", command=start_chg)
btn_start.pack(ipady=2,pady=4)

root.config(menu=menu)
root.resizable(False, False)
root.mainloop()