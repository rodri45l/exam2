"""Dice Unittest"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import cmd_game
from diceGame import Game
import unittest
from unittest import mock
import cmd


class TestCmd(unittest.TestCase):
    """CMD testing class"""

    def test_PigGame(self):
        '''Test  PigGame class'''
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        self.assertIsInstance(cmd_g, cmd_game.PigGame)
    
    # @mock.patch.object(Game.Game, "playerVsMachine")
    # def test_do_Game(self, mock):
    #     cmd_g = cmd_game.PigGame(cmd.Cmd)
    #     mock.assert_called()
