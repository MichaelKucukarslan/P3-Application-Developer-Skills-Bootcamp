import json
from pathlib import Path

from .tournament import Tournament


class TournamentManager:
    def __init__(self, data_folder="data/tournaments"):
        print("Tournament Manager")
        self.tournaments = []
        self.file_in_progress = data_folder + "/in-progress.json"
        self.file_future_tournaments = data_folder + "/completed.json"
        self.load_json_into_tournaments(self.file_in_progress)
        self.load_json_into_tournaments(self.file_future_tournaments)     
        
    def load_json_into_tournaments(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            tournament = Tournament(data['name'], data['venue'], data['dates']['from'], data['dates']['to'], data['players'], data['rounds'])
            self.tournaments.append(tournament)
    
    def get_tournaments(self):
        return self.tournaments
    
    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        tournament = Tournament(name=name, filepath=filepath)
        tournament.save()

        self.tournaments.append(tournament)
        return tournament