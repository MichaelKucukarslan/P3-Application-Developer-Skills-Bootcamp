import json


class Round:
    def __init__(self):
        # self.data = data
        self.rounds = []

    def create_next_round(self, tournament):
        # create pairings
        rounds = []
        for i in range(0, len(tournament.wrapped_players_with_points), 2):
            player1 = (tournament.wrapped_players_with_points[i].
                       player.chess_id)
            player2 = (tournament.wrapped_players_with_points[i+1].
                       player.chess_id)
            # make rounds with those pairings
            rounds.append({
                "players": [player1, player2],
                "completed": False,
                "winner": None
                })
        self.rounds = rounds
        return rounds

    def new_round_to_json(self, rounds):
        self.data["rounds"].append(rounds)
        pass

    def print_json(self, data):
        json_data = json.dumps(data, indent=4)
        print(json_data)
