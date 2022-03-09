import pickle
import Bcolors as B
# "./diceGame/scoreboard.pickle"

class Scoreboard:
    def __init__(self, path):
        """Constructor which creates the property scoreboard with a value taken from the file scoreboard.pickle
        """
        self.path = path
        try:
            with open(path, "rb") as handle:
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
            """Scoreboard is a dictionary with a key player's name 
            and 2 values - wins count and games played
            """
            wr = item[0]/item[1]
            str += f"\n{B.Bcolors.OKGREEN}{key}: Matches won: {item[0]} Matches \
played: {item[1]} Winrate: {(wr*100):.2f}%"
        print(str)

    def save_scoreboard(self):
        """Update the scoreboard in binary format"""
        with open(self.path, "wb") as handle:
            pickle.dump(self.scoreboard, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def update_player(self, player):
        """Updates player's score and if there are no errors it creates a new player"""
        if player.won:
                """If the name is the same update"""
                try:
                    """Scoreboard is a dictionary with a key player's name 
                    and 2 values - wins count and games played
                    """
                    if player.name == player.old_name:
                        self.scoreboard[player.name] = (
                            self.scoreboard[player.name][0] + 1,
                            self.scoreboard[player.name][1] + 1,
                        )
                    else:
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
            try:
                if player.name == player.old_name:
                    self.scoreboard[player.name] = (
                        self.scoreboard[player.name][0],
                        self.scoreboard[player.name][1] + 1,
                    )
                else:
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


        
