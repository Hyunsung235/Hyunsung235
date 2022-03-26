from cvzone.FaceDetectionModule import FaceDetector
import cv2
import streamlit as st

# cam 불러오는거
cap = cv2.VideoCapture(0)

# 얼굴관련 해서 만든 모델, 머신러닝(데이터)
# 인풋 -> 모델 -> 아웃풋

detector = FaceDetector()

st.title("Face Detection")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    img, bboxs = detector. findFaces(frame)

    # RGB
    # cv1, PIL, pillow
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(img)
else:
    st.write('Stopped')