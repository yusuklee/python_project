import cv2
from pyzbar.pyzbar import decode

cap =cv2.VideoCapture(0) #0번 웹캠 연결

print("카메라를 켜고 QR 코드를 보여주세요. 종료하려면 'q'를 누르세요.")

while True:
    ret, frame = cap.read() #ret은 true나 false로 연결여부를알려줌 frame은 화면인듯?
    if not ret:
        break

    decoded_objs = decode(frame) #화면해석한객체가 decoded_objs
    for obj in decoded_objs:
        points=obj.polygon #꼭지점 위치 알려주는거 근데 여기서는 필요없음
        (x,y,w,h)=obj.rect #x,y는 좌표 w는 너비 h는 높이 QR code의 위치와 크기를 알려주는것
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        data=obj.data.decode('utf-8')
        print("QR 코드 내용:",data)

        cv2.imshow("QR 코드 리더기",frame)# 내 컴퓨터 화면에 'QR 코드 리더기'라는 창을 띄우고, 거기에 카메라 영상을 실시간으로 보여주는 것
        if cv2.waitkey(1)& 0xFF ==ord('q'):
            break

cap.release() #카메라 연결해제 
cv2.destroyAllWindows() #창닫기