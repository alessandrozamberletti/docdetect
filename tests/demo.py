# -*- coding: utf-8 -*-
from tests import im_folder
import cv2
import os

import docdetect


video_path = os.path.join(im_folder, 'black.mp4')
video = cv2.VideoCapture(video_path)
cv2.startWindowThread()
cv2.namedWindow('output')
cv2.moveWindow('output', 500, 30)
while video.isOpened():
    ret, frame = video.read()
    if ret:
        rects = docdetect.process(frame)
        frame = docdetect.draw(rects, frame)
        cv2.imshow('output', frame)
        cv2.waitKey(1)
video.release()
