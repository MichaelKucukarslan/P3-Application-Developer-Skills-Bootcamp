from ..base_screen import BaseScreen
from models.printer import Printer

# Passes models
from models.tournament import Tournament
from models.players_manager import PlayersManager


class TournamentView(BaseScreen):
    """Screen displayed when viewing the tournament menu"""

    def __init__(self, tournament: 'Tournament', players_manager: 'PlayersManager'):
        self.tournament = tournament
        self.players_manager = players_manager
        print(players_manager)
        self.printer = Printer()
        pass

    def print_rounds(self):
        for round_index, round in enumerate(self.tournament.rounds, start=1):
            print() # A space to make it easier to read. 
            print(f"Round {round_index}")
            round_data = []
            round_data.append(['Player 1', 'Player 2', 'Winner', "Player 1 points", "Player 2 points"])
            for match in round:
                match_data = []
                player_1 = self.tournament.get_player_from_chess_id(match['players'][0])
                player_2 = self.tournament.get_player_from_chess_id(match['players'][1])
                completed = "Completed" if match["completed"] else "Not Completed"
                winner = match.get("winner", "None")
                winner = "Tie Game" if winner is None else self.tournament.get_player_from_chess_id(winner).player.name
                self.tournament.calculate_rounds(match)
                match_data.append(player_1.player.name)
                match_data.append(player_2.player.name)
                match_data.append(winner)
                match_data.append(player_1.points)
                match_data.append(player_2.points)
                round_data.append(match_data)
            self.printer.print_rows_of_info(round_data)
            print()
            self.tournament.wrapped_players_with_points.sort(reverse=True)
            self.print_ranking(self.tournament.wrapped_players_with_points)
            print()

    def print_ranking(self, data):
        ranking_data = []
        for player in data:
            ranking_data.append([player.player.name, str(player.points)])
        ranking_data.sort(key=lambda x: x[1], reverse=True)
        ranking_data.insert(0, ['Player', 'Points'])
        self.printer.print_rows_of_info(ranking_data)

    def display(self):
        print("Tournament Name: " + self.tournament.name)
        print("Venue Name: " + self.tournament.venue)
        print("Start Date: " + self.tournament.start_date)
        print("End Date: " + self.tournament.end_date)
        print("Players in this tournament:")
        tournament_players = []
        tournament_players.append(['Player IDs', 'Name'])
        for player in self.tournament.players:
            tournament_players.append([player.chess_id, player.name])
        self.printer.print_rows_of_info(tournament_players)
        if (self.tournament.current_round == 0):
            print("This tournament had been completed. Final results are below.")
        self.print_rounds()
    
    def get_command(self):
        """Child classes must implement this method. It must return a Command."""
        keep_asking = True
        while keep_asking:
            # If the tournament is done just display it
            if self.tournament.completed == True:
                print("This tournament is complete.These are the final results. You will now be returned to the Tournaments Menu...")
                keep_asking = False
            # If the tournament is NOT done allow to continue it
            if self.tournament.completed == False:
                print("Do you want to enter the next round of winners? (Y/N)")
                value = self.input_string()
                if value.upper() == 'Y':
                    keep_asking = False
                    return True
                if value.upper() == 'N':
                    keep_asking = False
                    return False
