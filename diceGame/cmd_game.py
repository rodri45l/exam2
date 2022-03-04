import cmd
from Game import Game
from Scoreboard import Scoreboard
from Bcolors import Bcolors as LetCol


class PigGame(cmd.Cmd):
    DIVIDER = "===================================================================\
======================================="
    intro = f"{LetCol.HEADER}{DIVIDER}\n\
{LetCol.OKBLUE}{LetCol.UNDERLINE}Welcome to the dice game PIG.{LetCol.RESET}\n\
{LetCol.HEADER}{DIVIDER}"

    prompt = f'\nAll commands: \n|  play  |  rules  |  scoreboard |  help |  bye  |\n\n{LetCol.WARNING}Enter a command: '

    def do_play(self, arg):
        "Enter 1 to play vs the computer, 2 for 2 player game."
        print(f'{LetCol.RESET}\nLet’s play!\n\n1. One player game\n2. Two player game')
        game_type = input(f"Choose a game:")

        game = Game()
        if game_type == "1":
            game.playerVsMachine()
        elif game_type == "2":
            game.playerVsPlayer()
        else:
            print(f"Please press 1 or 2 (you pressed: {game_type})")

    def do_scoreboard(self, arg):
        'Prints Scoreboard'
        scoreboard = Scoreboard()
        scoreboard.print_scorebard()

    def do_bye(self, arg):
        "close the game."
        print("Thank you for playing. Bye!!")
        return True

    def do_rules(self, arg):
        "Show game rules."
        DIVIDER = "===================================================================\
======================================="
        print(
            f"{LetCol.HEADER}{DIVIDER}{LetCol.OKCYAN}\nIn this game wins the\
first player to \
reach 100 points{LetCol.OKCYAN}\n\
Players take turns to roll a single dice as many times\
 as they wish,    \nadding all roll results to a running total, but losing \
their gained score for the turn if they roll a 1.\n{LetCol.HEADER}{DIVIDER}"
        )


if __name__ == "__main__":
    PigGame().cmdloop()
