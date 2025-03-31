import os
import shutil
import time
import glob
import sqlite3

DAY_OLD = 15
DOWNLOADS_PATH= os.path.join(os.path.expanduser('~'), "Downloads")

def is_old(filepath):
    file_time = os.path.getmtime(filepath)
    return(time.time() - file_time)>(DAY_OLD * 86400)

def delete_old_files(path):
    print(f"📂 정리 중: {path}")
    deleted=0

    for root,dirs,files in os.walk(path):
        for f in files:
            try:
                file_path = os.path.join(root,f)
                if is_old(file_path):
                    os.remove(file_path)
                    deleted=deleted+1
                    print(f"🗑️ 삭제됨: {file_path}")
            except Exception as e:
                print(f"오류: {e}")

    print(f"총 {deleted}개 파일 삭제됨")

if __name__=="__main__":

    print("정리시작")
    delete_old_files(DOWNLOADS_PATH)    
    print('모든 작업 완료')