import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# MIMEMultipart : 다양한 미디어 형태의 메일을 지원
# MIMETextm : 메일을 다목적으로 사용할 수 있는 모듈 -> 메일의 형태는 기본적인 텍스트메일을 지원
# MIMEApplication 첨부파일을 저장할 모듈
# 동작 : 멀티파트(첨부파일을 위함)에 기본 메일(text)과 첨부파일(App)을 넣어서 이메일 발송

sendEmail = "ssy01077@gmail.com"
recvEmail = "ssy5577@naver.com"
password = ""
smtpName = "smtp.gmail.com"
smtpPort = 587

msg = MIMEMultipart()

text = "Python Content Attach Test"
contentPart = MIMEText(text)
msg.attach(contentPart)

#파일첨부
etcFileName = 'test_attach.txt'
with open(etcFileName, 'rb') as etcFD: # etcFileName에 해당하는 파일을 rb(Read Binary)형식으로 오픈하고 etcFD라 명명한다
    etcPart = MIMEApplication(etcFD.read()) # etcFD를 읽고 MIMEApplication인자로 넣어준다
    etcPart.add_header('Content-Disposition','attachment', filename=etcFileName) # 첨부파일의 정보를 헤더에 기입한다
    msg.attach(etcPart) # 메일에 추가한다


s=smtplib.SMTP( smtpName , smtpPort )
s.starttls()
s.login( sendEmail , password )
s.sendmail( sendEmail, recvEmail, msg.as_string() )
s.close()
