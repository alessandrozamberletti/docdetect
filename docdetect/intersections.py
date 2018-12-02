# -*- coding: utf-8 -*-
import numpy as np
from docdetect.line_utils import lines_angle


def find_intersections(lines, im, angle_thr=45):
    height, width = im.shape[:2]
    intersections = []
    vertex_id = 0
    for line1 in lines:
        for line2 in lines:
            if not _angle_is_valid(line1, line2, angle_thr):
                continue
            coords = _find_intersection_coordinates(line1, line2)
            if _coordinates_are_valid(coords, width, height) and not already_present(coords, intersections):
                intersections.append({'id': vertex_id, 'lines': (line1, line2), 'corner': coords})
                vertex_id += 1
    return intersections


def _find_intersection_coordinates(line1, line2):
    rho1, theta1 = line1
    rho2, theta2 = line2
    a = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
    b = np.array([[rho1], [rho2]])
    try:
        # aX = b, solve for x
        x, y = np.round(np.linalg.solve(a, b))
        return int(x), int(y)
    except np.linalg.linalg.LinAlgError:
        # singular matrix
        return -1, -1


def already_present(coords, intersections):
    if any(intersection['corner'] == coords for intersection in intersections):
        return True
    return False


def _angle_is_valid(line1, line2, angle_thr):
    return lines_angle(line1, line2) > angle_thr


def _coordinates_are_valid(coords, width, height):
    return 0 < coords[0] < width and 0 < coords[1] < height
