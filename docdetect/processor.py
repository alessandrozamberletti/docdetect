import cv2

import docdetect


def process(im):
    im = cv2.bitwise_not(im)
    edges = docdetect.detect_edges(im, blur_radius=7)
    lines_unique = docdetect.detect_lines(edges)
    _intersections = docdetect.find_intersections(lines_unique, im)
    return docdetect.find_quadrilaterals(_intersections)


def draw(rects, im, debug=False):
    if len(rects) == 0:
        return im
    if debug:
        [draw_rect(im, rect, (0, 255, 0), 2) for rect in rects]
    best = max(rects, key=_area)
    if best:
        draw_rect(im, best)
    return im


def _area(rect):
    x, y = zip(*rect)
    width = max(x) - min(x)
    height = max(y) - min(y)
    return width * height


def draw_rect(im, rect, col=(255, 0, 0), thickness=5):
    [cv2.line(im, rect[i], rect[(i+1) % len(rect)], col, thickness=thickness) for i in range(len(rect))]
