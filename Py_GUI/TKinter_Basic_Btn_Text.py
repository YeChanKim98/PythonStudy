from tkinter import *

root = Tk() # Tkinter객체 생성

root.title('TK inter_Basic_Btn_Text')
root.iconbitmap('icon/lengmen.ico') # 창 아이콘 설정
# root.geometry("1080x680") # 창 크기
root.geometry("780x600+1400+880") # 창 크기 + 플로팅 위치(x+y)
#root.resizable(False, False) # X,Y의 크기 조정 불가

btn1 = Button(root, text='Button01') # 적용할 프레임 및 버튼 값을 준다
# pack를 통해서 적용한다
# side 옵션으로 위치를 지정할 수 있다
# fill 옵션으로 x,y값을 주어 크기를 늘릴 수 있다, 만약 both를 주면 최대로 커진다
# expand옵션에 참거짓을 주어 요구되지 않은 공간을 사용할 수 있다
btn1.pack()

# width, height 속성을 통해서 버튼의 크기를 조정할 수 있다.
btn2 = Button(root, width=20,height=5,text='Button02_Button02_Button02_Button02')
btn2.pack()

# padx,y 속성을 통해서 버튼내부 값과 프레임의 마진을 줄 수 있다.
btn3 = Button(root, padx=20,pady=20,text='Button03_Button03_Button03_Button03')
btn3.pack()

# fg,bg 속성을 통해서 버튼내부 폰트 색과 배경색을 설정할 수 있다
btn4 = Button(root,fg="white",bg='black',text='Button04')
btn4.pack()

# 이미지를 객체에 저장하여 버튼 이미지로써 넣어줌
# 버튼함수에 바로 경로를 넣을 수 없음 : 포토 객체가 아니므로
photo = PhotoImage(file="check.png")
btn5 = Button(root,image=photo)
btn5.pack()

# 일반 텍스트 입력 : 한줄코딩 가능
# Label(root, text='Label_01').pack()
label1 = Label(root, text='Label_01')
label1.pack()

# 이미지를 객체에 저장하여 레이블로 출력
photo2 = PhotoImage(file="check.png")
label2 = Label(root,image=photo2)
label2.pack()

# 버튼에 동작부여 : 레이블의 설정을 바꾸어 텍스트 변경
def btn_click() :
    label1.config(text='Hi Im Label_01')
    global photo3 # 바뀌긴 하지만 함수를 나가는 순간 가비지 컬렉터에 의해 수거되므로 전역변수로 선언
    photo3 = PhotoImage(file="x.png")
    label2.config(image=photo3)

btn6 = Button(root,text='Available',command=btn_click)
btn6.pack()


root.mainloop() # 화면이 닫히지 않게 계속 띄워두기 위함

