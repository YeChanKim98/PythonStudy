from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import filedialog  # 파일 선택시 나오는 탐색기 기능을 담는 서브모듈
from PIL import Image
import os

root = Tk()
root.title("Image Combine")
root.iconbitmap('icon.ico')

# 파일 추가 : 탐색기
def add_file():
    # 옵션으로 탐색창의 이름을 정하고 튜플 형식으로 파일타입을 지정해준다 : ('항목','항목에 해당하는 타입')
    # initialdir는 탐색창 시작 위치
    # 문자열 앞에 r을 붙여 로우스트링으로 만들면 탈출문자가 필요없이 전부 문장열로 사용
    files = filedialog.askopenfilenames(title="Select Img File", \
                                        filetypes=(("PNG File", "*.png"), ("All File", "*.*")), \
                                        initialdir=r"C:\Users\김예찬\Downloads\Image")  # filename함수와 혼동하면 안 됨. name은 이름을 한자한자 따로 저장함
    # 선택한 파일 목록을 리스트에 출력
    for file in files:
        list_file.insert(END, file)

# 파일 삭제 : 탐색기
def del_file():
    for index in reversed(list_file.curselection()):  # 뒤집지않고 작은 인덱스부터 삭제하면, 인덱스가 떙겨지면서 꼬인다
        list_file.delete(index)

# 저장 경로 : 탐색기
def save_path():
    fol_sel = filedialog.askdirectory()
    if fol_sel == '':  # 취소시 아무 행동 없음
        return
    # 기존에 선택한 경로가 있으면 삭제하고 새 경로 출력
    txt_path.delete(0, END)
    txt_path.insert(0, fol_sel)

# 이미지 통합 : 긴 코드라서 분리
def merge_img():
    try :
        # Option : Width
        img_width = cmb_width.get()
        if img_width == "Original" :
            img_width = -1
        else :
            img_width = int(img_width)
        # Option : Space
        img_space = cmb_space.get()
        if img_space == "Narrow" :
            img_space = 30
        elif img_space == "Usually" :
            img_space = 60
        elif img_space == "Wide" :
            img_space = 90
        else :
            img_space = 0
        # Option : Format
        img_format = cmb_format.get().lower() # 소문자로 치환
        # 옵션에따른 이미지 크기 처리
        images = [Image.open(x) for x in list_file.get(0, END)]
        image_size = []
        if img_width > -1 :
            image_size = [(int(img_width),int(img_width * x.size[1] / x.size[0])) for x in images]
        else : # 원본사용
            image_size = [(x.size[0],x.size[1]) for x in images]
        # Image객체는 size라는 리스트를 가지고 있으며, 각 인덱스마다 가로,세로 등의 크기를 가지고 있다
        # width = [x.size[0] for x in images]
        # height = [x.size[1] for x in images]
        width, height = zip(*(x.size for x in images)) # zip을 통해서 인자의 1번째 값인 wid끼리 묶고 hei끼리 묶어서 한번에 저장한다
        max_wid, total_hei = max(width), sum(height)  # sum은 모든 값을 더해준다
        if img_space > 0 :  # 간격 설정이 0이 아니면 (설정한 옵션 * 간격 수)의 값을 높이에 더해준다
            total_hei += (img_space * (len(images)-1))
        result = Image.new("RGB", (max_wid, total_hei), (255, 255, 255))  # 모드, 크기, 배경색을 정하여 새 이미지 생성
        y_off = 0  # 세로로 이어붙일때마다 전에 붙인 것을 기준으로 위치를 잡는데, 전에 붙인 것의 위치(오프셋)를 변수에 담아준다
        # for img in images:
        #     result.paste(img, (20, y_off))
        #     y_off += (int(img.size[1]) + 70)  # 오프셋 설정 : 다음 작업 때 위치를 정하기 위해 필요함
        for idx, img in enumerate(images): # 이너미터는 현재 몇번째 실행인지 튜플의 형태로 값과 같이 반환해준다
            if img_width > -1 : # 원본유지가 아닐경우 이미지 비율 적용
                img = img.resize(image_size[idx])
            result.paste(img, (0, y_off)) # 이미지를 (x,y)값에 붙여넣기
            y_off += (int(img.size[1]) + img_space)  # 오프셋 설정 : 다음 작업 때 위치를 정하기 위해 필요함
            prgs = (idx + 1) / len(images) * 100  # 퍼센트 계산
            p_var.set(prgs)
            pb.update()
        # 포맥 옵션 적용하여 이미지 저장
        file_name = "Combine."+img_format
        spath = os.path.join(txt_path.get(), file_name)  # 경로와 이름을 합친다 : 파일의 최종 풀네임이 나옴
        result.save(spath)  # 만든 풀네임으로 저장
        msgbox.showinfo('Result', 'Image Combine Success')
    except Exception as err :
        print(err)
        msgbox.showerror("ERROR",err)

