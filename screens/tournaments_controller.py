from commands import ExitCmd, NoopCmd
from models import TournamentsManager
# from .tournaments.view import TournamentView
from .tournament_controller import TournamentMenu
from .base_screen import BaseScreen


class TournamentsMenu(BaseScreen):
    """
    Tournaments Menu Screen
    This is the over world view of all past and current tournaments.
    The Tournament (Singular) Menu handles one tournament.
    """

    def __init__(self, players_manager, data_folder="data/tournaments"):
        # Load all tournaments into a list
        self.tournament_manager = TournamentsManager(data_folder)
        self.players_manager = players_manager

    def display(self):
        for idx, tournament in enumerate(self.tournament_manager.get_tournaments(), 1):
            print(idx, tournament.name)

    def get_command(self):
        keep_asking = True
        while keep_asking:
            print("**Tournaments Menu**")
            self.display()
            print()
            print("Type a number to access a current tournament.")
            print("Type C to create a new tournament.")
            print("Type B to go back.")
            value = self.input_string()
            if value.isdigit(): 
                # Display a tournament
                value = int(value)
                if value in range(1, len(self.tournament_manager.get_tournaments()) + 1):
                    tournament_menu = TournamentMenu(self.tournament_manager.get_tournament(value -1), self.players_manager)
                    tournament_menu.display()
                    pass
            elif value.upper() == "C":
                # [ ] Create a new tournament
                return NoopCmd("tournament-menu")
            elif value.upper() == "B":
                keep_asking = False
            else:
                print("Please input valid command.")