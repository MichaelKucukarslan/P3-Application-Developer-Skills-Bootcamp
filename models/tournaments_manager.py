import json

from .tournament import Tournament
from models.players_manager import PlayersManager
from models.player import Player

class TournamentsManager:
    def __init__(self, data_folder="data/tournaments"):
        self.player_manager = PlayersManager()
        self.tournaments = []
        self.file_in_progress = data_folder + "/in-progress.json"
        self.file_future_tournaments = data_folder + "/completed.json"
        self.load_json_into_tournaments(self.file_in_progress)
        self.load_json_into_tournaments(self.file_future_tournaments)
        
    def load_json_into_tournaments(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            tournament_players = []
            for chess_id in data['players']:
                p = self.player_manager.get_player_from_chess_id(chess_id) 
                # print(p)
                tournament_players.append(p)
            tournament = Tournament(data['name'], data['dates']['from'], data['dates']['to'], 
                                    data['venue'], data['number_of_rounds'], data['current_round'],
                                    data['completed'], tournament_players ,data['finished'], 
                                    data['rounds'])
            self.tournaments.append(tournament)
    
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