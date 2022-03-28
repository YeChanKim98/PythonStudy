from tkinter import *

root = Tk()
root.title('TK inter_Basic_Btn_Text')
root.geometry("780x600+1400+880")

# 텍스트 에어리어 입력창 : 무한입력 가능 양식
txt = Text(root, width=30, height=5)
txt.pack()
# Place Holder : 빈 칸에 입력시 END,0 둘중 하나 선택
txt.insert(END,'Place Holder')

# 한줄 텍스트 입력창 : 엔터 기능 없으며, 주로 ID,PW등을 받는데 사용
e = Entry(root, width=30)
e.pack()
e.insert(0, "Input ID")

# 버튼을 통한 Text요소 제어
def get_txt() :
    # 텍스트 에어리어 : 1번째줄 0번째 컬럼부터 END까지 반환받아 출력 : 컬럼은 띄어쓰기로 구분되는 요소
    print(txt.get("1.0",END))
    # 엔트리는 인자가 필요없다
    print(e.get(),"\n")
    # 반환 받은 후 텍스트 내용 삭제 : 삭제는 둘다 범위를 지정해 줘야함
    txt.delete("1.0",END)
    e.delete(0,END)
btn = Button(root,text="Go", command=get_txt)
btn.pack()



root.mainloop()

