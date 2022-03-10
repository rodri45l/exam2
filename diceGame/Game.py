"""Game module containing functions for the pig game."""
from random import randint
from Bcolors import Bcolors
import should_roll as prob
from Player import Player
from Scoreboard import Scoreboard
from Dice import Dice


class Game:
    """Game class with methods for the game."""

    def __init__(self):
        """Class constructor with GOAL and Divider as attributes."""
        self.GOAL = 100
        self.DIVIDER = "===================================================================\
======================================="

    def showOptionMenu(self, name):
        """Print a menu with options."""
        try:
            option = int(input(f"{Bcolors.HEADER}{self.DIVIDER}\n\
{Bcolors.UNDERLINE}Please {name} enter:{Bcolors.NOT_UNDERLINED}\n\
1 to roll the dice\n\
2 to hold your score\n\
3 to change your name\n\
4 to restart\n\
5 to exit the game\n\
Enter your choice: {Bcolors.RESET}"))
            if option not in range(1, 6):
                raise ValueError('Problem!')
        except ValueError:
            print(f'\n{Bcolors.FAIL}Please input a number between 1 and 5{Bcolors.RESET}')
            return self.showOptionMenu(name)

        return option

    def createPlayer(self, n):
        """Create player."""
        player = Player(
            input(
                f"\n{Bcolors.OKCYAN}Please Player {n} \
enter your name: {Bcolors.RESET}"
            )
        )
        return player

    def playerVsMachine(self, difficulty):
        """Player vs machine game."""
        player = self.createPlayer(1)
        computer = Player("Computer")
        if player.name == "test":
            computer.score = 100

        while player.score < 100 and computer.score < 100:
            player = self.playerTurn(player)
            if player.score >= 100:
                break
            elif player.score == -1:
                return 0
            elif player.score == -2:
                self.playerVsMachine(difficulty)
                return 0

            computer = self.computerTurn(computer, player, difficulty)
            if computer.score >= 100:
                break
            print(
                f"Your probabilities to win are: \
    {prob.p_win(player.score, computer.score, 0):.2f}"
            )

        if player.score >= self.GOAL:
            print(
                f"{Bcolors.OKGREEN}CONGRATULATIONS {player.name} YOU WIN!! Humans \
> Computers{Bcolors.RESET}"
            )
            print(f"{self.DIVIDER}")
            player.won = True
            scoreboard = Scoreboard("./diceGame/scoreboard.pickle")
            scoreboard.update_player(player)
            return 1
        elif computer.score >= self.GOAL:
            print(f"{Bcolors.FAIL}You lose, Computers > Humans")
            print(
                f"Final Score:\n{player.name}: {player.score}\n\
Computer: {computer.score}"
            )
            scoreboard = Scoreboard("./diceGame/scoreboard.pickle")
            scoreboard.update_player(player)
            return 2

    def playerTurn(self, player):
        """Player turn."""
        option = 0
        keepRunning = True
        x = Dice()
        while keepRunning:
            option = self.showOptionMenu(player.name)
            if option == 2:
                keepRunning = False
            elif option == 4:
                print("Restarting the game...")
                player.score = -2
                return player
            elif option == 5:
                print('Game halted!')
                player.score = -1
                return player
            elif option == 3:
                self.change_name(player)
            elif option == 1:
                x.roll_dice(True)

                if x.roll == 1:
                    player.turn_score = 0
                    print(
                        f"{Bcolors.WARNING}Unlucky, you scored a 1\n\
{Bcolors.OKBLUE}Your score this turn is {player.turn_score}\n\
{player.name}'s Total score this turn is \
{player.score}"
                    )
                    return player
                else:
                    print(f"You got a {x.roll}")
                    player.turn_score += x.roll
                    print(
                        f"{Bcolors.OKBLUE}Your score for this turn is:\
    {player.turn_score}"
                    )
        print(f"{Bcolors.OKBLUE}Your score this turn is {player.turn_score}")
        player.sum_turn_score()
        print(f"{player.name}'s Total score this turn is {player.score}")

        return player

    def computerTurn(self, computer, player, difficulty):
        """Play as computer."""
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
                print(f"Computer Score this turn is {computer.score}")
                print(f"Computer Total Score is {computer.score}")
                return computer
            else:
                computer.turn_score += dice.roll
        print(f"Computer Score this turn is {computer.turn_score}")
        computer.sum_turn_score()
        print(f"Computer Total Score is {computer.score}")
        return computer

    def playerVsPlayer(self):
        """Play with 2 players."""
        player1 = self.createPlayer(1)
        player2 = self.createPlayer(2)
        while player1.score < 100 and player2.score < 100:
            print(
                f"{self.DIVIDER}\n{player1.name}\
It's Your turn!\n{self.DIVIDER}"
            )
            player1 = self.playerTurn(player1)
            if player1.score >= 100:
                break
            elif player1.score == -1:
                return 0
            elif player1.score == -2:
                self.playerVsPlayer()
                return 0
            print(
                f"{self.DIVIDER}\n{player2.name}\
It's Your turn!\n{self.DIVIDER}"
            )
            player2 = self.playerTurn(player2)
            if player2.score >= 100:
                break
            elif player2.score == -1:
                return 0
            elif player2.score == -2:
                self.playerVsPlayer()
                return 0
            print(
                f"{self.DIVIDER}\nProbabilites to win:\n{player1.name}: \
{prob.p_win(player1.score, player2.score, 0):.2f}\n{player2.name}: \
{prob.p_win(player2.score, player1.score, 0):.2f}\n{self.DIVIDER}"
            )
        if player1.score >= self.GOAL:
            print(
                f"{Bcolors.OKGREEN}CONGRATULATIONS {player1.name}\
 YOU WIN!!{Bcolors.RESET}"
            )
            player1.won = True

        elif player2.score >= self.GOAL:
            print(
                f"{Bcolors.OKGREEN}CONGRATULATIONS {player2.name} YOU WIN!!\
{Bcolors.RESET}"
            )
            player2.won = True
        print(
            f"Final Score:\n{player1.name}: {player1.score}\n\
{player2.name}: {player2.score}"
        )
        scoreboard = Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard.update_player(player1)
        scoreboard.update_player(player2)

    def change_name(self, player):
        """Change name."""
        new_name = input('Enter new name: ')
        player.change_name(new_name)
