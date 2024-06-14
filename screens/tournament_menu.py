from .tournaments.view import TournamentView

class TournamentMenu:
    def __init__(self, tournament, players_manager):
        # self.players = players
        self.tournament_view = TournamentView(tournament, players_manager)
        pass

    def display(self):
        self.tournament_view.display()
        
    # [ ] Add editing ability
    