from ..base_screen import BaseScreen
import pandas as pd # type: ignore

class TournamentView(BaseScreen):
    """Screen displayed when viewing the tournament menu"""

    def __init__(self, tournament, players_manager):
        self.tournament = tournament
        self.players_manager = players_manager
        pass

    def print_rounds(self):
        for round_index, round_data in enumerate(self.tournament.rounds, start=1):
            print() # A space to make it easier to read. 
            print(f"Round {round_index}")
            print("| Player 1         | Player 2         | Winner           | Player 1 points  | Player 2 points  |")
            print("| ---------------  | ---------------- | ---------------- | ---------------- | ---------------- |")
            for match in round_data:
                # print(match)
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
                self.print_row_of_info(match_data, 17)
            print()
            self.tournament.wrapped_players_with_points.sort(reverse=True)
            self.print_ranking(self.tournament.wrapped_players_with_points)
            print()

    def print_ranking(self, data):
        length_max = 12
        print("| Player      | Points      |")
        print("| ----------- | ----------- |")
        for player in self.tournament.wrapped_players_with_points:
            self.print_row_of_info([player.player.name, str(player.points)], length_max)

    def print_row_of_info(self, data, length_max):
        pad_char = ' '
        for item in data:
            item = str(item)
            print('| ', end='')
            if len(item) > length_max:
                print(item[:length_max], end="")
            elif len(item) < length_max:
                print(item.ljust(length_max, pad_char), end="")
            else:
                print(item, end="")
        print('|')

    def display(self):
        print("Tournament Name: " + self.tournament.name)
        print("Venue Name: " + self.tournament.venue)
        print("Start Date: " + self.tournament.start_date)
        print("End Date: " + self.tournament.end_date)
        print("Players in this tournament:")
        data = []
        for player in self.tournament.players:
            data.append({
                'ID': player.chess_id,
                'Name': player.name
            })
        df = pd.DataFrame(data)
        print(df)
        if (self.tournament.current_round == 0):
            print("Tournament Completed")
        self.print_rounds()
    
    def get_command(self):
        """Child classes must implement this method. It must return a Command."""
        # If the tournament is done just display it
        # If the tournament is NOT done allow to continue it
    pass
