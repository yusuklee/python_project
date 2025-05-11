import qrcode
import qrcode.constants

data="알빠노"

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")
img.save("qrcode.png")
print("QR 코드가 생성되어 qrcode.png로 저장됨.")