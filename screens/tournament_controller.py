from .base_screen import BaseScreen
# Does not have a tournament model because it is passed from calling class.
from models.tournament import Tournament
from .tournament.view import TournamentView
from .tournament_create.view import TournamentCreateView
from models.players_manager import PlayersManager
from .round_controller import RoundController


class TournamentController(BaseScreen):
    """
    Tournament Menu will look at individual tournaments.
    If the tournament is done it will display the results of that
    tournament. If it is not complete it will ask the user if they
    want to input the next rounds winners.
    """
    def __init__(self,
                 players_manager: PlayersManager,
                 tournament: Tournament = None):
        self.players_manager = players_manager
        self.tournament = tournament
        if self.tournament is None:
            print("create a new tournament")
            tournament_create_view = TournamentCreateView()
            self.tournament = tournament_create_view.create_tournament()
        self.tournament_view = TournamentView(tournament, players_manager)
        pass

    def get_command(self):
        self.tournament.reset_player_points()
        self.tournament_view.display()
        # Asks if user wants to continue tournament (Y/N)
        continue_tournament = self.tournament_view.get_command()
        while continue_tournament:
            round_controller = RoundController(self.tournament)
            round_controller.get_command()
            continue_tournament = False
