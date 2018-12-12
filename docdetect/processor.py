import cv2

import docdetect


def process(im):
    im = cv2.bitwise_not(im)
    edges = docdetect.detect_edges(im, blur_radius=7)
    lines_unique = docdetect.detect_lines(edges)
    _intersections = docdetect.find_intersections(lines_unique, im)
    return docdetect.find_quadrilaterals(_intersections)


def draw(rects, im):
    area = -1
    best = None
    for rect in rects:
        x, y = zip(*rect)
        width = max(x) - min(x)
        height = max(y) - min(y)
        if width * height > area:
            best = rect
            area = width * height

    if best is not None:
        cv2.line(im, best[0], best[1], (255, 0, 255), thickness=5, lineType=8)
        cv2.line(im, best[1], best[2], (255, 0, 255), thickness=5, lineType=8)
        cv2.line(im, best[2], best[3], (255, 0, 255), thickness=5, lineType=8)
        cv2.line(im, best[3], best[0], (255, 0, 255), thickness=5, lineType=8)

    return im
