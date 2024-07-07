from models.printer import Printer
from models.tournament import Tournament
from datetime import datetime
from models.players_manager import PlayersManager
import re


class TournamentCreateView:
    def __init__(self):
        self.printer = Printer()
        self.tournament = Tournament()
        self.player_manager = PlayersManager()

    def create_tournament(self):
        print("Thank you for creating a new tournament.")
        print("Please input the following information:")
        user_input = input("Name of tournament:")
        self.tournament.name = user_input
        user_input = self.get_user_date(
            "Start date of tournament: (Format YYYY-MM-DD)"
            )
        self.tournament.start_date = user_input
        user_input = self.get_user_date(
            "End date of tournament: (Format YYYY-MM-DD)"
            )
        self.tournament.end_date = user_input
        user_input = str(input("The name of the venue:"))
        self.tournament.venue = user_input
        user_input = self.get_user_integer("Number of rounds:")
        self.tournament.number_of_rounds = user_input
        self.tournament.current_round = 0
        self.tournament.completed = False
        # Add players
        self.tournament.players = []
        self.ask_for_players()
        # [ ] For testing; Remove when done.
        # self.ask_for_players("LU33889")
        # self.ask_for_players("YJ29085")
        # self.ask_for_players("PB43166")
        # self.ask_for_players("XW31336")
        self.tournament.create_new_round()
        self.tournament.save()

    def ask_for_players(self, chess_id=None):
        if chess_id is not None:
            player = self.get_player(chess_id)
            self.tournament.players.append(player)
            return
        more_players = True
        print("Players can only be added by Chess IDs. "
              "If you enter a name it will return a list of names and IDs. "
              "You can then input the ID to add the player. "
              "Chess IDS are in the format AA11111"
              )
        print("What player do you want to add?")
        while more_players:
            user_input = input("Name or Chess ID:\n")
            possible_player = self.get_player(user_input)
            if possible_player is not None:
                self.tournament.players.append(possible_player)
            else:
                player_search =  self.player_manager.search_player_by_name(
                    user_input
                )
                player_search_print = []
                player_search_print.append(['Index', 'Name', 'Chess ID'])
                for index, player in enumerate(player_search, start=1):
                    player_search_print.append([index,
                                                player.name,
                                                player.chess_id]
                                            )
                self.printer.print_rows_of_info(player_search_print)
                # print("Pick a number to add the player to the tournament.")
                user_input = self.get_int_from_string("Pick a number to add the player to the tournament.")
                if type(user_input) is int:
                    if 1 <= int(user_input) <= len(player_search):
                        possible_player = self.get_player(player_search[user_input - 1].chess_id)
                        if possible_player is not None:
                            self.tournament.players.append(possible_player)
                else:
                    print("Index out of range")
                pass
            user_input = TournamentCreateView.get_yes_or_no(
                "Do you still want to add more players? Y/N"
                )
            more_players = True if user_input == 'Y' else False

    @staticmethod
    def get_int_from_string(prompt):
        user_input = input(prompt)
        try:
            # Try to convert the input to an integer
            user_input_as_int = int(user_input)
            return user_input_as_int
        except ValueError:
            # If conversion fails, return the original string
            return user_input

    @staticmethod
    def get_yes_or_no(prompt):
        while True:
            user_input = input(prompt).strip().upper()
            if user_input in ['Y', 'N']:
                return user_input
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

    def get_player(self, possible_player):
        # check if the player exists
        player = None
        if self.is_chess_id_format(possible_player):
            player = self.player_manager.get_player_from_chess_id(
                possible_player
                )
        # return that player
        return player
        # return none if it doesn't exist

    def is_chess_id_format(self, s):
        # Define the regex pattern
        pattern = r'^[A-Za-z]{2}\d{5}$'
        return bool(re.match(pattern, s))

    @staticmethod
    def get_user_date(prompt):
        while True:
            user_input = input(prompt)
            try:
                user_date = datetime.strptime(user_input, "%Y-%m-%d")
                return user_date
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    @staticmethod
    def get_user_integer(prompt):
        while True:
            user_input = input(prompt)
            try:
                # Attempt to convert the input to an integer
                user_integer = int(user_input)
                return user_integer
            except ValueError:
                print("Invalid input. Please enter an integer.")
