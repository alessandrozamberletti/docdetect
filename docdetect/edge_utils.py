# -*- coding: utf-8 -*-
from cv2 import Canny, cvtColor, COLOR_BGR2HSV, COLOR_BGR2GRAY, medianBlur


def detect_edges(im):
    saturation = cvtColor(im, COLOR_BGR2HSV)[:, :, 2]
    saturation = medianBlur(saturation, 9)
    return Canny(saturation, 100, 200)
