"""Dice Unittest"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Game
import unittest
from unittest.mock import patch
import pickle
from unittest import mock

class TestGame(unittest.TestCase):
    """ Game Testing class """

    def test_Game(self):
        '''Test Dice class'''
        game = Game.Game()
        self.assertIsInstance(game, Game.Game)
    
    # @mock.patch("builtins.print")
    # def test_showOptionMenu(self, mock):
    #     """Test show option menu """
    #     game = Game.Game()
    #     game.Game("7")
    #     str = "Enter your choice: 7"
    #     mock.assert_called_with(str)

    # def test_createPlayer(self):
    #     """ Test creating player """
    #     game = Game.Game()
    #     game.Game("1")
    #     str = "Please Player n \ enter your name: 1 "
    #     mock.assert_called_with(str)