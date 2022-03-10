"""Should Roll  Unittest."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from diceGame import should_roll


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
