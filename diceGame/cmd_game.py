import cmd
from pig_classes import Game
from pig_classes import Bcolors as LetCol


class PigGame(cmd.Cmd):
    DIVIDER = "===================================================================\
======================================="
    intro = f'{LetCol.HEADER}{DIVIDER}\n\
{LetCol.OKBLUE}{LetCol.UNDERLINE}Welcome to the dice game PIG\n\
{LetCol.NOT_UNDERLINED}{LetCol.OKCYAN}In this game wins the first player to \
reach 100 points{LetCol.OKCYAN}\n\
Players take turns to roll a single dice as many times\
 as they wish,    \nadding all roll results to a running total, but losing \
their gained score for the turn if they roll a 1.\n{LetCol.HEADER}{DIVIDER}'
    prompt = f'{LetCol.WARNING}(Pig Game) '

    def do_play(self, arg):
        'Enter 1 to play vs the computer, 2 for 2 player game.'
        game = Game()
        if arg == '1':
            game.playerVsMachine()
        elif arg == '2':
            game.playerVsPlayer()
        else:
            print(f"please press 1 or 2 (you pressed: {arg})")


if __name__ == '__main__':
    PigGame().cmdloop()
