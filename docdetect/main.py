import cv2

import docdetect


def process(im):
    im = cv2.bitwise_not(im)
    edges = docdetect.detect_edges(im)
    lines_unique = docdetect.detect_lines(edges)
    _intersections = docdetect.find_intersections(lines_unique, im)
    return docdetect.find_quadrilaterals(_intersections)
