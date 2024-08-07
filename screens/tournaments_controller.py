from commands import ExitCmd, NoopCmd
from models import Tournaments
from screens.tournaments import TournamentsView
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
            self.tournaments_view.print_tournaments(
                self.tournament_manager.get_tournaments()
            )
            self.tournaments_view.print_menu()
            value = self.input_string()
            if value.isdigit():
                # Display a tournament
                value = int(value)
                tournaments_count = len(
                    self.tournament_manager.get_tournaments()
                ) + 1
                if value in range(1, tournaments_count):
                    tournament_menu = TournamentController(
                        self.players_manager,
                        self.tournament_manager.get_tournament(value - 1)
                    )
                    tournament_menu.get_command()
                    pass
            elif value.upper() == "C":
                tournament_menu = TournamentController(self.players_manager)
                return NoopCmd("tournament-menu")
            elif value.upper() == "B":
                keep_asking = False
            else:
                print("Please input valid command.")
