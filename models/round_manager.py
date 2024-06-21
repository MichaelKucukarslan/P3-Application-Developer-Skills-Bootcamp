import json
from models.rounds import Rounds

class RoundManager:
    def __init__(self, tournament):
        self.tournament = tournament
        self.rounds = Rounds(self.tournament)
        self.data = {"rounds": []}
        for player in self.tournament.wrapped_players_with_points:
            print("Rounds Manager" + player.player.name + " " + str(player.points))
        self.create_next_round(tournament)

    def create_next_round(self, tournament):
        # create pairings
        # make rounds with those pairings
        # save it to json file as not completed rounds
        rounds = []
        for i in range(0, len(tournament.wrapped_players_with_points), 2):
            player1 = tournament.wrapped_players_with_points[i].player.chess_id
            player2 = tournament.wrapped_players_with_points[i+1].player.chess_id
            rounds.append({
                "players":[player1, player2 ],
                "completed": False,
                "winner": None
                })    
        self.new_round_to_json(rounds)
        self.print_json(self.data)

    def new_round_to_json(self, rounds):
        self.data["rounds"].append(rounds)
        pass

    def print_json(self, data):
        json_data = json.dumps(data, indent=4)
        print(json_data)