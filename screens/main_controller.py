from commands import ExitCmd, NoopCmd
from models.players_manager import PlayersManager
from .tournaments_controller import TournamentsController
from .base_screen import BaseScreen


class MainController(BaseScreen):
    """Main menu screen
        This is a given class and will not adhere to my model view controller pattern.
        """

    def __init__(self, clubs):
        self.clubs = clubs
        self.players_manager = PlayersManager()

    def display(self):
        for idx, club in enumerate(self.clubs, 1):
            print(idx, club.name)

    def get_command(self):
        while True:
            print("**Main Menu**")
            print("Type C to create a club or a club number to view/edit it.")
            print("Type T to enter the tournament menu.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.clubs) + 1):
                    return NoopCmd("club-view", club=self.clubs[value - 1])
            elif value.upper() == "C":
                return NoopCmd("club-create")
            elif value.upper() == "T":
                tournaments_manager = TournamentsController(self.players_manager)
                tournaments_manager.get_command()
            elif value.upper() == "X":
                return ExitCmd()
