# -*- coding: utf-8 -*-
import numpy as np


def find_corners(lines, im):
    height, width = im.shape[:2]
    corners = []
    vertex_id = 0
    for idx_line1, x in enumerate(lines):
        rho1, theta1 = x[0]
        for idx_line2, y in enumerate(lines):
            rho2, theta2 = y[0]
            if lines_are_same(x, y):
                continue
            a = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
            b = np.array([[rho1], [rho2]])
            try:
                # aX = b, solve for x
                x0, y0 = np.linalg.solve(a, b)
                x0, y0 = int(np.round(x0)), int(np.round(y0))

                angle = np.abs(theta1 - theta2) * 180 / np.pi
                if angle < 45 or x0 < 0 or y0 < 0 or x0 > width or y0 > height:
                    continue
                if not already_present(x0, y0, corners):
                    corners.append([vertex_id, idx_line1, idx_line2, x, y, x0, y0])
                    vertex_id += 1
            except np.linalg.linalg.LinAlgError:
                pass
    return corners


def already_present(_x0, _y0, angles):
    for x in angles:
        x0 = x[-2]
        y0 = x[-1]
        if _x0 == x0 and _y0 == y0:
            return True
    return False


def lines_are_same(line1, line2):
    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    return rho1 == rho2 and theta1 == theta2
