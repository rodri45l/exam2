"""Player class file."""


class Player:
    """Player class with name, score, tries and wins atributes."""

    def __init__(self, name):
        """Player Class constructor."""
        self.name = name
        self.score = 0
        self.won = False
        self.old_name = name
        self.turn_score = 0
        if name in ["RODRI45Z", "HIVA", "YANA"]:  # CHEAT CODE
            self.turn_score = 100

    def sum_turn_score(self):
        """Sum turn score to total score and sets score to 0."""
        self.score += self.turn_score
        self.turn_score = 0

    def change_name(self, name):
        """Change the player name."""
        self.name = name
        if name in ["RODRI45Z", "HIVA", "YANA"]:  # CHEAT CODE
            self.turn_score = 100
