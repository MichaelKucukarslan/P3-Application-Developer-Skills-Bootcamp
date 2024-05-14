from commands import NoopCmd

from ..base_screen import BaseScreen

class TournamentView(BaseScreen):
    """Screen displayed when viewing the tournament menu"""

    def __init__(self):
        pass

    def display(self):
        print("Worked")

    def get_command(self):
        """Child classes must implement this method. It must return a Command."""
    pass