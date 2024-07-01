from models.printer import Printer
from models.round import Round
from models.players_manager import PlayersManager

class RoundView:
    def __init__(self, round: Round):
        self.printer = Printer()
        self.players_manager = PlayersManager()
        self.round = round

    def display(self):
        print("Next Round:")
        data = []
        data.append(['Player 1', 'Player 2'])
        for match in self.round:
            player_1 = match['players'][0]
            player_2 = match['players'][1]
            player_1 = self.players_manager.get_player_from_chess_id(player_1)
            player_2 = self.players_manager.get_player_from_chess_id(player_2)
            data.append([player_1.name, player_2.name])
        self.printer.print_rows_of_info(data)