import json
from commands import ExitCmd, NoopCmd
from models import TournamentManager, Tournament
from .base_screen import BaseScreen


class TournamentMenu(BaseScreen):
    """Tournament Menu Screen"""

    def __init__(self, data_folder="data/tournaments"):
        self.tournaments = []
        self.file_in_progress = data_folder + "/in-progress.json"
        self.file_future_tournaments = data_folder + "/completed.json"
        self.load_json_into_tournaments(self.file_in_progress)
        self.load_json_into_tournaments(self.file_future_tournaments)

    def load_json_into_tournaments(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            # start_date=None, end_date=None, players=None, round_number=None):
            tournament = Tournament(data['name'], data['venue'], data['dates']['from'], data['dates']['to'], data['players'], data['rounds'])
            self.tournaments.append(tournament)

    def display(self):
        print("**Tournament Menu**")
        for idx, tournament in enumerate(self.tournaments, 1):
            print(idx, tournament.name)
    
    def get_command(self):
        while True:
            # view all tournament
            # create a new tournament
            # ask user for input
            print("Type a number to access a current tournament.")
            print("Type C to create a new tournament.")
            print("Type B to go back.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.clubs) + 1):
                    return NoopCmd("club-view", club=self.clubs[value - 1])
            elif value.upper() == "C":
                return NoopCmd("tournament-menu")
            elif value.upper() == "X":
                return ExitCmd()
        pass