from commands import ExitCmd, NoopCmd
from models import TournamentsManager
from .tournaments.view import TournamentView
from .base_screen import BaseScreen


class TournamentsMenu(BaseScreen):
    """Tournament Menu Screen"""

    def __init__(self, data_folder="data/tournaments"):
        # Load all tournaments into a list
        self.tournament_manager = TournamentsManager()

    def display(self):
        print("**Tournament Menu**")
        for idx, tournament in enumerate(self.tournament_manager.get_tournaments(), 1):
            print(idx, tournament.name)
    
    def get_command(self):
        keep_asking = True
        while keep_asking:
            print("")
            # view a tournament
            # create a new tournament
            # ask user for input
            print("Type a number to access a current tournament.")
            print("Type C to create a new tournament.")
            print("Type B to go back.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.tournament_manager.get_tournaments()) + 1):
                    view = TournamentView(self.tournament_manager.get_tournament(value - 1))
                    view.display()
                    pass
            elif value.upper() == "C":
                return NoopCmd("tournament-menu")
            elif value.upper() == "B":
                keep_asking = False
            print("Please input valid command.")