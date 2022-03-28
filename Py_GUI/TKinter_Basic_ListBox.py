from tkinter import *

root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x600+1400+880")

# 리스트박스 : 콤보박스와는 다르며, 개인적으로 콤보박스가 더 UI나 사용측면에 있어서 편리하다
# Mode옵션 : extended - 여러개 선택가능 / single - 한개만 선택가능
# 높이 설정 : 1 - 한줄만 출력 / 1초과 - 지정 수만큼 목록을 출력하며, 스크롤하여 아래 목록을 더 볼 수 있다 / 0 - 전체 출력
listbox = Listbox(root, selectmode="single", height=3)
listbox.insert(0,"First")
listbox.insert(1,"Second")
listbox.insert(END,"Third") # END로 사용시 맨뒤에 어펜드
listbox.insert(END,"Forth")
listbox.pack()
# 목록삭제 : END를 쓰면 맨 뒤 항목을 삭제하고 인덱스를 쓰면 해당 인덱스를 삭제
#listbox.delete(END)
# 리스트 목록 갯수
#listbox.size()
# 리스트 값 받아오기 : 시작 인덱스와 종료 인덱스 지정하여 가져온다
#listbox.get(0,2)
# 현재 선택된 항목의 인덱스값 반환
#listbox.curselection() # 커렌트 셀렉션

# 선택한 항목 값 출력
def get_txt() :
    print(listbox.get(listbox.curselection()))
btn = Button(root,text="Txt Control", command=get_txt)
btn.pack()

root.mainloop()

