
"""Classes module for Dice Pig game."""

from random import randint
import pickle
import should_roll as prob


class Scoreboard():
    def __init__(self):
        try:
            with open('./diceGame/scoreboard.pickle', 'rb') as handle:
                sb = pickle.load(handle)
        except FileNotFoundError:
            print('No scoreboard found, creating a new one')
            sb = dict()
        finally:
            self.scoreboard = sb

    def print_scorebard(self):
        print('Scoreboard')
        print('##########################################################################################################')
        for key, item in self.scoreboard.items():
            print(f'{Bcolors.OKGREEN}{key}: Matches won: {item[0]} Matches played: {item[1]} Winrate: {(item[0]/item[1])*100}%')

    def save_scoreboard(self):
        with open('./diceGame/scoreboard.pickle', 'wb') as handle:
            pickle.dump(self.scoreboard, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def update_player(self, player):
        """updates player to scoreboard, if there is no coincidence it creates a new player"""
        if player.won:
            try:
                self.scoreboard[player.name] = self.scoreboard[player.name][0]+1, self.scoreboard[player.name][1]+1
            except KeyError:
                data = [1, 1]
                self.scoreboard[player.name] = data
            finally:
                self.save_scoreboard()
        else:
            try:
                self.scoreboard[player.name] = self.scoreboard[player.name][0], self.scoreboard[player.name][1]+1
            except KeyError:
                data = [0, 1]
                self.scoreboard[player.name] = data
            finally:
                self.save_scoreboard()


class Game():
    """Game class with with methods for the game"""
    def __init__(self):
        self.GOAL = 100
        self.DIVIDER = "===================================================================\
======================================="

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
            player.won = True
        elif computer.score >= self.GOAL:
            print(f'{Bcolors.FAIL}You lose, computers > humans')
            print(f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}")
        scoreboard = Scoreboard()
        scoreboard.update_player(player)

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
        """THIS IS THE METHOD FOR THE COMPUTER TURN """
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
