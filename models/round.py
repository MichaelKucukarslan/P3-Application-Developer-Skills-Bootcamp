import json
from models.printer import Printer

class Round:
    def __init__(self):
        # self.data = data
        self.rounds = []
        self.printer = Printer()

    def create_next_round(self, tournament):
    # create pairings
        rounds = []
        for i in range(0, len(tournament.wrapped_players_with_points), 2):
            player1 = tournament.wrapped_players_with_points[i].player.chess_id
            player2 = tournament.wrapped_players_with_points[i+1].player.chess_id
            # make rounds with those pairings
            rounds.append({
                "players":[player1, player2],
                "completed": False,
                "winner": None
                })
        self.rounds = rounds
        return rounds

    def print_round(self, rounds):
        print("| Player 1   | Player 2   |")
        max_length = 11
        for item in rounds:
            self.printer.print_row_of_info(item['players'], max_length)

    def new_round_to_json(self, rounds):
        self.data["rounds"].append(rounds)
        pass

    def print_json(self, data):
        json_data = json.dumps(data, indent=4)
        print(json_data)