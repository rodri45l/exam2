"""Dice class file"""
from random import randint
import pickle


class Dice:
    """Dice class with roll argument"""

    def __init__(self):
        """Constructor for dice class, sets roll to 0"""
        self.roll = 0

    def roll_dice(self, print_dice):
        """Sets a random number between 1-6 into roll variable and
        if Print Dice true, it prints an ASCII drawing of the dice.
        """
        with open("./diceGame/dice_drawings.pickle", "rb") as handle:
            dice_face_dic = pickle.load(handle)
            self.roll = randint(1, 6)
        if print_dice:
            print("\n" + dice_face_dic[self.roll] + "\n")
