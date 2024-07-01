from models.printer import Printer
from models.players_manager import PlayersManager
from models.match import Match

class MatchView():
    def __init__(self, match: Match):
        self.pm = PlayersManager()
        self.printer = Printer()
        self.match = match

    def display(self):
        data = []
        data.append(['Player 1', 'Player 2'])
        player_1 = self.pm.get_player_from_chess_id(self.match['players'][0]).name
        player_2 = self.pm.get_player_from_chess_id(self.match['players'][1]).name
        data.append([player_1, player_2])
        self.printer.print_rows_of_info(data)
