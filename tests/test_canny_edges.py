# -*- coding: utf-8 -*-
from unittest import TestCase, main
from tests import im_folder
from cv2 import imread
from os.path import join
from numpy import unique, sort
from numpy.testing import assert_array_equal

from docdetect.canny_edges import detect_edges, preprocess, find_characters


class TestCannyEdges(TestCase):
    def setUp(self):
        im_path = join(im_folder, 'sample.jpg')
        self.im = imread(im_path)

    def test_detect_edges_correct_shape_and_values(self):
        edges = detect_edges(self.im)
        self.assertEqual(2, len(edges.shape))
        self.assertEqual(self.im.shape[:-1], edges.shape)
        self.assertEqual(2, len(unique(edges)))
        assert_array_equal([0, 255], sort(unique(edges)))

    def test_preprocess_correct_shape(self):
        preprocess_im = preprocess(self.im, True, 3)
        self.assertEqual(2, len(preprocess_im.shape))

    def test_find_characters(self):
        characters = find_characters(self.im)
        self.assertEqual(377, len(characters))
        for character in characters:
            self.assertEqual(2, character.shape[-1])


if __name__ == "__main__":
    main()
