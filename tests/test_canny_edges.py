# -*- coding: utf-8 -*-
from unittest import TestCase, main
from tests import im
from numpy import unique, sort, ones, array, count_nonzero
from numpy.testing import assert_array_equal

from docdetect.canny_edges import detect_edges, _preprocess, _find_characters, _remove_characters


class TestCannyEdges(TestCase):
    def test_detect_edges_correct_shape_and_values(self):
        edges = detect_edges(im)
        self.assertEqual(2, len(edges.shape))
        self.assertEqual(im.shape[:-1], edges.shape)
        self.assertEqual(2, len(unique(edges)))
        assert_array_equal([0, 255], sort(unique(edges)))

    def test_preprocess_correct_shape(self):
        preprocess_im = _preprocess(im, True, 3)
        self.assertEqual(2, len(preprocess_im.shape))

    def test_find_characters(self):
        height, width = im.shape[:2]
        characters = _find_characters(im, int((width * height) / 1e2))
        self.assertEqual(377, len(characters))
        for character in characters:
            self.assertEqual(2, character.shape[-1])

    def test_remove_characters(self):
        character = array([[2, 3], [1, 1]])
        mask = ones((5, 5))
        self.assertEqual(25, count_nonzero(mask))
        _remove_characters([character], mask)
        self.assertEqual(23, count_nonzero(mask))
        self.assertEqual(0, mask[3, 2])
        self.assertEqual(0, mask[1, 1])


if __name__ == "__main__":
    main()
