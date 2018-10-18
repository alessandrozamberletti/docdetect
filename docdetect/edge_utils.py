# -*- coding: utf-8 -*-
from cv2 import Canny


def detect_edges(im):
    return Canny(im, 100, 200)
