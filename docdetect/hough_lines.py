# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math


def detect_lines(im, rho=1, theta=np.pi/90, hough_thr=65, group_similar=True, angle_thr=30):
    lines = cv2.HoughLines(image=im, rho=rho, theta=theta, threshold=hough_thr)
    if lines is None:
        return []
    if group_similar:
        return _group_similar(lines, angle_thr)
    return lines


def cvhoughlines2list(lines):
    pass


def _group_similar(lines, angle_thr):
    lines_unique = []
    for line in lines:
        rho1, theta1 = line[0]
        found = False
        for already_added in lines_unique:
            if lines_are_same(line, already_added):
                continue
            rho2, theta2 = already_added[0]
            if np.abs(math.fabs(rho1) - math.fabs(rho2)) < angle_thr:
                found = True
                break
        if not found:
            lines_unique.append(line)
    return lines_unique


def lines_are_same(line1, line2):
    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    return rho1 == rho2 and theta1 == theta2
