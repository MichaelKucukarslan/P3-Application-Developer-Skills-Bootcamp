import json
from pathlib import Path
from .player import Player

class PlayerManager:
    # Get all the players
    # load a file
    # get players from that file
    def __init__(self, data_folder="data/clubs"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.players = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    with open(filepath) as fp:
                        data = json.load(fp)
                        for player in data['players']:
                            self.players.append(Player(player['name'], player['email'], player['chess_id'], player['birthday']))
                        print(data['name'] + " club loaded.")
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    def get_players(self):
        return self.players