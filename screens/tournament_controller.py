from .base_screen import BaseScreen
# Does not have a tournament model because it is passed from calling class.
from models.tournament import Tournament
from .tournament.view import TournamentView
from models.players_manager import PlayersManager
from .round_controller import RoundController

class TournamentController(BaseScreen):
    """
    Tournament Menu will look at individual tournaments.
    If the tournament is done it will display the results of that
    tournament. If it is not complete it will ask the user if they 
    want to input the next rounds winners. 
    """

    def __init__(self, tournament: Tournament, players_manager: PlayersManager):
        self.players_manager = players_manager
        self.tournament = tournament
        self.tournament_view = TournamentView(tournament, players_manager)
        pass

    def get_command(self):
        self.tournament_view.display()
        continue_tournament = self.tournament_view.get_command() # Asks if user wants to continue tournament (Y/N)
        while continue_tournament:
            round_controller = RoundController(self.tournament)
            round_controller.get_command()
            continue_tournament = False
            pass
        players = self.tournament.get_players_with_points()
        print(players)
        self.tournament_view.print_ranking(players)

        
    