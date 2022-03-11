"""Dice Unittest."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
import pickle
from diceGame import Scoreboard
from diceGame import Player
from diceGame import Bcolors as B


class TestScoreboard(unittest.TestCase):
    """Scoreboard testing class."""

    def test_scoreboard(self):
        """Test Scoreboard class."""
        scoreboard = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        self.assertIsInstance(scoreboard, Scoreboard.Scoreboard)

    @patch("builtins.print")
    def test_init(self, mock):
        """Test if we throw FileNotFoundError exception."""
        Scoreboard.Scoreboard("./wrong/scoreboardWrongName.pickle")
        str = "No scoreboard found, creating a new one"
        mock.assert_called_with(str)

    @patch("builtins.print")
    def test_print_scoreboard(self, mock):
        """Test print_scoreboard func."""
        scoreboard = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        sb = scoreboard.scoreboard
        str = "Scoreboard\n\
##############################################################\
############################################"
        for key, item in sb.items():
            wr = item[0] / item[1]
            str += f"\n{B.Bcolors.OKGREEN}{key}: Matches won: {item[0]} Matches \
played: {item[1]} Winrate: {(wr*100):.2f}%"
        scoreboard.print_scorebard()
        mock.assert_called_with(str)

    def test_save_scoreboard(self):
        """Test save_scoreboard func."""
        player = Player.Player("Test")
        player.won = True
        scoreboard = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard.update_player(player)
        sb = scoreboard.scoreboard
        scoreboard.save_scoreboard()

        with open("./diceGame/scoreboard.pickle", "rb") as handle:
            sb2 = pickle.load(handle)
        self.assertEqual(sb, sb2)

        # remove test data to avoid duplicates
        sb.pop(player.name)
        scoreboard.save_scoreboard()

    def test_update_player_1(self):
        """Test name NOT changed, socre and games count saved correctly."""
        # Arrange:
        scoreboard_object = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard = scoreboard_object.scoreboard

        initial_name = "Koci"

        # Clean scoreboard
        if initial_name in scoreboard.keys():
            scoreboard.pop(initial_name)
            scoreboard_object.save_scoreboard()

        player = Player.Player(initial_name)
        player.won = True

        # Act: Won 3 games, Lost 2, Played 5 games
        scoreboard_object.update_player(player)
        scoreboard_object.update_player(player)
        player.won = False
        scoreboard_object.update_player(player)
        player.won = True
        scoreboard_object.update_player(player)
        player.won = False
        scoreboard_object.update_player(player)

        # Assert: Is the name in the dict
        self.assertIn(player.name, scoreboard.keys())

        # Assert: Won 3 games, Lost 2, Played 5 games
        self.assertEqual(3, scoreboard[player.name][0])
        self.assertEqual(5, scoreboard[player.name][1])

        # Remove test data to avoid duplicates
        scoreboard.pop(player.name)
        scoreboard_object.save_scoreboard()

    def test_update_player_2(self):
        """Test name changed and one win score and games count saved correctly."""
        # Note: We update the player at the end of the game
        # Arrange:
        scoreboard_object = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard = scoreboard_object.scoreboard

        initial_name = "Maya"
        new_name = "Mimi"

        # Clean scoreboard
        if initial_name in scoreboard.keys():
            scoreboard.pop(initial_name)
            scoreboard_object.save_scoreboard()
        if new_name in scoreboard.keys():
            scoreboard.pop(new_name)
            scoreboard_object.save_scoreboard()

        # Player:
        player = Player.Player(initial_name)
        player.won = True

        # Act: Change name, Won 3 games, Played 4 games
        scoreboard_object.update_player(player)
        scoreboard_object.update_player(player)
        player.won = False
        scoreboard_object.update_player(player)
        player.change_name(new_name)
        player.won = True
        scoreboard_object.update_player(player)

        # Assert: Is the name in the dict
        self.assertIn(player.name, scoreboard.keys())

        # Assert: Won 3 game, Played 4 games
        self.assertEqual(3, scoreboard[player.name][0])
        self.assertEqual(4, scoreboard[player.name][1])

        # Remove test data to avoid duplicates
        scoreboard.pop(player.name)
        scoreboard_object.save_scoreboard()

    def test_update_player_3(self):
        """Test - name changed and one loss - socre and games count saved correctly."""
        # Arrange:
        scoreboard_object = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard = scoreboard_object.scoreboard

        initial_name = "Maya"
        new_name = "Mimi"

        # Clean scoreboard
        if initial_name in scoreboard.keys():
            scoreboard.pop(initial_name)
            scoreboard_object.save_scoreboard()
        if new_name in scoreboard.keys():
            scoreboard.pop(new_name)
            scoreboard_object.save_scoreboard()

        # Player:
        player = Player.Player(initial_name)
        player.won = True
        # Act: Change name, Won 2 games, Played 4 games
        scoreboard_object.update_player(player)
        scoreboard_object.update_player(player)
        player.won = False
        scoreboard_object.update_player(player)
        player.change_name(new_name)
        scoreboard_object.update_player(player)

        # Assert: Is the name in the dict
        self.assertIn(player.name, scoreboard.keys())
        # Assert: Won 2 game, Played 2 games
        self.assertEqual(2, scoreboard[player.name][0])
        self.assertEqual(4, scoreboard[player.name][1])

        # Remove test data to avoid duplicates
        scoreboard.pop(player.name)
        scoreboard_object.save_scoreboard()

    def test_update_player_4(self):
        """Test create a new winner (player was not found)."""
        # Arrange:
        scoreboard_object = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard = scoreboard_object.scoreboard

        initial_name = "Maya"

        # Clean scoreboard
        if initial_name in scoreboard.keys():
            scoreboard.pop(initial_name)
            scoreboard_object.save_scoreboard()

        # Player:
        player = Player.Player(initial_name)
        player.won = True

        # Act: Change name, Won 1 games, Played 1 games
        scoreboard_object.update_player(player)
        # Assert: The new player is in the scoreboard
        self.assertIn(player.name, scoreboard.keys())

        # Assert: Won 1 game, Played 1 games
        self.assertEqual(1, scoreboard[player.name][0])
        self.assertEqual(1, scoreboard[player.name][1])

        # Remove test data to avoid duplicates
        scoreboard.pop(player.name)
        scoreboard_object.save_scoreboard()

    def test_update_player_5(self):
        """Test create a new loser."""
        # Arrange:
        scoreboard_object = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard = scoreboard_object.scoreboard

        initial_name = "Maya"

        # Clean scoreboard
        if initial_name in scoreboard.keys():
            scoreboard.pop(initial_name)
            scoreboard_object.save_scoreboard()

        # Player:
        player = Player.Player(initial_name)
        player.won = False

        # Act: Change name, Won 0 games, Played 1 games
        scoreboard_object.update_player(player)

        # Assert: The new player is in the scoreboard
        self.assertIn(player.name, scoreboard.keys())

        # Assert: Won 0 game, Played 1 games
        self.assertEqual(0, scoreboard[player.name][0])
        self.assertEqual(1, scoreboard[player.name][1])

        # Remove test data to avoid duplicates
        scoreboard.pop(player.name)
        scoreboard_object.save_scoreboard()

    def test_update_player_6(self):
        """Test - Winning - check if we delete the old name from the scoreboard."""
        # Arrange:
        scoreboard_object = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard = scoreboard_object.scoreboard

        initial_name = "Maya"
        new_name = "Mimi"

        # Clean scoreboard
        if initial_name in scoreboard.keys():
            scoreboard.pop(initial_name)
            scoreboard_object.save_scoreboard()

        if new_name in scoreboard.keys():
            scoreboard.pop(new_name)
            scoreboard_object.save_scoreboard()

        # Player:
        player = Player.Player(initial_name)
        player.won = True

        # Act: Change name
        scoreboard_object.update_player(player)
        player.change_name(new_name)
        scoreboard_object.update_player(player)

        # Assert: If we changed the name in the scoreboard
        self.assertIn(player.name, scoreboard.keys())
        self.assertFalse(player.old_name in scoreboard.keys())

        # Remove test data to avoid duplicates
        scoreboard.pop(player.name)
        scoreboard_object.save_scoreboard()

    def test_update_player_7(self):
        """Test - Loosing - check if we delete the old name from the scoreboard."""
        # Arrange:
        scoreboard_object = Scoreboard.Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard = scoreboard_object.scoreboard

        initial_name = "Maya"
        new_name = "Mimi"

        # Clean scoreboard
        if initial_name in scoreboard.keys():
            scoreboard.pop(initial_name)
            scoreboard_object.save_scoreboard()

        if new_name in scoreboard.keys():
            scoreboard.pop(new_name)
            scoreboard_object.save_scoreboard()

        # Player:
        player = Player.Player(initial_name)
        player.won = True

        # Act: Change name
        scoreboard_object.update_player(player)
        player.change_name(new_name)
        scoreboard_object.update_player(player)

        # Assert: If we changed the name in the scoreboard
        self.assertIn(player.name, scoreboard.keys())
        self.assertFalse(player.old_name in scoreboard.keys())

        # Remove test data to avoid duplicates
        scoreboard.pop(player.name)
        scoreboard_object.save_scoreboard()
