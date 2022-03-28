import smtplib
from email.mime.text import MIMEText # 메일을 다목적으로 사용할 수 있는 모듈 -> 메일의 형태는 기본적인 텍스트메일을 지원

sendEmail = "ssy5577@naver.com"
recvEmail = "ssy01077@gmail.com"
password = ""
smtpName = "smtp.naver.com"
smtpPort = 465


text = "Python Content"
msg = MIMEText(text)

msg['Subject'] ="Python Title"
msg['From'] = sendEmail
msg['To'] = recvEmail


# 네이버는 SMTP가 2개이며 현재 사용한 POP3/SMTP는 SSL 접속을 필수로 하고있다 -> IMAP/SMTP는 SSL 대기 TLS가능

# ssl 설정이므로, TLS연결을 삭제함
s=smtplib.SMTP_SSL( smtpName , smtpPort )
s.connect(smtpName,smtpPort)
s.login( sendEmail , password )
s.sendmail( sendEmail, recvEmail, msg.as_string() )
s.close()
