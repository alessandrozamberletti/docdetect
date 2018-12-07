# -*- coding: utf-8 -*-
from unittest import TestCase, main

from docdetect.intersections import _angle_are_similar, _coords_are_valid, _already_present, _find_intersection_coords


class TestIntersections(TestCase):
    def test_angle_is_valid(self):
        self.assertEqual(False, _angle_are_similar((0, 0.26), (0, 0.08), 10))
        self.assertEqual(True, _angle_are_similar((0, 0.26), (0, 0.08), 11))

    def test_coordinates_are_valid(self):
        self.assertEqual(True, _coords_are_valid((1, 1), 10, 10))
        self.assertEqual(False, _coords_are_valid((-1, 1), 10, 10))
        self.assertEqual(False, _coords_are_valid((1, -1), 10, 10))
        self.assertEqual(False, _coords_are_valid((10, 1), 10, 10))
        self.assertEqual(False, _coords_are_valid((1, 10), 10, 10))
        self.assertEqual(False, _coords_are_valid((11, 1), 10, 10))
        self.assertEqual(False, _coords_are_valid((1, 11), 10, 10))

    def test_already_present(self):
        intersections = [{'coords': (0, 0)},
                         {'coords': (1, 1)},
                         {'coords': (2, 2)}]
        self.assertEqual(True, _already_present((0, 0), intersections))
        self.assertEqual(True, _already_present((1, 1), intersections))
        self.assertEqual(True, _already_present((2, 2), intersections))
        self.assertEqual(False, _already_present((0, 1), intersections))
        self.assertEqual(False, _already_present((1, 0), intersections))

    def test_find_intersection_coords(self):
        self.assertEqual((0, 1), _find_intersection_coords((0, 0), (1, 1)))
        self.assertEqual((0, 0), _find_intersection_coords((0, 0), (0, 1)))
        self.assertEqual((0, 0), _find_intersection_coords((0, 1), (0, 0)))
        self.assertEqual((-1, -1), _find_intersection_coords((1, 0), (0, 0)))
        self.assertEqual((-1, -1), _find_intersection_coords((0, 0), (1, 0)))
        self.assertEqual((-1, -1), _find_intersection_coords((0, 0), (0, 0)))


if __name__ == "__main__":
    main()
