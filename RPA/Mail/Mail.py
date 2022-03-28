import smtplib
from imap_tools import *

id = 'ssy01077@gmail.com'
pw = ''

def send() :
    with smtplib.SMTP("smtp.gmail.com",587) as smtp : # 객체를 만들어 실행

        # 초기설정
        smtp.ehlo() # 연결 수립 확인
        smtp.starttls() # 암호화 On
        smtp.login(id,pw) # 아이디와 비번은 직접입력할 수 없으며, 변수를 통해서 인자로 주어야한다

        # 내용설정
        subject = 'Mail Title'
        body = 'Main Text'
        msg = f'Subject: {subject}\n{body}' # 제목을 구분해주고 이후 엔터를 통해 본문으로 구분 짓는다

        # 메일 전송(발신자, 수신자, 메일)
        smtp.sendmail('ssy01077@gmail.com','ssy5577@naver.com',msg)

def receive() :
    mailbox = MailBox('imap.gmail.com',993)
    mailbox.login(id, pw, initial_folder='INBOX') # ID,PW,선택할 메일함

    for msg in mailbox.fetch(limit=10, reverse=True) : # True는 최근 메일 부터, False는 과거 메일부터 조회. 기본값 F
        print(msg.subject)

# 각종 조건에 따른 조건부 메일 출력
def search() :
    with MailBox('imap.gmail.com',993).login(id, pw, initial_folder='INBOX') as mailbox :
        print('미열람 메일')
        for msg in mailbox.fetch('(UNSEEN)',limit=10, reverse=True): # 안 본 메일을 가져온다
            print('{}'.format(msg.subject))

        print('\n발신자 특정 메일')
        for msg in mailbox.fetch('(FROM ssy5577@naver.com)'): # 특정인으로 부터 온 메일 출력
            print('{}'.format(msg.subject))

        print('\n텍스트 조건부 메일')
        for msg in mailbox.fetch('(TEXT "Steam")', limit=10): # 특정 문구를 포함한 메일 출력
            print('{}'.format(msg.subject))

        print('\n우회를 통한 한글 검색')
        for msg in mailbox.fetch(limit=10) :
            if '보안' in msg.subject :
                print(msg.subject)


search()