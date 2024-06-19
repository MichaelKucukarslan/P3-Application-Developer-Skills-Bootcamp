from .tournaments.view import TournamentView
from models.round_manager import RoundManager
class TournamentMenu:
    """
    Tournament Menu will look at individual tournaments.
    If the tournament is done it will display the results of that
    tournament. If it is not complete it will ask the user if they 
    want to input the next rounds winners. 
    """
    
    def __init__(self, tournament, players_manager):
        self.players_manager = players_manager
        self.tournament = tournament
        self.tournament_view = TournamentView(tournament, players_manager)
        pass

    def display(self):
        self.tournament_view.display() 
        value = self.tournament_view.get_command() # Asks if user wants to continue tournament (Y/N)
        if value:
            rounds = RoundManager(self.tournament)
            pass
        
    # [ ] Add editing ability
    