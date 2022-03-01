from tkinter import E
from Bcolors import Bcolors
import should_roll as prob
from Player import Player
from Scoreboard import Scoreboard
from Dice import Dice
from random import randint


class Game():
    """Game class with methods for the game"""
    def __init__(self):
        self.GOAL = 100
        self.DIVIDER = "===================================================================\
======================================="

    def showOptionMenu(self):
        """ Printing a menu with option of playing or not for the turn """
        print('Enter 1 to roll the dice')
        print('Enter 2 to hold your score')
        option2 = int(input(f'Enter your choice: {Bcolors.RESET}'))
        return option2

    def createPlayer(self, n):
        """ Creating player """
        player = Player(input(f"{Bcolors.OKCYAN}Please Player{n} \
enter your name: {Bcolors.RESET}"))
        return player
    
    def set_difficulty(self):
        """returns the difficulty mode"""
        difficulty = 0
        while difficulty not in [1, 2]:
            print("1. Easy mode\n2. Hard mode.")
            difficulty  = int(input("Please enter the difficulty: "))
        return difficulty

    def playerVsMachine(self):
        """ Player will compete with computer -
        both will play and winner will be displayed
        """
        player = self.createPlayer(1)
        difficulty = self.set_difficulty()
        computer = Player("Computer")
        while(player.score < 100 and computer.score < 100):
            player = self.playerTurn(player)
            if player.score >= 100:
                break
            computer = self.computerTurn(computer, player, difficulty)
            if computer.score >= 100:
                break
            print(f'Your probabilities to win are: \
    {prob.p_win(player.score, computer.score, 0):.2f}')

        if player.score >= self.GOAL:
            print(f'{Bcolors.OKGREEN}CONGRATULATIONS {player.name} YOU WIN!! Humans \
> Computers{Bcolors.RESET}')
            print(f'{self.DIVIDER}')
            player.won = True
        elif computer.score >= self.GOAL:
            print(f'{Bcolors.FAIL}You lose, computers > humans')
            print(f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}")
        scoreboard = Scoreboard()
        scoreboard.update_player(player)

    def playerTurn(self, player):
        """ it is Player turn - role the dice and get the score and total score for this turn """
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

    def computerTurn(self, computer, player, difficulty):
        """ Computer turn - role the dice and get the score and total score for this turn """
        dice = Dice()
        while prob.should_roll(computer.score, player.score, computer.turn_score):
            if difficulty == 1:
                random = randint(1, 2)
                if random == 2:
                    break
                else:
                    pass
            else:
                pass
            dice.roll_dice(False)
            if dice.roll == 1:
                computer.turn_score = 0
                print(f"Computer score this turn is {computer.score}")
                print(f"Computer Total score is {computer.score}")
                return computer
            else:
                computer.turn_score += dice.roll
        print(f"Computer score this turn is {computer.turn_score}")
        computer.sum_turn_score()
        print(f"Computer Total score is {computer.score}")
        return computer

    def playerVsPlayer(self):
        """ Two players playing - both will play and one would win and one would lose """
        player1 = self.createPlayer(1)
        player2 = self.createPlayer(2)
        while(player1.score < 100 and player2.score < 100):
            print(f"{self.DIVIDER}\n{player1.name}\
It's Your turn!\n{self.DIVIDER}")
            player1 = self.playerTurn(player1)
            if player1.score >= 100:
                break
            print(f"{self.DIVIDER}\n{player2.name}\
It's Your turn!\n{self.DIVIDER}")
            player2 = self.playerTurn(player2)
            if player2.score >= 100:
                break
            print(f'{self.DIVIDER}\nProbabilites to win:\n{player1.name}: \
{prob.p_win(player1.score, player2.score, 0):.2f}\n{player2.name}: \
{prob.p_win(player2.score, player1.score, 0):.2f}\n{self.DIVIDER}')
        if player1.score >= self.GOAL:
            print(f'{Bcolors.OKGREEN}CONGRATULATIONS {player1.name}\
 YOU WIN!!{Bcolors.RESET}')
            player1.won = True

        elif player2.score >= self.GOAL:
            print(f'{Bcolors.OKGREEN}CONGRATULATIONS {player2.name} YOU WIN!!\
{Bcolors.RESET}')
            player2.won = True
        print(f"Final Score:\n{player1.name}: {player1.score}\n\
{player2.name}: {player2.score}")
        scoreboard = Scoreboard()
        scoreboard.update_player(player1)
        scoreboard.update_player(player2)
