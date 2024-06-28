import json

from models.tournament import Tournament
from models.round_manager import RoundManager
from models.round import Round
from screens.rounds import RoundView

class RoundMenu:
    """
    Round Menu is called when the user wants to continue a tournament.
    It first creates the next round. Then allows the user to input winners for that round.
    """
    def __init__(self, tournament, data_folder="data/tournaments"):
        self.tournament = tournament
        self.tournament.save()
        self.round_view = RoundView(tournament)
        self.display()
        pass

    def display(self):
        print("**Round Menu**")
        print()
        
        pass