import cv2
from pyzbar.pyzbar import decode

cap =cv2.VideoCapture(0)

print("카메라를 켜고 QR 코드를 보여주세요. 종료하려면 'q'를 누르세요.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    decoded_objs = decode(frame)
    for obj in decoded_objs:
        points=obj.polygon
        (x,y,w,h)=obj.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        data=obj.data.decode('utf-8')
        print("QR 코드 내용:",data)

        cv2.imshow("QR 코드 리더기",frame)
        if cv2.waitkey(1)& 0xFF ==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()