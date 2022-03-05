"""Dice Unittest"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Game
import unittest
from unittest.mock import patch
import pickle
from unittest import mock
from diceGame.Bcolors import Bcolors

class TestGame(unittest.TestCase):
    """ Game Testing class """
    DIVIDER = "===================================================================\
======================================="
    def test_Game(self):
        '''Test Dice class'''
        game = Game.Game()
        self.assertIsInstance(game, Game.Game)
    
#     @mock.patch("builtins.print")
#     def test_showOptionMenu(self, mock):
#         """Test show option menu """
#         game = Game.Game()
#         game.showOptionMenu("7")
#         str = f"{Bcolors.HEADER}{self.DIVIDER}\n\
# {Bcolors.UNDERLINE}Please 7 enter:{Bcolors.NOT_UNDERLINED}"
#         mock.assert_called_with(str)

#     def test_createPlayer(self):
#         """ Test creating player """
#         game = Game.Game()
#         game.createPlayer("1")
#         str = '\x1b[95m==========================================================================================================\x1b[96m\nIn this game wins the first player to reach 100 points\x1b[96m\nPlayers take turns to roll a single dice as many times as they wish,\
# \nadding all roll results to a running total, but losing their gained score for the turn if they roll a 1.\n\x1b[95m=========================================================================================================='
#         mock.assert_called_with(str)