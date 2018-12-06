# -*- coding: utf-8 -*-
from unittest import TestCase, main

from docdetect.line_utils import lines_angle, lines_are_same


class TestLineUtils(TestCase):
    def test_lines_are_same(self):
        self.assertTrue(lines_are_same((0, 0), (0, 0)))
        self.assertFalse(lines_are_same((0, 0), (1, 1)))
        self.assertFalse(lines_are_same((0, 0), (0, 1)))
        self.assertFalse(lines_are_same((0, 0), (1, 0)))

    def test_lines_angle(self):
        # 0.0174533 rad = 1 degree
        self.assertAlmostEqual(1, lines_angle((0, 0), (0, 0.0174533)), places=2)
        self.assertEqual(0, lines_angle((0, 0), (0, 0)))
        # 1.5708 rad = 90 degree - 6.28319 rad = 360 rad
        self.assertAlmostEqual(270, lines_angle((0, 1.5708), (0, 6.28319)), places=2)


if __name__ == "__main__":
    main()
