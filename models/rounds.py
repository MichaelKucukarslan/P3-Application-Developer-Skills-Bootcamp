

class Rounds:
    def __init__(self, tournament):
        self.tournament = tournament
        for player in self.tournament.wrapped_players_with_points:
            print("Rounds " + player.player.name + " " + str(player.points))