import json

from .tournament import Tournament


class TournamentsManager:
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
            tournament = Tournament(data['name'], data['dates']['from'], data['dates']['to'], 
                                    data['venue'], data['number_of_rounds'], data['current_round'],
                                    data['completed'], data['players'],data['finished'], 
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