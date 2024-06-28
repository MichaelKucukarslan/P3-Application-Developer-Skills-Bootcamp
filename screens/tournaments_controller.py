from commands import ExitCmd, NoopCmd
from models import Tournaments
from screens.tournaments import TournamentsView
# from .tournaments.view import TournamentView
from .tournament_controller import TournamentController
from .base_screen import BaseScreen


class TournamentsController(BaseScreen):
    """
    Tournaments Menu Screen
    This is the over world view of all past and current tournaments.
    The Tournament (Singular) Menu handles one tournament.
    """

    def __init__(self, players_manager, data_folder="data/tournaments"):
        # Load all tournaments into a list
        self.tournament_manager = Tournaments(data_folder)
        self.tournaments_view = TournamentsView()
        self.players_manager = players_manager

    def get_command(self):
        keep_asking = True
        while keep_asking:
            self.tournaments_view.print_title()
            self.tournaments_view.print_tournaments(self.tournament_manager.get_tournaments())
            self.tournaments_view.print_menu()
            value = self.input_string()
            if value.isdigit(): 
                # Display a tournament
                value = int(value)
                if value in range(1, len(self.tournament_manager.get_tournaments()) + 1):
                    tournament_menu = TournamentController(self.tournament_manager.get_tournament(value -1), self.players_manager)
                    tournament_menu.display()
                    pass
            elif value.upper() == "C":
                # [ ] Create a new tournament
                return NoopCmd("tournament-menu")
            elif value.upper() == "B":
                keep_asking = False
            else:
                print("Please input valid command.")