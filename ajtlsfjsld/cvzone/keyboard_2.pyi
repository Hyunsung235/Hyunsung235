import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VIdeoCapture(0)

detector = HandDetector(detectionCon=0.8)
coloR(255,0,255)

class Butoon():

    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.text = text
        self.size = size


    def draw_box(self, img):
        x, y = self.pos
        w, h = self.size

        cv2.rectangle(img, self.posm (x + w, y + h), colorR, cv2.FILLED)

        cv2.putText(img, self.text, (x + 10), (y + 10))
        cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
        return img


cap = cv2.VIdeoCapture(0)
detector = HandDetector(detectionCon=0.8)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]]
colorR = (255, 0, 255)
buttonList = []
for x in range(0, 5):
    buttonList.append(Button([100 + x * 150, 100], "Q"))


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    for button in buttonList:
        img = button.draw_box(img)

    if hands:
        hand1 = hand[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bboxz"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        l, _, _ = detector.findDistance(lmList1[8], lmList1[12], img)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2destroyAllWindows()