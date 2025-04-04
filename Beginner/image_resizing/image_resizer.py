from PIL import Image
import os

count =1
os.makedirs('resized_images_folder',exist_ok=True)
for filename in os.listdir('images'):
    if filename.lower().endswith(('.jpg','.jpeg','.png')):
        resize_image=Image.open(os.path.join('images',filename)).resize((600,400))
        file_path=os.path.join('resized_images_folder',f"{os.path.splitext(filename)[0]}.jpeg")
        resize_image.save(file_path)
        print(f'{count}: {file_path} 저장완료!')
        count = count+1

        