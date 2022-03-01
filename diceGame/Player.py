"""Player class file"""


class Player():
    """Player class with name, score, tries and wins atributes"""
    def __init__(self, name):
        """Constructor, takes name as argument and sets score to 0 and won to False.
        It also has a cheat code implemented for certain player names.
        """
        self.name = name
        self.score = 0
        self.won = False
        if(name in ['RODRI45Z', 'HIVA', 'YANA']):  # CHEAT CODE
            self.score = 99
        self.turn_score = 0

    def sum_turn_score(self):
        """Sums turn score to total score and sets score to 0"""
        self.score += self.turn_score
        self.turn_score = 0

    def change_name(self, name):
        """changes the player name"""
        self.name = name
