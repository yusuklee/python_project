import smtplib #simplt mail transfer protocol
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import logging
import time
import schedule
import requests

sender_email = 'l56267969@gmail.com'
app_password = 'kzyewhunzuvvmqyt'
to_emails = ['yusuk199@naver.com'] #cc랑 역할은 같음
cc_emails=['cc_test@example.com']
bcc_emails=['bcc_test@example.com']
all_recipients = to_emails + cc_emails + bcc_emails

file_path = 'Intermediate/auto_mail/2023082524_이유석.pdf'

subject = '구글 메일 전송 테스트 (자동화 시스템)'
MAX_RETREIS = 3 #실패해도 시도 횟수


logging.basicConfig( #로그를 어떻게 남길것인지 세팅하는 함수
    filename='mail_log.log', #로그파일이름
    level=logging.INFO, #로그 레벨
    format='%(asctime)s-%(levelname)s-%(message)s' #로그 메세지 출력 형식
)

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data =response.json()
        return data['bpi']['USD']['rate']
    except Exception as e:
        logging.warning(f'비트코인 데이터 불러오기 실패:{e}')
        return '불러오기 실패'
    
def send_email():
    price = get_bitcoin_price()
    html_body = f"""
    <h2 style="color:green;">안녕하세요!</h2>
    <p>이 메일은 <b>자동 전송</b>되는 메일입니다.</p>
    <p>비트코인 현재 가격은 <b>{price} USD</b>입니다.</p>
    """
    msg = MIMEMultipart() #텍스트만 보내면 MIMEText 첨부파일이나 html같은것도보내면 이거쓰는것
    msg['From']=sender_email
    msg['To']=', '.join(to_emails)
    msg['Cc'] = ', '.join(cc_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(html_body,'html'))


    if os.path.exists(file_path):
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream") #파일을 받을객체
            part.set_payload(attachment.read())  
            encoders.encode_base64(part) 
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(file_path)}",
            )
            msg.attach(part)
    else:
        print(f'파일이 존재하지 않음:{file_path}')


    for attempt in range(MAX_RETREIS):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com',465)
            server.login(sender_email, app_password)
            server.sendmail(sender_email,all_recipients,msg.as_string())
            server.quit()
            print('이메일 전송 성공')
            break

        except Exception as e:
            logging.error(f'이메일 전송 실패 ({attempt+1}/{MAX_RETREIS}:{e})')
            print(f'이메일 전송 실패({attempt+1}/{MAX_RETREIS}):{e}')
            time.sleep(5)

schedule.every().day.at('09:00').do(send_email)

print('스케줄러 실행중... (매일 오전 9시)')

while True:
    schedule.run_pending()
    time.sleep(60)