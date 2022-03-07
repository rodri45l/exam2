"""Dice Unittest"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Game
import unittest
from unittest.mock import patch
from diceGame.Bcolors import Bcolors
from diceGame.Player import Player

class TestGame(unittest.TestCase):
    """ Game Testing class """
    DIVIDER = "===================================================================\
======================================="
    def test_Game(self):
        '''Test Dice class'''
        game = Game.Game()
        self.assertIsInstance(game, Game.Game)
    
    @patch('builtins.input', return_value="Rodri")
    def test_create_player(self, mock_input):
        game = Game.Game()
        player = game.createPlayer(1)
        exp = player.name == "Rodri"
        self.assertTrue(exp)
    
    @patch('builtins.input', return_value = "Rodri2")
    def test_change_name(self, mock_input):
        player = Player("Rodri")
        game = Game.Game()
        game.change_name(player)
        self.assertEqual(player.name, "Rodri2")


    
    @patch("builtins.input", return_value = "1")
    def test_showOptionMenu(self, mock_input):
        """Test show option menu """
        game = Game.Game()
        num = game.showOptionMenu("Rodri")
        str = f"{Bcolors.HEADER}{self.DIVIDER}\n\
{Bcolors.UNDERLINE}Please Rodri enter:{Bcolors.NOT_UNDERLINED}\n\
1 to roll the dice\n\
2 to hold your score\n\
3 to change your name\n\
4 to restart\n\
5 to exit the game\n\
Enter your choice: {Bcolors.RESET}"
        mock_input.assert_called_with(str)
        self.assertEqual(num, 1)

    @patch("builtins.input", side_effect=["7", "1"])
    def test_showOptionMenu2(self, mock_input):
        """Test show option menu """
        game = Game.Game()
        num = game.showOptionMenu("Rodri")
        str = f"{Bcolors.HEADER}{self.DIVIDER}\n\
{Bcolors.UNDERLINE}Please Rodri enter:{Bcolors.NOT_UNDERLINED}\n\
1 to roll the dice\n\
2 to hold your score\n\
3 to change your name\n\
4 to restart\n\
5 to exit the game\n\
Enter your choice: {Bcolors.RESET}"
        mock_input.assert_called_with(str)
        self.assertEqual(num, 1)
