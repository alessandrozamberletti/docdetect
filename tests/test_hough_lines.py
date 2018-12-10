# -*- coding: utf-8 -*-
from tests import im
from unittest import TestCase, main
from random import randint
from numpy import zeros, uint8

import docdetect.canny_edges as canny_edges
import docdetect.hough_lines as hough_lines


class TestCannyEdges(TestCase):
    def setUp(self):
        self.edges = canny_edges.detect_edges(im)

    def test_detects_correct_format(self):
        self.assert_format_is_correct(hough_lines.detect_lines(self.edges, group_similar_thr=30))
        self.assert_format_is_correct(hough_lines.detect_lines(self.edges, group_similar_thr=30))

    def assert_format_is_correct(self, lines):
        self.assertTrue(isinstance(lines, list))
        [self.assertTrue(isinstance(line, tuple)) for line in lines]

    def test_detects_group_similar_reduces_number_of_lines(self):
        raws = hough_lines.detect_lines(self.edges, group_similar_thr=0)
        groupeds = hough_lines.detect_lines(self.edges, group_similar_thr=30)
        self.assertGreater(len(raws), len(groupeds))
        self.assertEqual(15, len(raws))
        self.assertEqual(7, len(groupeds))

    def test_format_cvhoughlines2list(self):
        self.assertEqual([(0, 1), (2, 3)], hough_lines._cvhoughlines2list([[[0, 1]], [[2, 3]]]))
        self.assertEqual([], hough_lines._cvhoughlines2list([]))
        with self.assertRaises(TypeError):
            hough_lines._cvhoughlines2list(None)

    def test_group_similar_no_duplicates(self):
        self.assert_groups_are([(0, 0), (0, 0)], [(0, 0)])
        self.assert_groups_are([(0, 0), (1, 1), (0, 0)], [(0, 0), (1, 1)])
        self.assert_groups_are([(0, 0), (0, 0), (1, 1), (1, 1)], [(0, 0), (1, 1)])
        self.assert_groups_are([(0, 0), (1, 1), (0, 0), (0, 0)], [(0, 0), (1, 1)])
        self.assert_groups_are([(0, 0), (1, 1), (0, 0), (1, 1), (0, 0)], [(0, 0), (1, 1)])

    def test_group_similar_thr_works(self):
        self.assert_groups_are([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (2, 0), (3, 0)], group_similar_thr=1)
        self.assert_groups_are([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (2, 0)], group_similar_thr=2)
        self.assert_groups_are([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (3, 0)], group_similar_thr=3)
        self.assert_groups_are([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0)], group_similar_thr=4)
        self.assert_groups_are([(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0)], group_similar_thr=100)

    def test_no_lines(self):
        empty_im = zeros((10, 10, 1), dtype=uint8)
        self.assertEqual([], hough_lines.detect_lines(empty_im))

    def test_group_similar_is_deterministic(self):
        max_rho = 100
        rnds = random_lines(42, max_rho=max_rho)
        rnds.append((0, 0))
        self.assert_groups_are(rnds, [(0, 0)], group_similar_thr=max_rho+1)

    def test_group_similar_ignores_theta(self):
        self.assert_groups_are([(0, 0), (0, 1), (0, 2)], [(0, 0)], group_similar_thr=100)

    def test_is_duplicated(self):
        self.assertTrue(hough_lines._is_duplicated((0, 0), [(0, 0)], 1))
        self.assertFalse(hough_lines._is_duplicated((0, 0), [(1, 0)], 1))
        self.assertTrue(hough_lines._is_duplicated((0, 0), [(1, 0)], 2))
        self.assertFalse(hough_lines._is_duplicated((0, 0), [], 1))

    def assert_groups_are(self, raws, expected_groupeds, group_similar_thr=1):
        self.assertEqual(expected_groupeds, hough_lines._group_similar(raws, group_similar_thr))


def random_lines(nlines, max_rho=0, max_theta=0):
    return [(randint(0, max_rho), randint(0, max_theta)) for _ in range(nlines)]


if __name__ == "__main__":
    main()
