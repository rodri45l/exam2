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

    def test_dice_cheat(self):
        """Test dice cheat"""
        player = Player.Player("RODRI45Z")
        exp = player.score == 99
        self.assertTrue(exp)
    
    def test_sum_turnscore(self):
        player = Player.Player("RODRI45Z")
        player.turn_score = 1
        player.sum_turn_score()
        exp = player.score == 100
        self.assertTrue(exp)
    
    def test_change_name(self):
        player = Player.Player("RODRI45Z")
        player.change_name("Pete")
        exp = player.name == "Pete"
        self.assertTrue(exp)
