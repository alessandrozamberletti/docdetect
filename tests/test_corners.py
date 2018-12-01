# -*- coding: utf-8 -*-
from unittest import TestCase, main

from docdetect.corners import _angle_is_valid, _coordinates_are_valid


class TestCorners(TestCase):
    def test_angle_is_valid(self):
        self.assertEqual(True, _angle_is_valid((0, 0.26), (0, 0.08), 10))
        self.assertEqual(False, _angle_is_valid((0, 0.26), (0, 0.08), 11))

    def test_coordinates_are_valid(self):
        self.assertEqual(True, _coordinates_are_valid(1, 1, 10, 10))
        self.assertEqual(False, _coordinates_are_valid(-1, 1, 10, 10))
        self.assertEqual(False, _coordinates_are_valid(1, -1, 10, 10))
        self.assertEqual(False, _coordinates_are_valid(10, 1, 10, 10))
        self.assertEqual(False, _coordinates_are_valid(1, 10, 10, 10))
        self.assertEqual(False, _coordinates_are_valid(11, 1, 10, 10))
        self.assertEqual(False, _coordinates_are_valid(1, 11, 10, 10))


if __name__ == "__main__":
    main()
