import json

from .player import Player

class Tournament:
    """A local tournament"""
    def __init__(self, name=None, start_date=None, end_date=None, venue=None, 
                 number_of_rounds=None, current_round=None, completed=None, 
                 players=None, finished=None, rounds=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        if current_round:
            self.current_round = current_round
        else:
            self.current_round = 0 
        self.completed = completed
        self.players = players
        self.finished = finished
        self.rounds = rounds

    # Save file
    def save(self):
        """Serialize the players and save them to the tournament into a JSON file"""

        with open(self.filepath, "w") as fp:
            json.dump(
                {"name": self.name, "players": [p.serialize() for p in self.players]},
                fp,
            )
