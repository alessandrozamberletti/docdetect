# -*- coding: utf-8 -*-
from unittest import TestCase, main

import docdetect.line_utils as line_utils


class TestLineUtils(TestCase):
    def test_lines_are_same(self):
        self.assertTrue(line_utils.lines_are_same((0, 0), (0, 0)))
        self.assertFalse(line_utils.lines_are_same((0, 0), (1, 1)))
        self.assertFalse(line_utils.lines_are_same((0, 0), (0, 1)))
        self.assertFalse(line_utils.lines_are_same((0, 0), (1, 0)))

    def test_lines_angle(self):
        # 0.0174533 rad = 1 degree
        self.assertAlmostEqual(1, line_utils.lines_angle((0, 0), (0, 0.0174533)), places=2)
        self.assertEqual(0, line_utils.lines_angle((0, 0), (0, 0)))
        # 1.5708 rad = 90 degree - 6.28319 rad = 360 rad
        self.assertAlmostEqual(270, line_utils.lines_angle((0, 1.5708), (0, 6.28319)), places=2)


if __name__ == "__main__":
    main()
