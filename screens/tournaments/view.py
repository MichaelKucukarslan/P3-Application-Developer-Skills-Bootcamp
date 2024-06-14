from ..base_screen import BaseScreen
import pandas as pd # type: ignore
from models.players_manager import PlayersManager

class TournamentView(BaseScreen):
    """Screen displayed when viewing the tournament menu"""

    def __init__(self, tournament, players_manager):
        self.tournament = tournament
        self.players_manager = players_manager
        pass

    def print_rounds(self):
        print("| Player 1    | Player 2    | Winner        | Player 1 points | Player 2 points |")
        print("| ----------  | ----------- | ------------- | --------------- | --------------- |")
        data = []
        for round_index, round_data in enumerate(self.tournament.rounds, start=1):
                for match_index, match in enumerate(round_data, start=1):
                    player_1 = self.players_manager.get_player_from_chess_id(match['players'][0]).name
                    player_2 = self.players_manager.get_player_from_chess_id(match['players'][1]).name
                    completed = "Completed" if match["completed"] else "Not Completed"
                    winner = match.get("winner", "None")
                    winner = "Tie Game" if winner is None else winner
                    data.append({
                        # 'Round': round_index,
                        # 'Match': match_index,
                        'Player 1': player_1,
                        'Player 2': player_2,
                        'Winner': winner,
                    })

    def display(self):
        print("Tournament Name: " + self.tournament.name)
        print("Venue Name: " + self.tournament.venue)
        print("Start Date: " + self.tournament.start_date)
        print("End Date: " + self.tournament.end_date)
        print("Player ID Numbers:")
        for player in self.tournament.players:
            print(f"\tID: {player.chess_id} \tName: {player.name}")
        if (self.tournament.current_round == 0):
            print("Tournament Completed")
        self.print_rounds()
    
    def get_command(self):
        """Child classes must implement this method. It must return a Command."""
        # If the tournament is done just display it
        # If the tournament is NOT done allow to continue it
    pass
