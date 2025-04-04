import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from email.mime.application import MIMEApplication

sender_email = 'l56267969@gmail.com'
app_password = 'kzyewhunzuvvmqyt'
receiver_email = 'yusuk199@naver.com'

file_path = 'Intermediate/auto_mail/2023082524_이유석.pdf'

subject = '구글 메일 전송 테스트'
html_body = """
<h2 style="color:green;">안녕하세요!</h2>
<p>이 메일은 <b>HTML 형식</b>과 <b>파일 첨부</b>가 포함된 파이썬 자동 메일입니다.</p>
"""

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject']= subject
msg.attach(MIMEText(html_body,'html'))

if os.path.exists(file_path):
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(file_path)}",
        )

        msg.attach(part)
else:
    print(f'파일이 존재하지 않음:{file_path}')

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print('이메일 전송 성공')
except Exception as e:
    print(f'이메일 전송실패{e}')