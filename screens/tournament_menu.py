from .tournaments.view import TournamentView
from models.printer import Printer


class TournamentMenu:
    """
    Tournament Menu will look at individual tournaments.
    If the tournament is done it will display the results of that
    tournament. If it is not complete it will ask the user if they 
    want to input the next rounds winners. 
    """
    
    def __init__(self, tournament, players_manager):
        self.players_manager = players_manager
        self.tournament = tournament
        self.tournament_view = TournamentView(tournament, players_manager)
        self.printer = Printer()
        pass

    def display(self):
        self.tournament_view.display()
        continue_tournament = self.tournament_view.get_command() # Asks if user wants to continue tournament (Y/N)
        current_round = self.tournament.current_round
        while continue_tournament:
            # create a new round with that tournament
            self.tournament.create_new_round()
            self.tournament.save()
            # get the latest round
            self.print_round(self.tournament.rounds[current_round])
            # display that round
            # get the winners of each round
            print("Who won these matches?")
            continue_tournament = False
            pass
        
    def print_round(self, rounds):
        print("| Player 1   | Player 2   |")
        max_length = 11
        for item in rounds:
            self.printer.print_row_of_info(item['players'], max_length)
    