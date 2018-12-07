# -*- coding: utf-8 -*-
from unittest import TestCase, main

from docdetect.quadrilaterals import _common_line_exists


class TestQuadrilaterals(TestCase):
    def test_common_line_exists(self):
        l0 = (0, 0)
        l1 = (0, 1)
        l2 = (1, 0)
        l3 = (1, 1)
        self.assertTrue(_common_line_exists((l0, l1), (l0, l1)))
        self.assertTrue(_common_line_exists((l0, l1), (l0, l2)))
        self.assertTrue(_common_line_exists((l0, l1), (l1, l2)))
        self.assertFalse(_common_line_exists((l0, l1), (l2, l3)))
        self.assertTrue(_common_line_exists((l0, l2), (l0, l1)))
        self.assertTrue(_common_line_exists((l1, l2), (l0, l1)))
        self.assertFalse(_common_line_exists((l2, l3), (l0, l1)))


if __name__ == "__main__":
    main()
