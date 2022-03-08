"""Dice Unittest"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from telnetlib import SB
from diceGame import Scoreboard
from diceGame import Player
import unittest
from unittest.mock import patch
from unittest import mock
import pickle
from diceGame import Bcolors as B


class TestScoreboard(unittest.TestCase):
    """Scoreboard testing class"""

    def test_scoreboard(self):
        '''Test Scoreboard class'''
        scoreboard = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        self.assertIsInstance(scoreboard, Scoreboard.Scoreboard)

    @patch("builtins.print")
    def test_print_scoreboard(self, mock):
        """Test print_scoreboard func"""
        scoreboard = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        sb = scoreboard.scoreboard
        str="Scoreboard\n\
##############################################################\
############################################"
        for key, item in sb.items():
            wr = item[0]/item[1]
            str += f"\n{B.Bcolors.OKGREEN}{key}: Matches won: {item[0]} Matches\
played: {item[1]} Winrate: {(wr*100):.2f}%"
        scoreboard.print_scorebard()
        mock.assert_called_with(str)
    
    def test_save_scoreboard(self):
        """Test save_scoreboard func"""
        player = Player.Player("Test")
        player.Won = True
        scoreboard = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard.update_player(player)
        sb = scoreboard.scoreboard
        scoreboard.save_scoreboard()
        with open("./diceGame/scoreboard.pickle", "rb") as handle:
            sb2 = pickle.load(handle)
        self.assertEqual(sb, sb2)


    
    
    
    def test_init(self):
        with self.assertRaises(FileNotFoundError):
            pass
    
    def test_print_scorebard(self):
        pass
