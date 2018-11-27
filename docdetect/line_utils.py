# -*- coding: utf-8 -*-
import numpy as np


def lines_are_same(line1, line2):
    return line1 == line2


def lines_angle(line1, line2):
    return np.abs(line1[1] - line2[1]) * 180 / np.pi
