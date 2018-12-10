# -*- coding: utf-8 -*-
from unittest import TestCase, main
import numpy as np

import docdetect.intersections as intersections


class TestIntersections(TestCase):
    def test_angles_are_similar(self):
        self.assertEqual(False, intersections._angles_are_similar((0, 0.26), (0, 0.08), 10))
        self.assertEqual(True, intersections._angles_are_similar((0, 0.26), (0, 0.08), 11))

    def test_coordinates_are_valid(self):
        self.assertEqual(True, intersections._coords_are_valid((1, 1), 10, 10))
        self.assertEqual(False, intersections._coords_are_valid((-1, 1), 10, 10))
        self.assertEqual(False, intersections._coords_are_valid((1, -1), 10, 10))
        self.assertEqual(False, intersections._coords_are_valid((10, 1), 10, 10))
        self.assertEqual(False, intersections._coords_are_valid((1, 10), 10, 10))
        self.assertEqual(False, intersections._coords_are_valid((11, 1), 10, 10))
        self.assertEqual(False, intersections._coords_are_valid((1, 11), 10, 10))

    def test_already_present(self):
        _intersections = [{'coords': (0, 0)},
                          {'coords': (1, 1)},
                          {'coords': (2, 2)}]
        self.assertEqual(True, intersections._already_present((0, 0), _intersections))
        self.assertEqual(True, intersections._already_present((1, 1), _intersections))
        self.assertEqual(True, intersections._already_present((2, 2), _intersections))
        self.assertEqual(False, intersections._already_present((0, 1), _intersections))
        self.assertEqual(False, intersections._already_present((1, 0), _intersections))

    def test_find_intersection_coords(self):
        self.assertEqual((0, 1), intersections._find_intersection_coords((0, 0), (1, 1)))
        self.assertEqual((0, 0), intersections._find_intersection_coords((0, 0), (0, 1)))
        self.assertEqual((0, 0), intersections._find_intersection_coords((0, 1), (0, 0)))
        self.assertEqual((-1, -1), intersections._find_intersection_coords((1, 0), (0, 0)))
        self.assertEqual((-1, -1), intersections._find_intersection_coords((0, 0), (1, 0)))
        self.assertEqual((-1, -1), intersections._find_intersection_coords((0, 0), (0, 0)))

    def test_find_intersections_base(self):
        im = np.zeros((100, 100, 1), dtype=np.uint8)
        lines = [(50, 50), (10, 5)]
        expected_intersection = [{'id': 0, 'lines': ((50, 50), (10, 5)), 'coords': (53, 5)}]
        self.assertEqual(expected_intersection, intersections.find_intersections(lines, im))

    def test_find_intersections_duplicate(self):
        im = np.zeros((100, 100, 1), dtype=np.uint8)
        lines = [(50, 50), (10, 5), (50, 50), (10, 5)]
        expected_intersection = [{'id': 0, 'lines': ((50, 50), (10, 5)), 'coords': (53, 5)}]
        self.assertEqual(expected_intersection, intersections.find_intersections(lines, im))

    def test_find_intersections_invalid(self):
        im = np.zeros((100, 100, 1), dtype=np.uint8)
        lines = [(5, 5), (1, 5)]
        self.assertEqual([], intersections.find_intersections(lines, im))

    def test_find_intersections_empty(self):
        im = np.zeros((100, 100, 1), dtype=np.uint8)
        self.assertEqual([], intersections.find_intersections([], im))


if __name__ == "__main__":
    main()
