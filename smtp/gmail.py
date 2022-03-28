import smtplib
from email.mime.text import MIMEText # 메일을 다목적으로 사용할 수 있는 모듈 -> 메일의 형태는 기본적인 텍스트메일을 지원

sendEmail = "ssy01077@gmail.com" # 보내는 곳에서 보안처리를 풀어줘야함
recvEmail = "ssy5577@naver.com" # 받는곳
password = ""
smtpName = "smtp.gmail.com"
smtpPort = 587 #smtp 포트 번호


text = "Python Content"
msg = MIMEText(text) #내용을 SMTP메일 형식에 맞게 세팅 해준다 / 뒤에 인자로 _charset=''인자를 줄 수 있음
# 이후 msg는 메일의 기본적인 정보를 담는 변수가 되어 여러 인자를 가지게 됨

msg['Subject'] ="Python Title"
msg['From'] = sendEmail
msg['To'] = recvEmail

print(msg.as_string()) # String의 형태로 볼 수 있게 치환하여 출력

# SMTP를 이용한 메일 전송의 기본 형태
s=smtplib.SMTP( smtpName , smtpPort ) # 메일 서버 연결 / (서버명, 포트)
s.starttls() #TLS 보안 처리 시작
s.login( sendEmail , password ) # 로그인(smtp ID , smtp PW)
s.sendmail( sendEmail, recvEmail, msg.as_string() ) # 발송 : (발신자, 수신자, 메일(String형))
s.close() #smtp 서버 연결을 종료합니다.
