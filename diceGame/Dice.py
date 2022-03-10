"""Dice class file."""
from random import randint
import pickle


class Dice:
    """Dice class with roll argument."""

    def __init__(self):
        """Construct the dice class, sets roll to 0."""
        self.roll = 0

    def roll_dice(self, print_dice):
        """Set roll attribute as a random number from 1 to 6."""
        with open("./diceGame/dice_drawings.pickle", "rb") as handle:
            dice_face_dic = pickle.load(handle)
            self.roll = randint(1, 6)
        if print_dice:
            print("\n" + dice_face_dic[self.roll] + "\n")
