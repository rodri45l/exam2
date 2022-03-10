"""Dice Unittest."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from diceGame import Player


class TestDice(unittest.TestCase):
    """Player testing class."""

    def test_Player(self):
        """Test Player class."""
        player = Player.Player("noname")
        self.assertIsInstance(player, Player.Player)

    def test_player_cheat(self):
        """Test player cheat."""
        player = Player.Player("RODRI45Z")
        exp = player.turn_score == 100
        self.assertTrue(exp)

    def test_sum_turnscore(self):
        """Test Sum turn score to score."""
        player = Player.Player("Robert")
        player.score = 15
        player.turn_score = 10
        player.sum_turn_score()
        exp = player.score == 25
        self.assertTrue(exp)
        exp = player.turn_score == 0
        self.assertTrue(exp)

    def test_change_name(self):
        """Test change name."""
        player = Player.Player("Pete")
        player.change_name("RODRI45Z")
        exp = player.name == "RODRI45Z"
        self.assertTrue(exp)

    def test_change_name_cheater(self):
        """Test if the score changes if a cheater name is given."""
        player = Player.Player("Pipi")
        player.change_name("HIVA")
        self.assertEqual(player.turn_score, 100)
