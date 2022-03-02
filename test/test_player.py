"""Dice Unittest"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Player
import unittest
from unittest.mock import patch
import pickle

class TestDice(unittest.TestCase):
    """Dice testing class"""

    def test_Dice(self):
        '''Test Dice class'''
        player = Player.Player("noname")
        self.assertIsInstance(player, Player.Player)
    