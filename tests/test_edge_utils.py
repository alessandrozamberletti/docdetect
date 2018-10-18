# -*- coding: utf-8 -*-
from unittest import TestCase, main
from tests import im_folder
from cv2 import imread
from os.path import join

from docdetect.edge_utils import detect_edges


class TestEdgeUtils(TestCase):
    def setUp(self):
        im_path = join(im_folder, 'sample.jpg')
        self.im = imread(im_path)

    def test_detect_edges(self):
        edges = detect_edges(self.im)
        self.assertEqual(2, len(edges.shape))
        self.assertEqual(self.im.shape[:-1], edges.shape)


if __name__ == "__main__":
    main()
