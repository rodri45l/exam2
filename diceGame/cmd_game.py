"""Cmd module ussing cmd class for game loop."""
import cmd
from Game import Game
from Scoreboard import Scoreboard
from Bcolors import Bcolors as LetCol


class PigGame(cmd.Cmd):
    """PigGame cmd Class."""

    DIVIDER = "===================================================================\
======================================="
    intro = f"{LetCol.HEADER}{DIVIDER}\n\
{LetCol.OKBLUE}{LetCol.UNDERLINE}Welcome to the dice game PIG.{LetCol.RESET}\n\
{LetCol.HEADER}{DIVIDER}{LetCol.RESET}"
    prompt = f'{LetCol.RESET}\nAll commands: \n|  play (easy\hard)  |  play2  |  \
rules  |  scoreboard |  help |  bye  |\n\n{LetCol.WARNING}Enter a command:{LetCol.RESET} '

    def do_play(self, arg):
        """Play versus computer, enter hard or easy as an argument after 'play'."""
        game = Game()
        if arg == "hard":
            game.playerVsMachine(2)
        elif arg == "easy":
            game.playerVsMachine(1)
        else:
            print("Wrong argument, type easy or hard after 'play'.")

    def do_play2(self, arg):
        """2 player game."""
        game = Game()
        game.playerVsPlayer()

    def do_scoreboard(self, arg):
        """Print Scoreboard."""
        scoreboard = Scoreboard("./diceGame/scoreboard.pickle")
        scoreboard.print_scorebard()

    def do_bye(self, arg):
        """Close the game."""
        print("Thank you for playing. Bye!!")
        return True

    def do_rules(self, arg):
        """Show game rules."""
        DIVIDER = "===================================================================\
======================================="
        print(
            f"{LetCol.HEADER}{DIVIDER}{LetCol.OKCYAN}\nIn this game wins the \
first player to \
reach 100 points{LetCol.OKCYAN}\n\
Players take turns to roll a single dice as many times\
 as they wish,    \nadding all roll results to a running total, but losing \
their gained score for the turn if they roll a 1.\n{LetCol.HEADER}{DIVIDER}"
        )


if __name__ == "__main__":
    PigGame().cmdloop()
