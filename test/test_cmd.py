"""Dice Unittest"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import cmd_game
import unittest
from unittest import mock
import cmd


class TestCmd(unittest.TestCase):
    """CMD testing class"""

    def test_PigGame(self):
        '''Test  PigGame class'''
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        self.assertIsInstance(cmd_g, cmd_game.PigGame)

    @mock.patch('Game.Game.playerVsMachine')
    def test_do_Game(self, mock):
        """Test if do_play calls playerVsMachine func."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_play('1')
        self.assertTrue(mock.called)

    @mock.patch('Game.Game.playerVsPlayer')
    def test_do_Game2(self, mock):
        """Test if do_play calls playerVsMachine func."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_play('2')
        self.assertTrue(mock.called)
    
    # Add test_do_game3. Mock print when we input wrong argument.
    # Add test_scoreboard, follow example in test_do_Game,
    # check if scoreboard is called.
    # Check do bye print and returning true.
    # Check do rule print

