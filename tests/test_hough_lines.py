# -*- coding: utf-8 -*-
from tests import im
from unittest import TestCase, main

from docdetect.canny_edges import detect_edges
from docdetect.hough_lines import detect_lines, _group_similar, cvhoughlines2list


class TestCannyEdges(TestCase):
    def setUp(self):
        self.edges = detect_edges(im)

    def test_detect_lines(self):
        pass

    def test_detect_lines_group_similar_param(self):
        raw_lines = detect_lines(self.edges, group_similar=False)
        grouped_lines = detect_lines(self.edges, group_similar=True)
        self.assertGreater(len(raw_lines), len(grouped_lines))

    def test_format_cvhoughlines2list(self):
        self.assertEqual([(0, 1), (2, 3)], cvhoughlines2list([[[0, 1]], [[2, 3]]]))

    def test_group_similar_no_duplicates(self):
        pass

    def test_group_similar_angle_similarity_thr_works(self):
        pass

    def test_group_similar(self):
        pass


if __name__ == "__main__":
    main()
