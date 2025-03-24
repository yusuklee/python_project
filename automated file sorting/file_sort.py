import os
import shutil
import time
import glob
import sqlite3

DAY_OLD = 15
DOWNLOADS_PATH= os.path.join(os.path.expanduser('~'), "Downloads")

CHROME_USER_DATA = os.path.join(
    os.environ['LOCALAPPDATA'], "Google", "Chrome", "User Data", 'Profile 1'
)


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

def clear_chrome_history():
    history_path = os.path.join(CHROME_USER_DATA, "History")

    try:
        if os.path.exists(history_path):
            os.remove(history_path)
            print("크롬 방문기록 삭제완료")
    except Exception as e:
        print(f" 크롬 방문기록 삭제 실패{e}")

def clear_chrome_cache():
    cache_path = os.path.join(CHROME_USER_DATA, "Cache")
    print(f"🧪 캐시 경로: {cache_path}")  # 이거 추가!

    try:
        if os.path.exists(cache_path):
            shutil.rmtree(cache_path)
            print("크롬 캐시 삭제 완료")
        else:
            print("❌ Cache 폴더 없음")
    except Exception as e:
        print(f"크롬 캐시 삭제 실패: {e}")

if __name__=="__main__":
    print("정리시작")

    delete_old_files(DOWNLOADS_PATH)
    clear_chrome_history()
    clear_chrome_cache()

    print('모든 작업 완료')