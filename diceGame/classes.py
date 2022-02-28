"""Classes module for Dice Pig game."""

from random import randint
import pickle
import should_roll as prob


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
        with open('./diceGame/dice_drawings.pickle', 'rb') as handle:
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


class Game():
    """Game class with with methods for the game"""
    def __init__(self):
        self.GOAL = 100
        self.DIVIDER = "===================================================================\
======================================="

    def showMenu(self):
        print(f'{Bcolors.UNDERLINE}{ Bcolors.OKCYAN}Press 1\
to play vs the computer.')
        print(f'Press 2 for 2 players.{Bcolors.NOT_UNDERLINED}')
        choice = [1, 2]
        option = 0
        while option not in choice:
            try:
                option = int(input(f'{Bcolors.OKCYAN}Please input 1 or 2 \
depending on your choice: {Bcolors.RESET}'))
            except ValueError:
                print(f'{Bcolors.FAIL} Please enter a valid value (1, 2)')
                print('\n')
        return option

    def showOptionMenu(self):
        print('Enter 1 to roll the dice')
        print('Enter 2 to hold your score')
        option2 = int(input(f'Enter your choice: {Bcolors.RESET}'))
        return option2

    def createPlayer(self, n):
        player = Player(input(f"{Bcolors.OKCYAN}Please Player{n} \
enter your name: {Bcolors.RESET}"))
        return player

    def playerVsMachine(self):
        player = self.createPlayer(1)
        computer = Player("Computer")
        while(player.score < 100 and computer.score < 100):
            player = self.playerTurn(player)
            if player.score >= 100:
                break
            computer = self.computerTurn(computer, player)
            if computer.score >= 100:
                break
            print(f'Your probabilities to win are: \
    {prob.p_win(player.score, computer.score, 0):.2f}')

        if player.score >= self.GOAL:
            print(f'{Bcolors.OKGREEN}CONGRATULATIONS {player.name} YOU WIN!! Humans \
> Computers{Bcolors.RESET}')
            print(f'{self.DIVIDER}')
        elif computer.score >= self.GOAL:
            print(f'{Bcolors.FAIL}You lose, computers > humans')
            print(f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}")

    def playerTurn(self, player):
        option = 0
        keepRunning = True
        x = Dice()
        while keepRunning:
            print(f'{Bcolors.HEADER}{self.DIVIDER}\n\
{Bcolors.UNDERLINE}Please {player.name} choose:{Bcolors.NOT_UNDERLINED}')
            option = self.showOptionMenu()
            if option == 2:
                keepRunning = False
            elif option == 1:
                x.roll_dice(True)

                if x.roll == 1:
                    player.turn_score = 0
                    print(f"{Bcolors.WARNING}Unlucky, you scored a 1\n\
{Bcolors.OKBLUE}Your score this turn is {player.turn_score}\n\
{player.name}'s Total score this turn is \
{player.score}")
                    return player
                else:
                    print(f"You got a {x.roll}")
                    player.turn_score += x.roll
                    print(f'{Bcolors.OKBLUE}Your score for this turn is:\
    {player.turn_score}')
            else:
                print(f'{Bcolors.FAIL}!!!!!!\nPlease enter a \
valid option\n!!!!!!')
                self.playerTurn(player)
        print(f"{Bcolors.OKBLUE}Your score this turn is {player.turn_score}")
        player.sum_turn_score()
        print(f"{player.name}'s Total score this turn is {player.score}")

        return player

    def computerTurn(self, computer, player):
        dice = Dice()
        while prob.should_roll(computer.score, player.score, computer.turn_score):
            dice.roll_dice(False)
            if dice.roll == 1:
                computer.turn_score = 0
                print(f"Computer score this turn is {computer.score}")
                return computer
            else:
                computer.turn_score += dice.roll
        print(f"Computer score this turn is {computer.turn_score}")
        computer.sum_turn_score()
        print(f"Computer Total score is {computer.score}")
        return computer

    def playerVsPlayer(self):
        player1 = self.createPlayer(1)
        player2 = self.createPlayer(2)
        while(player1.score < 100 and player2.score < 100):
            print(f"{self.DIVIDER}\n{player1.name}\
It's Your turn!\n{self.DIVIDER}")
            player1 = self.playerTurn(player1)
            print(f"{self.DIVIDER}\n{player2.name}\
It's Your turn!\n{self.DIVIDER}")
            player2 = self.playerTurn(player2)
            print(f'{self.DIVIDER}\nProbabilites to win:\n{player1.name}: \
{prob.pWin(player1.score, player2.score, 0):.2f}\n{player2.name}: \
{prob.pWin(player2.score, player1.score, 0):.2f}\n{self.DIVIDER}')
        if player1.score >= self.GOAL:
            print(f'{Bcolors.OKGREEN} CONGRATULATIONS {player1.name}\
YOU WIN!!{Bcolors.RESET}')

        elif player2.score >= self.GOAL:
            print(f'{Bcolors.OKGREEN} CONGRATULATIONS {player2.name} YOU WIN!!\
{Bcolors.RESET}')
        print(f"Final Score:\n{player1.name}: {player1.score}\n\
{player2.name}: {player2.score}")

        player = self.createPlayer(1)
        computer = Player("Computer")
        while(player.score < 100 and computer.score < 100):
            player = self.playerTurn(player)
            computer = self.computerTurn(computer, player)
            print(f'Your probabilities to win are: \
{prob.pWin(player.score, computer.score, 0):.2f}')

        if player.score >= self.GOAL:
            print(f'{Bcolors.OKGREEN}CONGRATULATIONS {player.name} YOU WIN!! Humans \
> Computers{Bcolors.RESET}')
            print(f'{self.DIVIDER}')
        elif computer.score >= self.GOAL:
            print(f'{Bcolors.FAIL}You lose, computers > humans')
            print(f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}")

    def play(self):
        playersOPtion = self.showMenu()
        if playersOPtion == 1:
            self.playerVsMachine()
        else:
            self.playerVsPlayer()
