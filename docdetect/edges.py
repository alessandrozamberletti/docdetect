# -*- coding: utf-8 -*-
import cv2


def detect_edges(im, blur=9, thr1=100, thr2=200):
    saturation = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)[:, :, 2]
    saturation = cv2.medianBlur(saturation, blur)
    edges = cv2.Canny(saturation, thr1, thr2)
    return edges

