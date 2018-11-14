# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math


def detect_lines(im, rho=1, theta=np.pi/90, hough_thr=65, angle_thr=30):
    lines = cv2.HoughLines(image=im, rho=rho, theta=theta, threshold=hough_thr)
    if lines is None:
        return []
    lines = _group_similar(lines, angle_thr)
    return lines


def _group_similar(lines, angle_thr):
    lines_unique = []
    for line in lines:
        rho1, theta1 = line[0]
        found = False
        for already_added in lines_unique:
            rho2, theta2 = already_added[0]
            if np.abs(math.fabs(rho1) - math.fabs(rho2)) < angle_thr:
                found = True
                break
        if not found:
            lines_unique.append(line)
    return lines_unique
