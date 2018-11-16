# -*- coding: utf-8 -*-
from cv2 import HoughLines
from numpy import pi, abs
from math import fabs


def detect_lines(im, rho=1, theta=pi/90, hough_thr=65, group_similar=True, group_similar_thr=30):
    lines = HoughLines(image=im, rho=rho, theta=theta, threshold=hough_thr)
    if lines is None:
        return []
    lines = _cvhoughlines2list(lines)
    if group_similar:
        lines = _group_similar(lines, group_similar_thr)
    return lines


def _group_similar(lines, group_similar_thr):
    lines = sorted(lines, key=lambda line: line[0])
    lines_unique = []
    for rho1, theta1 in lines:
        found = False
        for rho2, theta2 in lines_unique:
            if abs(fabs(rho1) - fabs(rho2)) < group_similar_thr:
                found = True
                break
        if not found:
            lines_unique.append(_line(rho1, theta1))
    return lines_unique


def _cvhoughlines2list(lines):
    return [_line(*line[0]) for line in lines]


def _line(rho, theta):
    return rho, theta
