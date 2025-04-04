import tkinter as tk
from tkinter import messagebox
import pyautogui
import os
from datetime import datetime
import threading
import time

class screenshotApp:
    def __init__(self,root):
        self.root = root #screenshotApp 의 필드 root에 매개변수로 준 root를 넘겨주겟다
        self.root.title('스크린샷 자동 저장 프로그램') #필드 root의 제목은 스크린샷 자동저장프로그램
        self.root.geometry('400x300') #애초에 매개변수로 준놈이 root로 메인 gui임

        self.is_running = False 
        self.interval = tk.IntVar(value=5)

        tk.Label(root, text='캡처 간격 (초):').pack(pady=5) #pack은 정렬 pady는 바깥 여백임
        tk.Entry(root, textvariable=self.interval, width=10).pack()

        self.start_btn=tk.Button(root,text='시작', command=self.start)
        self.start_btn.pack(pady=10)

        self.stop_btn=tk.Button(root,text='중지', command=self.stop, state = tk.DISABLED)
        self.stop_btn.pack()

        self.status_label=tk.Label(root,text='상태: 대기중')
        self.status_label.pack(pady=10)

        self.save_dir='Intermediate/screenshot/screenshot_images'
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)


    def take_screenshot(self):
        while self.is_running:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = os.path.join(self.save_dir, f'shot_{now}.png')
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            print(f"[{now}] 스크린샷 저장완료: {filename}")
            time.sleep(self.interval.get())

    def start(self):
        try:
            interval = self.interval.get() #숫자가져오기 음수나 이상한거 입력하면 올바른 숫자 입력하라고
            if interval<=0:
                raise ValueError
        except:
            messagebox.showerror('오류', '올바른 숫자를 입력해주세요')
            return
        
        self.is_running = True 
        self.status_label.config(text='상태=실행중') #설정 바꾸는거 
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        
        threading.Thread(target=self.take_screenshot, daemon=True).start()

    def stop(self):
        self.is_running = False
        self.status_label.config(text='상태=정지')
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk() #메인창생성
    app=screenshotApp(root) #메인창 인자로 넘겨주기
    root.mainloop() #창계속 뛰우기 없으면
        