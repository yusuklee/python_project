import os
import shutil

TARGET_FOLDER = r"C:\Users\USER\Desktop\old_files\sibal"

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Executables': ['.exe', '.msi']
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return  'Others'


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("지정한 폴더 없음")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            category = get_category(extension)

        category_folder = os.path.join(folder_path,category)
        os.makedirs(category_folder, exist_ok=True)

        new_path = os.path.join(category_folder, filename) #이건 새로 정리한 폴더 Images같은거 안에 넣은
        #파일의 경로다

        counter = 1
        while os.path.exists(new_path):
            name, ext = os.path.splitext(filename)
            new_filename=f"{name} ({counter}){ext}"
            new_path= os.path.join(category_folder, new_filename)
            counter+=1

        shutil.move(file_path, new_path)
        print(f"{filename} -> {category}/")

    print("정리 완료")

if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)