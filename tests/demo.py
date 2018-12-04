# -*- coding: utf-8 -*-
from tests import im_folder
import cv2
import os

import docdetect


video_path = os.path.join(im_folder, 'black.mp4')
video = cv2.VideoCapture(video_path)
while video.isOpened():
    ret, frame = video.read()
    if ret:
        # frame = cv2.bitwise_not(frame)
        edges = docdetect.detect_edges(frame, thr1=50, thr2=100)
        lines_unique = docdetect.detect_lines(edges)
        _intersections = docdetect.find_intersections(lines_unique, frame)
        rects = docdetect.find_quadrilaterals(_intersections)

        for rect in rects:
            cv2.line(frame, rect[0], rect[1], (0, 255, 0), thickness=5, lineType=8)
            cv2.line(frame, rect[1], rect[2], (0, 255, 0), thickness=5, lineType=8)
            cv2.line(frame, rect[2], rect[3], (0, 255, 0), thickness=5, lineType=8)
            cv2.line(frame, rect[3], rect[0], (0, 255, 0), thickness=5, lineType=8)
        cv2.startWindowThread()
        cv2.namedWindow('output')
        cv2.moveWindow('output', 500, 30)
        cv2.imshow('output', frame)
        cv2.waitKey(10)
video.release()