# 시작
def start():
    # 옵션 값 받아오기
    cmb_space.get()
    cmb_format.get()
    cmb_width.get()
    # 타겟파일 존재 여부 확인
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Select Img File !")
        return
    if len(txt_path.get()) == 0:
        msgbox.showwarning("Warning", "Select Save Directory !")
        return
    merge_img()

# 파일 선택 프레임
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)
btn_add_file = Button(file_frame, text='Add File', width=10, height=2, command=add_file)
btn_add_file.pack(side='left')
btn_del_file = Button(file_frame, text='Cancel Add', width=10, height=2, command=del_file)
btn_del_file.pack(side='right')

# 파일 항목 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)
scroll = Scrollbar(list_frame)
scroll.pack(side='right', fill='y')
list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scroll.set)
list_file.pack(side='left', fill='both', expand=True)
scroll.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="Save Path")  # 제목작성이 가능한 프레임
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)
txt_path = Entry(path_frame)
txt_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4)  # ipadx,y는 이너, 즉 내부 크기이다. 사용시 입력창의 크기 조절 가능
btn_path = Button(path_frame, text='Select', width=10, command=save_path)
btn_path.pack(side='right', padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text='Option')
option_frame.pack(padx=5, pady=5, ipady=5)
# 가로 넓이 옵션(전부 외쪽 정렬하여 가로로 배치)
lb_width = Label(option_frame, text="Width", width=8)
lb_width.pack(side='left', padx=5, pady=5)
opt_width = ["Original", "1024", "800", "640"]  # 옵션항목
cmb_width = ttk.Combobox(option_frame, state='readonly', values=opt_width, width=8)  # 옵션 선택
cmb_width.current(0)  # 기본 첫번째 목록 선택
cmb_width.pack(side='left', padx=5, pady=5)
# 간격 옵션
lb_space = Label(option_frame, text="Space", width=8)
lb_space.pack(side='left', padx=5, pady=5)
opt_space = ["None", "Narrow", "Usually", "Wide"]  # 옵션항목
cmb_space = ttk.Combobox(option_frame, state='readonly', values=opt_space, width=8)  # 옵션 선택
cmb_space.current(0)  # 기본 첫번째 목록 선택
cmb_space.pack(side='left', padx=5, pady=5)
# 파일 포맷 옵션
lb_format = Label(option_frame, text="Format", width=8)
lb_format.pack(side='left', padx=5, pady=5)
opt_format = ["PNG", "JPG", "BMP"]  # 옵션항목
cmb_format = ttk.Combobox(option_frame, state='readonly', values=opt_format, width=8)  # 옵션 선택
cmb_format.current(0)  # 기본 첫번째 목록 선택
cmb_format.pack(side='left', padx=5, pady=5)

# 진행도 프레임
frame_prog = LabelFrame(root, text='Progress')
frame_prog.pack(fill='x', padx=5, pady=5, ipady=5)
p_var = DoubleVar()
pb = ttk.Progressbar(frame_prog, maximum=100, variable=p_var)
pb.pack(fill='x', padx=5, pady=5)

# 시작 종료 프레임
frame_run = Frame(root)  # 제목 불필요
frame_run.pack(fill='x', padx=5, pady=5)
btn_close = Button(frame_run, padx=5, pady=5, width=10, text="Close", command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)
btn_start = Button(frame_run, padx=5, pady=5, width=10, text="Start", command=start)
btn_start.pack(side='right', padx=5, pady=5)

root.resizable(False, False)
root.mainloop()