import pickle
import Bcolors as B


class Scoreboard:
    def __init__(self):
        """Constructor which creates the property scoreboard with a value taken from the file scoreboard.pickle
        """
        try:
            with open("./diceGame/scoreboard.pickle", "rb") as handle:
                sb = pickle.load(handle)
        except FileNotFoundError:
            print("No scoreboard found, creating a new one")
            sb = dict()
        finally:
            self.scoreboard = sb

    def print_scorebard(self):
        """Prints the scoreboard"""
        str="Scoreboard\n\
##############################################################\
############################################"
        for key, item in self.scoreboard.items():
            wr = item[0]/item[1]
            str += f"\n{B.Bcolors.OKGREEN}{key}: Matches won: {item[0]} Matches\
played: {item[1]} Winrate: {(wr*100):.2f}%"
        print(str)

    def save_scoreboard(self):
        """Update the scoreboard in binary format"""
        with open("./diceGame/scoreboard.pickle", "wb") as handle:
            pickle.dump(self.scoreboard, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def update_player(self, player):
        """Updates player's score and if there are no errors it creates a new player"""
        if player.won:
            if player.name == player.old_name:
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
                    """Scoreboard a dictionary key name.
                    value 0 wins count and value 1 games played
                    """
                    self.scoreboard[player.name] = (
                        # Store old data with new name
                        self.scoreboard[player.old_name][0] + 1,
                        self.scoreboard[player.old_name][1] + 1,
                    )
                    self.scoreboard.pop(player.old_name)
                    # remove data to avoid duplicates
                except KeyError:
                    data = [1, 1]
                    self.scoreboard[player.name] = data
                finally:
                    self.save_scoreboard()
        else:
            if player.name == player.old_name:
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
            else:
                try:
                    """Scoreboard a dictionary key name.
                    value 0 wins count and value 1 games played
                    """
                    self.scoreboard[player.name] = (
                        # Store old data with new name
                        self.scoreboard[player.old_name][0],
                        self.scoreboard[player.old_name][1] + 1,
                    )
                    self.scoreboard.pop(player.old_name)
                    # remove data to avoid duplicates
                except KeyError:
                    data = [0, 1]
                    self.scoreboard[player.name] = data
                finally:
                    self.save_scoreboard()
