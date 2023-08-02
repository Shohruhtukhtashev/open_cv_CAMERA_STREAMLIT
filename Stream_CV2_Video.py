# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:45:26 2021

@author: malraharsh
"""
import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
    
from flask import Flask, Response
import cv2

app = Flask(__name__)
video = cv2.VideoCapture(0)


# @app.route('/')
# def index():
#     return "Default Message"

# def gen(video):
#     while True:
#         success, image = video.read()
#         ret, jpeg = cv2.imencode('.jpg', image)
#         frame = jpeg.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
#     global video
#     return Response(gen(video),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=2204, threaded=True)
