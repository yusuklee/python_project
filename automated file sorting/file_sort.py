import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

TARGET_FOLDER = Path("C:/Users/USER/Desktop/old_files")
DAYS_THRESHOLD = 7
NOW = datetime.now()

def get_destination(file: Path):
    name = file.name.lower()
    ext = file.suffix.lower()

    if "img" in name:
        return TARGET_FOLDER / "Images"
    elif ext == ".jpg":
        return TARGET_FOLDER / "Pictures"
    elif ext == ".pdf":
        return TARGET_FOLDER / "Documents"
    elif ext == ".zip":
        return TARGET_FOLDER / "Archives"
    return None

def organize_files():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 파일 정리 시작")
    for file in TARGET_FOLDER.iterdir():
        if file.is_file():
            last_modified = datetime.fromtimestamp(file.stat().st_mtime)
            if NOW - last_modified > timedelta(days=DAYS_THRESHOLD):
                dest = get_destination(file)
                if dest:
                    dest.mkdir(exist_ok=True)  
                    try:
                        shutil.move(str(file), str(dest / file.name))
                        print(f"Moved: {file.name} → {dest.name}/")
                    except Exception as e:
                        print(f"Error moving {file.name}: {e}")
    print("정리 완료!\n")

if __name__ == "__main__":
    organize_files()