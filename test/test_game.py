"""Dice Unittest"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Game
import unittest
from unittest.mock import patch
import pickle

class TestDice(unittest.TestCase):
    """Dice testing class"""

    def test_Dice(self):
        '''Test Dice class'''
        game = Game.Game()
        self.assertIsInstance(game, Game.Game())
    