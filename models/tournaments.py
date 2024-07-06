import json
from pathlib import Path

from .tournament import Tournament
from models.players_manager import PlayersManager


class Tournaments:
    def __init__(self, data_folder="data/tournaments"):
        self.player_manager = PlayersManager()
        self.tournaments = []
        directory = Path(data_folder)
        files = [f for f in directory.iterdir() if f.is_file()]
        print(files)
        for file in files:
            self.load_json_into_tournaments(file)

    def load_json_into_tournaments(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            tournament_players = []
            for chess_id in data['players']:
                p = self.player_manager.get_player_from_chess_id(chess_id)
                tournament_players.append(p)
            tournament = Tournament(
                data['name'], data['dates']['from'], data['dates']['to'],
                data['venue'], data['number_of_rounds'], data['current_round'],
                data['completed'], tournament_players, data['finished'],
                data['rounds']
            )
            self.tournaments.append(tournament)
        self.tournaments = self.sort_tournaments(self.tournaments)

    def get_tournaments(self):
        return self.tournaments

    def get_tournament(self, tournament_number):
        return self.tournaments[tournament_number]

    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        tournament = Tournament(name=name, filepath=filepath)
        tournament.save()

        self.tournaments.append(tournament)
        return tournament

    def sort_tournaments(self, tournaments):
        sorted_tournaments = sorted(
            tournaments,
            key=lambda t: (t.completed, t.start_date)
        )
        return sorted_tournaments
