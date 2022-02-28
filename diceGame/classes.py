"""Classes module for Dice Pig game."""

from random import randint
import pickle


class Player():
    """Player class with name, score, tries and wins atributes"""
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wins = 0
        self.tries = 0
        if name == 'RODRI45Z':  # CHEAT CODE
            self.score = 99
        self.turn_score = 0

    def sum_turn_score(self):
        """Sums turn score to total score and sets score to 0"""
        self.score += self.turn_score
        self.turn_score = 0

    def change_name(self, name):
        """changes the player name"""
        self.name = name


class Dice():
    """Dice class with roll argument"""
    def __init__(self):
        self.roll = 0

    def roll_dice(self, print_dice):
        """sets a random number between 1-6 into roll variable and
        if Print Dice true, it prints an ASCII drawing of the dice.
        """
        with open('dice_drawings.pickle', 'rb') as handle:
            dice_face_dic = pickle.load(handle)
            self.roll = randint(1, 6)
        if print_dice:
            print(dice_face_dic[self.roll] + '\n')


class Bcolors:
    """Colors to print in cmd"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NOT_UNDERLINED = '\033[24m'
    RESET = '\u001b[0m'
