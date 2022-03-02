"""Dice Unittest"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Scoreboard
import unittest
from unittest.mock import patch
import pickle

class TestScoreboard(unittest.TestCase):
    """Scoreboard testing class"""

    def test_Dice(self):
        '''Test Scoreboard class'''
        scoreboard = Scoreboard.Scoreboard()
        self.assertIsInstance(scoreboard, Scoreboard.Scoreboard)
    
