# -*- coding: utf-8 -*-
import numpy as np


def find_corners(lines, im):
    height, width = im.shape[:2]
    corners = []
    vertex_id = 0
    for line1 in lines:
        rho1, theta1 = line1
        for line2 in lines:
            rho2, theta2 = line2
            if lines_are_same(line1, line2):
                continue
            a = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
            b = np.array([[rho1], [rho2]])
            try:
                # aX = b, solve for x
                x0, y0 = np.round(np.linalg.solve(a, b))
                x0, y0 = int(x0), int(y0)

                angle = np.abs(theta1 - theta2) * 180 / np.pi
                if angle < 45 or x0 < 0 or y0 < 0 or x0 > width or y0 > height:
                    continue
                if not already_present(x0, y0, corners):
                    corners.append([vertex_id, line1, line2, x0, y0])
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
    return line1 == line2
