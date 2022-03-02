"""Dice Unittest"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from diceGame import Dice
import unittest
from unittest.mock import patch
import pickle

class TestDice(unittest.TestCase):
    """Dice testing class"""

    def test_Dice(self):
        '''Test Dice class'''
        die = Dice.Dice()
        self.assertIsInstance(die, Dice.Dice)
    
    def test_roll_dice(self):
        """Test roll_dice method without printing"""
        die = Dice.Dice()
        die.roll_dice(False)
        exp = 0 < die.roll < 7 
        self.assertTrue(exp)

    @patch('builtins.print')
    def test_roll_dice2(self, mock_print):
        """Test roll_dice method with printing"""
        die = Dice.Dice()
        die.roll_dice(True)
        with open("./diceGame/dice_drawings.pickle", "rb") as handle:
            dice_face_dic = pickle.load(handle)
        str = "\n" + dice_face_dic[die.roll] + "\n"
        mock_print.assert_called_with(str)


