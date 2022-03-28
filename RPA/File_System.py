import os

# os모듈에서 경로앞에 r추가 시, \를 일반 문자로 취급하여 읽는다

def work_01() :
    os.getcwd() # 현재 작업 디렉터리 반환
    os.chdir('') # 지정 경로로 작업 디렉터리 반환
    # 기존 cmd와 이용방법이 동일하다 : 절대, 상대 모두 이용 가능

    file_path = os.path.join(os.getcwd(), '') # 두 인자 결합을 통한 파일 경로 생성 / 인자에 변수를 주어 여러번 돌려서 경로를 매번 재생성 할 때 용이
    os.path.getsize(file_path) # 인자파일의 사이즈를 저누형으로 반환(단위는 Byte)

def work_02() :
    os.listdir() # 디렉터리'만' 파일 목록을 리스트로 반환

    import fnmatch
    res = os.walk('File_System') # 디렉터리의 모든 하위 디렉터리, 파일 목록을 객체로 반환 / 출력방법 : for을 통해서 변수 3(root, dir, file)개로 받아와야한다
    pattern = '*.txt'
    for root, dirs, files in res :
        for name in file :
            # 지정한 패턴과 일치하는 파일네임을 출력
            if fnmatch.fnmatch(name,pattern) :
                print(name)

    os.path.isdir('test.txt') # 인자가 디렉터리인지
    os.path.isfile('test.txt') # 인자가 파일인지
    # 경로가 없어도 거짓

    os.path.exists() # 인자 파일 혹은 디렉터리가 존재하는가
    os.rename('기존이름','새로운이름') # 파일명 변경

def work_03() :
    import shutil # Shell Util
    shutil.copy('원본.txt','D/[바꿀이름.txt]') # 파일만 복사
    shutil.copy2() # 메타데이터까지 복사
    
    