from .tournaments.view import TournamentView

class TournamentMenu:
    def __init__(self, tournament):
        # self.players = players
        self.tournament_view = TournamentView(tournament)
        pass

    def display(self):
        self.tournament_view.display()
        
    # [ ] Add editing ability
    