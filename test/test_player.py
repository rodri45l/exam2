"""Dice Unittest"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Player
import unittest


class TestDice(unittest.TestCase):
    """Dice testing class"""

    def test_Player(self):
        '''Test Dice class'''
        player = Player.Player("noname")
        self.assertIsInstance(player, Player.Player)

    def test_player_cheat(self):
        """Test dice cheat"""
        player = Player.Player("RODRI45Z")
        exp = player.turn_score == 100
        self.assertTrue(exp)

    def test_sum_turnscore(self):
        player = Player.Player("RODRI45Z")
        player.sum_turn_score()
        exp = player.score == 100
        self.assertTrue(exp)

    def test_change_name(self):
        player = Player.Player("pete")
        player.change_name("RODRI45Z")
        exp = player.name == "RODRI45Z"
        self.assertTrue(exp)

    def test_change_name_cheater(self):
        """Test if the score changes if a cheater name is given"""
        player = Player.Player("Pipi")
        player.change_name("HIVA")
        self.assertEqual(player.turn_score, 100)