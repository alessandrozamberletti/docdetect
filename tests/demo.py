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
        frame = cv2.bitwise_not(frame)
        edges = docdetect.detect_edges(frame)
        lines_unique = docdetect.detect_lines(edges)
        _intersections = docdetect.find_intersections(lines_unique, frame)
        rects = docdetect.find_quadrilaterals(_intersections)

        area = -1
        best = None
        for rect in rects:
            points = (rect[0], rect[1], rect[2], rect[3])
            x, y = zip(*points)
            width = max(x) - min(x)
            height = max(y) - min(y)
            if width*height > area:
                best = rect
                area = width*height

        if best is not None:
            cv2.line(frame, best[0], best[1], (255, 0, 0), thickness=5, lineType=8)
            cv2.line(frame, best[1], best[2], (255, 0, 0), thickness=5, lineType=8)
            cv2.line(frame, best[2], best[3], (255, 0, 0), thickness=5, lineType=8)
            cv2.line(frame, best[3], best[0], (255, 0, 0), thickness=5, lineType=8)

        cv2.startWindowThread()
        cv2.namedWindow('output')
        cv2.moveWindow('output', 500, 30)
        cv2.imshow('output', frame)
        cv2.waitKey(1)
video.release()
