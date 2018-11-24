# -*- coding: utf-8 -*-
import numpy as np


# TODO fix corner format so that it makes more sense
def find_corners(lines, im, angle_thr=45):
    height, width = im.shape[:2]
    corners = []
    vertex_id = 0
    for line1 in lines:
        rho1, theta1 = line1
        for line2 in lines:
            rho2, theta2 = line2
            angle = np.abs(theta1 - theta2) * 180 / np.pi
            if angle < angle_thr:
                continue
            x, y = _find_intersection_coordinates(rho1, theta1, rho2, theta2)
            # TODO use set instead
            if _coordinates_are_valid(x, y, width, height) and not already_present(x, y, corners):
                corners.append([vertex_id, line1, line2, x, y])
                vertex_id += 1
    return corners


def _find_intersection_coordinates(rho1, theta1, rho2, theta2):
    a = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
    b = np.array([[rho1], [rho2]])
    try:
        # aX = b, solve for x
        x, y = np.round(np.linalg.solve(a, b))
        return int(x), int(y)
    except np.linalg.linalg.LinAlgError:
        # singular matrix
        return -1, -1


def _coordinates_are_valid(x, y, width, height):
    return 0 < x < width and 0 < y < height


# TODO _x0, _y0 becomes line, if becomes lines_are_same
def already_present(_x0, _y0, angles):
    for x in angles:
        x0 = x[-2]
        y0 = x[-1]
        if _x0 == x0 and _y0 == y0:
            return True
    return False
