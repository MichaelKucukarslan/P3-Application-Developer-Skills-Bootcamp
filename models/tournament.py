import json

from models.round import Round


class Tournament:
    """A local tournament"""
    def __init__(self, name=None, start_date=None, end_date=None, venue=None, 
                 number_of_rounds=None, current_round=None, completed=None, 
                 players=None, finished=None, rounds=None, file_folder="data/tournaments"):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round if current_round else 0
        self.completed = completed
        self.players = players
        self.finished = finished
        self.rounds = rounds
        self.wrapped_players_with_points = []
        for player in self.players:
            self.wrapped_players_with_points.append(TournamentPlayersWrapper(player))
        self.file_folder = file_folder

    def calculate_rounds(self, match):
        """Give a single match to calculate the newest round"""
        # find the winner
        winner = 'Tie Game' if match['winner'] is None else match['winner']
        # if tie add 0.5 to each player
        if winner == "Tie Game":
            self.add_to_player_points(match['players'][0], 0.5)
            self.add_to_player_points(match['players'][1], 0.5)
        # or add 1 point to the winner
        else:
            self.add_to_player_points(winner, 1.0)
            
    def get_player_from_chess_id(self, chess_id):
        for player in self.wrapped_players_with_points:
            if chess_id == player.player.chess_id:
                return player
        
    def add_to_player_points(self, chess_id, points_to_inc):
        for player in self.wrapped_players_with_points:
            if player.player.chess_id == chess_id:
                player.change_points(points_to_inc)

    def save(self):
        """Serialize the players and save them to the tournament into a JSON file"""
        file_name = ''
        if self.completed:
            file_name += '[Completed]'
        file_name += "".join(self.name.split())
        filepath = self.file_folder + '/' + file_name + '.json'
        with open(filepath, 'w') as fp:
            json.dump(self.serialize(), fp, indent=4)
        
    def serialize(self):
        return {
            "name": self.name,
            "dates": {
                "from": self.start_date,
                "to": self.end_date
            },
            "venue": self.venue,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "completed": self.completed,
            "players": [player.chess_id for player in self.players],
            "finished": self.finished,
            "rounds": self.rounds
        }
    
    def create_new_round(self):
        round = Round()
        new_round = round.create_next_round(self)
        self.rounds.append(new_round)
        self.save()

    def update_match(self, data):
        """Updates match and saves right away. 
        Given data should give the round, match, and winner. """
        self.rounds[data[0]][data[1]]['completed'] = True
        self.rounds[data[0]][data[1]]['winner'] = data[2]
        self.save()

        pass

    def get_latest_round(self):
        return(self.rounds[-1])

    def get_players_with_points(self):
        return self.wrapped_players_with_points
    

class TournamentPlayersWrapper:
    def __init__(self, player):
        self.player = player
        self.points = 0.0
    
    def change_points(self, increment):
        self.points = self.points + increment
    
    def __str__(self):
        return f"<Tournament Player Wrapper: {self.player.name}>"
    
    def __lt__(self, other):
        return self.points < other.points