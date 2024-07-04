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

    def print_ranking(self, data):
        ranking_data = []
        for player in data:
            ranking_data.append([player.player.name, str(player.points)])
        ranking_data.sort(key=lambda x: x[1], reverse=True)
        ranking_data.insert(0, ['Player', 'Points'])
        self.printer.print_rows_of_info(ranking_data)

    def print_completed_tournament(self, data):
        print()
        print("The tournament is over. Here are the final standings:")
        print()
        self.print_ranking(data)
    def get_continue_round(self):
        pass