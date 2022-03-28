from tkinter import *
import tkinter.ttk as ttk # 프로그래스바는 해당 모듈을 임포트 해야함
import time
root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x300+1400+790")

# 프로그래스바
# indeterminate모드 : 게이지가 차는 것이 아닌 바가 좌우로 움직이며 보여주는 방식
# determinate모드 : 게이지가 차는 방식으로 보여주는 방식
pb = ttk.Progressbar(root,maximum=100,mode="indeterminate")
# 지정한 초마다 바가 움직임
pb.start(2)
pb.pack()

def get_txt() :
    pb.stop()
btn = Button(root,text="Go", command=get_txt)
btn.pack()

# 동작 상태에 따른 작동 : 실제 처리 정도에 따라 바가 실행됨
# 패킹과 동시에 바가 활성화 되지 않도록 start는 제외
pbv = DoubleVar() # 소수점까지 받아와서 진행정도를 상세히 알기 위함
pb2 = ttk.Progressbar(root,maximum=100,length=150,mode="determinate",variable=pbv)
pb2.pack()

def pb_cmd() :
    for i in range(1,100):
        time.sleep(0.01)
        pbv.set(i)
        # 매 동작마다 업데이트를 하지 않으면, 모든 처리가 끝난 후 값에 대한 진행도를 보여주어 바로 100%가 된다
        pb2.update()
btn2 = Button(root,text="Go", command=pb_cmd)
btn2.pack()

root.mainloop()