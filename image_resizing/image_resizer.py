from PIL import Image
import os

input_folder = 'input_images'
output_folder = 'output_images'
new_size = (400,300)
output_foramat = 'JPEG'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png','.jpg','.jpeg','.bmp','.gig')):
        input_path=os.path.join(input_folder,filename)
        img = Image.open(input_path)

        resized_img = img.resize(new_size)

        base_filename = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder,f'{base_filename}.{output_foramat.lower()}')


        resized_img.save(output_path,output_foramat)
        print(f'저장 완료:{output_path}')

print("모든 이미지 처리 완료")