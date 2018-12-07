# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math


def detect_lines(im, rho=1, theta=np.pi/90, hough_thr=65, group_similar_thr=30):
    lines = cv2.HoughLines(image=im, rho=rho, theta=theta, threshold=hough_thr)
    if lines is None:
        return []
    lines = _cvhoughlines2list(lines)
    if group_similar_thr != 0:
        lines = _group_similar(lines, group_similar_thr)
    return lines


def _group_similar(lines, thr):
    lines = sorted(lines, key=lambda line: line[0])
    lines_unique = []
    for to_add in lines:
        if not _is_duplicated(to_add, lines_unique, thr):
            lines_unique.append(to_add)
    return lines_unique


def _is_duplicated(line, lines, thr):
    return any(abs(math.fabs(line[0]) - math.fabs(_line[0])) < thr for _line in lines)


def _cvhoughlines2list(lines):
    # line[0][0] = rho
    # line[0][1] = theta
    return [(line[0][0], line[0][1]) for line in lines]

