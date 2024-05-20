from ..base_screen import BaseScreen

class TournamentView(BaseScreen):
    """Screen displayed when viewing the tournament menu"""

    def __init__(self, tournament):
        self.tournament = tournament
        pass

    def display(self):
        print("Tournament Name: " + self.tournament.name)
        print("Venue Name: " + self.tournament.venue)
        print("Start Date: " + self.tournament.start_date)
        print("End Date: " + self.tournament.end_date)
        print("Player ID Numbers:")
        for player in self.tournament.players:
            print(f"\tID: {player} \tName:")
        print("Current Round: " + str(self.tournament.current_round))
        

    def get_command(self):
        """Child classes must implement this method. It must return a Command."""
    pass