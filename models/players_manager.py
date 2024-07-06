import json
from pathlib import Path
from .player import Player


class PlayersManager:
    """Players Manager gets all the players from all the clubs"""

    def __init__(self, data_folder="data/clubs"):
        # print("New Player Manager")
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.players = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    with open(filepath) as fp:
                        data = json.load(fp)
                        for player in data['players']:
                            self.players.append(
                                Player(
                                    player['name'],
                                    player['email'],
                                    player['chess_id'],
                                    player['birthday']
                                )
                            )
                        # print(data['name'] + " club loaded.")
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    """Gets all the players in all the clubs"""
    def get_players(self):
        return self.players

    """Find players by chess_id"""
    def get_player_from_chess_id(self, id):
        for player in self.players:
            if player.chess_id == id:
                return player
        return None
