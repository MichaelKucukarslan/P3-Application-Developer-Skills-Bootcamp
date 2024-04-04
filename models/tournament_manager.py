import json
from pathlib import Path

from .club import ChessClub

class TournamentManager:
    def __init__(self, data_folder="data/tournaments"):
        self.data_folder=data_folder
    
    """Trying to get this to work"""
    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        club = ChessClub(name=name, filepath=filepath)
        club.save()

        self.clubs.append(club)
        return club