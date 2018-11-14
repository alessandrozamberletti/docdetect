# -*- coding: utf-8 -*-
import cv2


def detect_edges(im, blur=False, blur_radius=9, thr1=100, thr2=200, remove_text=True):
    enhanced_im = _preprocess(im, blur, blur_radius)
    edges = cv2.Canny(enhanced_im, thr1, thr2)
    if remove_text:
        # find characters in im
        height, width = im.shape[:2]
        characters = _find_characters(im, int((width * height) / 1e2))
        # remove characters from edges mask
        for character in characters:
            x = character[:, 1]
            y = character[:, 0]
            edges[x, y] = 0
    return edges


def _find_characters(im, max_area):
    mser = cv2.MSER_create(_max_area=max_area)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    characters, _ = mser.detectRegions(gray)
    return characters


def _preprocess(im, blur, blur_radius):
    saturation = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)[..., 2]
    if blur:
        saturation = cv2.medianBlur(saturation, blur_radius)
    return saturation
