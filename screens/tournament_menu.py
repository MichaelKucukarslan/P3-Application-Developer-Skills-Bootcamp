from .tournaments.view import TournamentView

class TournamentMenu:
    def __init__(self, tournament):
        self.tournament = TournamentView(tournament)
        pass

    def display(self):
        self.tournament.display()
        