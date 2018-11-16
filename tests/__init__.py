# -*- coding: utf-8 -*-
from os.path import dirname, realpath, join
from cv2 import imread


pwd = dirname(realpath(__file__))
im_folder = join(pwd, 'res')
im = imread(join(pwd, 'res', 'sample.jpg'))
