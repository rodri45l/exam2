"""Game Unittest"""
import unittest
from unittest.mock import patch
from diceGame import Game
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
        """Test create player."""
        game = Game.Game()
        player = game.createPlayer(1)
        exp = player.name == "Rodri"
        self.assertTrue(exp)

    @patch('builtins.input', side_effect=["    ", "Koki"])
    def test_create_player_2(self, mock_input):
        """Test create player."""
        game = Game.Game()
        player = game.createPlayer(1)
        exp = player.name == "Koki"
        self.assertTrue(exp)

    @patch('builtins.input', return_value="Rodri2")
    def test_change_name(self, mock_input):
        """Test change name"""
        player = Player("Rodri")
        game = Game.Game()
        game.change_name(player)
        self.assertEqual(player.name, "Rodri2")

    @patch('builtins.input', side_effect=["    ", "Rodri2"])
    def test_change_name_2(self, mock_input):
        """Test change name"""
        player = Player("Rodri")
        game = Game.Game()
        game.change_name(player)
        self.assertEqual(player.name, "Rodri2")    
    
    @patch("builtins.input", return_value="1")
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

    @patch('builtins.input', side_effect=["Rodri45Z", "5"])
    def test_playerVsMachine(self, mock_input):
        """Test playervsMachine exit """
        game = Game.Game()
        exp = game.playerVsMachine(2)
        self.assertEqual(exp, 0)

    @patch("builtins.input", side_effect=["RODRI45Z", "4", "RODRI45Z", "2"])
    def test_playerVsMachine2(self, mock_input):
        """Test playervsMachine restart"""
        game = Game.Game()
        exp = game.playerVsMachine(1)
        self.assertEqual(exp, 0)

    @patch("builtins.input", side_effect=["RODRI45Z", "2"])
    def test_playerVsMachine3(self, mock_input):
        """Test playervsMachine player win"""
        game = Game.Game()
        exp = game.playerVsMachine(1)
        self.assertEqual(exp, 1)

    @patch("builtins.input", side_effect=["test"])
    def test_playerVsMachine4(self, mock_input):
        """Test playervsMachine computer wins"""
        game = Game.Game()
        exp = game.playerVsMachine(2)
        self.assertEqual(exp, 2)

    @patch("builtins.input", side_effect=["RODRI45Z", "yana", "2"])
    def test_playerVsplayer(self, mock_input):
        """Test playervsplayer player 1 win"""
        game = Game.Game()
        exp = game.playerVsPlayer()
        self.assertEqual(exp, 1)

    @patch("builtins.input", side_effect=["Robert", "YANA", "2", "2"])
    def test_playerVsplayer2(self, mock_input):
        """Test playervsplayer player 2 win"""
        game = Game.Game()
        exp = game.playerVsPlayer()
        self.assertEqual(exp, 2)

    def test_computerTurn(self):
        "Test of computer turn difficulty hard"
        game = Game.Game()
        computer = Player("computer")
        player = Player("Rodri")
        exp = game.computerTurn(computer, player, 2)
        self.assertIsInstance(exp, Player)

    def test_computerTurn2(self):
        "Test of computer turn difficulty easy."
        game = Game.Game()
        computer = Player("computer")
        player = Player("Rodri")
        exp = game.computerTurn(computer, player, 1)
        self.assertIsInstance(exp, Player)

    @patch('builtins.input', side_effect=["Rodri45Z", "yana", "5"])
    def test_playerVsplayer1exit(self, mock_input):
        """Test playervsplayer1 exit """
        game = Game.Game()
        exp = game.playerVsPlayer()
        self.assertEqual(exp, 0)

    @patch("builtins.input", side_effect=["RODRI45Z", "Yana", "4", "RODRI45Z", "Yana", "2"])
    def test_playerVsPlayer1Restart(self, mock_input):
        """Test playervsPlayer1 restart"""
        game = Game.Game()
        exp = game.playerVsPlayer()
        self.assertEqual(exp, 0)
