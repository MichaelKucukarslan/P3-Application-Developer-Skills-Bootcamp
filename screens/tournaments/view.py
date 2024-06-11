from ..base_screen import BaseScreen
import pandas as pd

class TournamentView(BaseScreen):
    """Screen displayed when viewing the tournament menu"""

    def __init__(self, tournament):
        self.tournament = tournament
        pass

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
        else:
            print("Current Round: " + str(self.tournament.current_round))
        for round_index, round_data in enumerate(self.tournament.rounds, start=1):
            print(f"Round {round_index}:")
            for match_index, match in enumerate(round_data, start=1):
                players = " vs ".join(match['players'])
                completed = "Completed" if match["completed"] else "Not Completed"
                winner = match.get("winner")
                winner_display = f"Winner: {winner}" if winner else "Tie Game"
                print(f"  Match {match_index}: {players}")
                print(f"    Status: {completed}")
                print(f"    {winner_display}")
            print()        
    data = []
    
    def get_command(self):
        """Child classes must implement this method. It must return a Command."""
        # If the tournament is done just display it
        # If the tournament is NOT done allow to continue it
    pass