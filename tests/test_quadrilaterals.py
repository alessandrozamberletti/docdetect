# -*- coding: utf-8 -*-
from unittest import TestCase, main

from docdetect.quadrilaterals import _common_line_exists, _add_if_loop


class TestQuadrilaterals(TestCase):
    #
    #        ----A-----
    #        |        |
    #    ----B---     |
    #    |      |     |
    #    C      D     |
    #    |      |     |
    #    ----E---     |
    #        ---------F
    #
    def setUp(self):
        self.neighbours = {'a': ['b', 'f'],
                           'b': ['a', 'c', 'd'],
                           'c': ['b', 'e'],
                           'd': ['b', 'e'],
                           'e': ['c', 'd', 'f'],
                           'f': ['a', 'e']}

    def test_add_if_loop(self):
        seen = ('a', 'b', 'c')
        cycles = []
        _add_if_loop('d', self.neighbours, seen, cycles)
        self.assertEqual([], cycles)
        seen = ('b', 'c', 'e', 'd')
        cycles = []
        _add_if_loop('d', self.neighbours, seen, cycles)
        self.assertEqual([seen], cycles)
        seen = ('a', 'b', 'c', 'e', 'f')
        cycles = []
        _add_if_loop('f', self.neighbours, seen, cycles)
        self.assertEqual([seen], cycles)
        seen = ('a', 'b', 'c', 'e')
        cycles = []
        _add_if_loop('e', self.neighbours, seen, cycles)
        self.assertEqual([], cycles)

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
