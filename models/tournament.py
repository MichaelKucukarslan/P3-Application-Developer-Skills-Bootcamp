import json

from .player import Player

class Tournament:
    """A local tournament"""
    def __init__(self, name=None, start_date=None, end_date=None, venue=None, 
                 number_of_rounds=None, current_round=None, completed=None, 
                 players=None, finished=None, rounds=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        if current_round:
            self.current_round = current_round
        else:
            self.current_round = 0 
        self.completed = completed
        self.players = players
        self.finished = finished
        self.rounds = rounds
        self.wrapped_players_with_points = []
        for player in self.players:
            self.wrapped_players_with_points.append(TournamentPlayersWrapper(player))

    def calculate_rounds(self, rounds):
        # find the winner
        # print(rounds)
        winner = 'Tie Game' if rounds['winner'] is None else rounds['winner']
        # print("Tournament: " + winner)
        # if tie add 0.5 to each player
        if winner == "Tie Game":
            # print(rounds['players'])
            self.add_to_player_points(rounds['players'][0], 0.5)
            self.add_to_player_points(rounds['players'][1], 0.5)
        # add 1 point to the winner
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

    # Save file
    def save(self):
        """Serialize the players and save them to the tournament into a JSON file"""

        with open(self.filepath, "w") as fp:
            json.dump(
                {"name": self.name, "players": [p.serialize() for p in self.players]},
                fp,
            )

class TournamentPlayersWrapper:
    def __init__(self, player):
        self.player = player
        self.points = 0.0
    
    def change_points(self, increment):
        self.points = self.points + increment
    
    def __str__(self):
        return f"<{self.player.name}>"