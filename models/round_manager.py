from models.rounds import Rounds

class RoundManager:
    def __init__(self, tournament):
        self.tournament = tournament
        self.rounds = Rounds(self.tournament)
        for player in self.tournament.wrapped_players_with_points:
            print("Rounds Manager" + player.player.name + " " + str(player.points))
        self.create_next_round(tournament)

    def create_next_round(self, tournament):
        # create pairings
        # make rounds with those pairings
        # save it to json file as not completed rounds
        pairs = []
        for i in range(0, len(tournament.wrapped_players_with_points), 2):
            pairs.append((tournament.wrapped_players_with_points[i].player.chess_id, tournament.wrapped_players_with_points[i+1].player.chess_id))
            
        print(pairs)

    def new_round_to_json(self, pairs):
        