"""CMD CLASS Unittest."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest import mock
import cmd
from diceGame import cmd_game


class TestCmd(unittest.TestCase):
    """CMD testing class."""

    def test_PigGame(self):
        """Test  PigGame class."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        self.assertIsInstance(cmd_g, cmd_game.PigGame)

    @mock.patch('Game.Game.playerVsMachine')
    def test_do_play_1(self, mock):
        """Test if do_play calls playerVsMachine func."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_play("hard")
        self.assertTrue(mock.called)

    @mock.patch('Game.Game.playerVsMachine')
    def test_do_play_2(self, mock):
        """Test if do_play calls playerVsMachine func."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_play("easy")
        self.assertTrue(mock.called)

    @mock.patch("builtins.print")
    def test_do_play3(self, mock):
        """Test if we pass an argument other thatn 1 or 2."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_play('3')
        str = "Wrong argument, type easy or hard after 'play'."
        mock.assert_called_with(str)

    @mock.patch('Game.Game.playerVsPlayer')
    def test_do_play2(self, mock):
        """Test if do_play2 calls playerVsPlayer func."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_play2("")
        self.assertTrue(mock.called)

    def test_do_bye(self):
        """Test do bye function."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        exp = cmd_g.do_bye("")
        self.assertTrue(exp)

    @mock.patch("Scoreboard.Scoreboard.print_scorebard")
    # """ Test Scoreboard method """
    def test_do_scoreboard(self, mock):
        """Test print scoreboard."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_scoreboard("")
        self.assertTrue(mock.called)

    @mock.patch("builtins.print")
    def test_do_rule(self, mock):
        """Test if print function as required."""
        cmd_g = cmd_game.PigGame(cmd.Cmd)
        cmd_g.do_rules("")
        str = "\x1b[95m=====================================================\
=====================================================\x1b[96m\nIn this game wins the first player to reach 100 points\x1b[96m\nPlayers\
 take turns to roll a single dice as many times as they wish,    \nadding all roll results to a running total, but losing their gained score for the turn if they roll a 1.\
\n\x1b[95m=========================================================================================================="
        mock.assert_called_with(str)
