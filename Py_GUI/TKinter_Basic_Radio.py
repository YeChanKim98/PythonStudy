from tkinter import *

root = Tk()
root.title('TK inter_Basic_ListBox')
root.geometry("780x600+1400+880")

# 같은 변수를 공유하는 라디오끼리 그룹핑이된다
rv = IntVar()
rd1 = Radiobutton(root, text="First", value=1, variable=rv).pack()
rd2 = Radiobutton(root, text="Second", value=2, variable=rv).pack()
rd3 = Radiobutton(root, text="Third", value=3, variable=rv).pack()

def get_txt() :
    print(rv.get())
btn = Button(root,text="Go", command=get_txt)
btn.pack()

root.mainloop()