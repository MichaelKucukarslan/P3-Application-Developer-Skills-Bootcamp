from rounds import Rounds

class RoundManager:
    def __init__(self, tournament):
        self.tournament = tournament
        self.rounds = Rounds(self.tournament)
        for player in self.tournament.wrapped_players_with_points:
            print("Rounds " + player.player.name + " " + str(player.points))