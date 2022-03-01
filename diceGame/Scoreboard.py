import pickle
from Bcolors import Bcolors


class Scoreboard:
    def __init__(self):
        try:
            with open("./diceGame/scoreboard.pickle", "rb") as handle:
                sb = pickle.load(handle)
        except FileNotFoundError:
            print("No scoreboard found, creating a new one")
            sb = dict()
        finally:
            self.scoreboard = sb

    def print_scorebard(self):
        print("Scoreboard")
        print(
            "##############################################################\
############################################"
        )
        for key, item in self.scoreboard.items():
            print(
                f"{Bcolors.OKGREEN}{key}: Matches won: {item[0]} Matches\
played: {item[1]} Winrate: {(item[0]/item[1])*100}%"
            )

    def save_scoreboard(self):
        with open("./diceGame/scoreboard.pickle", "wb") as handle:
            pickle.dump(self.scoreboard, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def update_player(self, player):
        """updates player to scoreboard,\
if there is no coincidence it creates a new player"""
        if player.won:
            try:
                """Scoreboard a dictionary key name.
                value 0 wins count and value 1 games played
                """
                self.scoreboard[player.name] = (
                    self.scoreboard[player.name][0] + 1,
                    self.scoreboard[player.name][1] + 1,
                )
            except KeyError:
                data = [1, 1]
                self.scoreboard[player.name] = data
            finally:
                self.save_scoreboard()
        else:
            try:
                self.scoreboard[player.name] = (
                    self.scoreboard[player.name][0],
                    self.scoreboard[player.name][1] + 1,
                )
            except KeyError:
                data = [0, 1]
                self.scoreboard[player.name] = data
            finally:
                self.save_scoreboard()
