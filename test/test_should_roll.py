"""Should Roll  Unittest."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from diceGame import should_roll
from collections import Counter


class test_should_roll(unittest.TestCase):
    """Should Roll testing class."""

    def test_should_roll(self):
        """Test should_roll function True."""
        exp = should_roll.should_roll(0, 0, 0)
        self.assertTrue(exp)

    def test_should_roll2(self):
        """Test should_roll function False."""
        exp = should_roll.should_roll(0, 0, 102)
        self.assertFalse(exp)

    def test_count_zeros(self):
        """Test count zeros"""
        exp = should_roll.count_zeros([0, 1, 0, 12, 30, 0])
        self.assertEqual(exp, 97)

    def test_p_win(self):
        """Test probabilities of winning"""
        exp = should_roll.p_win(99, 0, 99)
        self.assertEqual(exp, 1)
