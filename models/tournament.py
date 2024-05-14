import json

from .player import Player

class Tournament:
    """A local tournament"""
    def __init__(self, filepath=None, name=None, venue=None, start_date=None, end_date=None, players=None, round_number=None):
        self.filepath = filepath
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.round_number = round_number
        self.current_round = 0

        # Load File
        if filepath and not name:
            with open(filepath) as fp:
                data = json.load(fp)
                self.name = data["name"]
                self.players = [
                    Player(**player_dict) for player_dict in data["players"]
                ]
        elif not filepath:
            self.save()
    # Save file
    def save(self):
        """Serialize the players and save them to the tournament into a JSON file"""

        with open(self.filepath, "w") as fp:
            json.dump(
                {"name": self.name, "players": [p.serialize() for p in self.players]},
                fp,
            )
            
# Don't need to finish the whole class to go to the next class
# Think about how to add one feature at a time
# see how the project handles the clubs and the players for making the tournament