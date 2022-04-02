import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)
cx, cy, w, h = 100, 100, 200, 200
while True:
    # 계속해서 이미지를 불러와서 영상을 보여준다
    success, img = cap.read()
    # 이미지 좌우 반전
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        l, info, _ = detector.findDistance((lmList1[9][0], lmList1[9][1]),(lmList1[12][0], lmList1[12][1]), img)
        if lmList1[5][1] > lmList1[6][1] and lmList1[14][1] > lmList1[13][1] and lmList1[18][1] > lmList1[17][1] and lmList1[9][1] < lmList1[10][1]:
            print('욕설')

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()