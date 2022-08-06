import cv2
from cvzone.HandTrackingModule import HandDetector

# 카메라를 VideoCapture 객체로 가져온다.
cap = cv2.VideoCapture(0)

# Minimum Detection Confidence Threshold
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

while True:
    # 계속해서 이미지를 불러온다
    success, img = cap.read()

    # Find the hand
    # 이미지 좌우 반전
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    if hands:

        # Hand 1
        hand = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)

    # 상자 그리기
    cv2.rectangle(img, (100, 100), (200, 200), colorR, cv2.FILLED)

    # 글자 그려서 넣기
    cv2.putText(img, (100, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)


    # Display
    cv2.imshow("image", img)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindow