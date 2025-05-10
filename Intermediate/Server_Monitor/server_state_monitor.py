import psutil
import time
import logging
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

#임계치 설정
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

#로그 설정
logging.basicConfig(filename="server_monitor.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def send_slack_alert(message):
    payload = {"text": message}
    try:
        requests.post(SLACK_WEBHOOK_URL, json=payload)
    except Exception as e:
        logging.error(f"slack 전송 실패: {e}")


def log_and_alert(label, percent, threshold):#라벨부분에 cpu 메모리 디스크 이런게들갈듯
    msg = f"[ALERT] {label} 사용률 {percent}%가 임계치 {threshold}% 초과!"
    print(msg)
    logging.warning(msg) #로그에 기록
    send_slack_alert(msg) #슬랙으로 보내는거


def monitor(interval=5):
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1) #1초동안 cpu 사용률의 평균을 측정
            memory=psutil.virtual_memory() #메모리사용률
            disk = psutil.disk_usage("/")#루트 디렉터리의 디스크 사용률

            logging.info(f"cpu usage:{cpu}%")
            logging.info(f"Memory Usage:{memory.percent}%")
            logging.info(f"Disk Usage:{disk.percent}%")

            if cpu>CPU_THRESHOLD:
                log_and_alert('CPU',cpu,CPU_THRESHOLD)
            if memory.percent>MEMORY_THRESHOLD:
                log_and_alert('Memory',memory.percent,MEMORY_THRESHOLD)
            if disk.percent>DISK_THRESHOLD:
                log_and_alert('Disk',disk.percent,DISK_THRESHOLD)

            time.sleep(interval)

    except KeyboardInterrupt:
        print('모니터링 중단됨')


if __name__ == "__main__":
    send_slack_alert("✅ Slack 메시지 전송 테스트입니다.")  
    monitor(interval=5)
