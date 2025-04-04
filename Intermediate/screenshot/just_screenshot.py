import pyautogui
import schedule
import time
import os
from datetime import datetime

save_dir = 'Intermediate/screenshot/screenshot_images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


def take_screnshot():
    now= datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{save_dir}/screenshot_{now}.png"
    screenshot=pyautogui.screenshot()
    screenshot.save(filename)
    print(f'[{now}] 스크린샷 저장됨:{filename}')


schedule.every(5).seconds.do(take_screnshot)

print("스크린샷 자동 저장 프로그램 실행 중 (종료 Crtl+C)")
while True:
    schedule.run_pending()
    time.sleep(1)