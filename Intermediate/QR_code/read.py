from pyzbar.pyzbar import decode
from PIL import Image


img = Image.open('qrcode.png')

result = decode(img)

for item in result:
    print("QR코드 내용:",item.data.decode('utf-8'))