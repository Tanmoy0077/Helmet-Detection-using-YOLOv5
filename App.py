import streamlit as st
import cv2 as cv
import tempfile
import torch
import numpy as np

st.title("Helmet Detection on bikers using YoloV5")
f = st.file_uploader("Upload a video file : ", type=['mp4'])

if f is not None:
    with st.spinner('Please wait ...'):
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(f.read())


        cap = cv.VideoCapture(tfile.name)
        frame_width = int(cap.get(3)) 
        frame_height = int(cap.get(4))
        size = (frame_width, frame_height) 
        vidCap = cv.VideoWriter('1.webm',
                                cv.VideoWriter_fourcc(*'VP80'), 
                                30, size) 
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            vidCap.write(np.squeeze(results.render()))
        cap.release()
        vid = open('1.webm', 'rb')
        vid = vid.read()
    st.header("The Annoted Video is : ")
    st.video(vid)


