import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

ROOT_DIR = Path("C:/Users/USER/Downloads")
DEST_FOLDER = Path("C:/Users/USER/Desktop/old_files")
DAYS_THRESHOLD = 7
NOW = datetime.now()

def get_destination(file: Path):
    name = file.name.lower()
    ext = file.suffix.lower()

    
    if ext == ".pdf":
        return DEST_FOLDER / "Documents"
    return None

def organize_files():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 파일 정리 시작")
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        for fname in filenames:
            try:
                file_path = Path(dirpath) / fname
                if not file_path.exists() or not file_path.is_file():
                    continue
                last_modified= datetime.fromtimestamp(file_path.stat().st_mtime)
                if NOW - last_modified > timedelta(days=DAYS_THRESHOLD):
                    dest = get_destination(file_path)
                    if dest:
                        dest.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(file_path), str(dest/file_path.name))
                        print(f"Moved: {file_path} -> {dest}")

            except PermissionError:
                continue

            except Exception as e:
                    print(f"Error: {file_path} - > {e}")
    print("정리 완료!\n")

if __name__ == "__main__":
    organize_files()