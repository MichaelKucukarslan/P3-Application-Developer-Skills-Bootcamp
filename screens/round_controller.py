from .base_screen import BaseScreen
from models.tournament import Tournament
from screens.tournament import TournamentView
from models.players_manager import PlayersManager
from models.round import Round
from screens.rounds import RoundView
from models.match import Match 
from .match_controller import Match_Controller

class RoundController(BaseScreen):
    """
    Round Menu is called when the user wants to continue a tournament.
    It first creates the next round. Then allows the user to input winners for that round.
    """
    def __init__(self, tournament: Tournament, data_folder="data/tournaments"):
        self.tournament = tournament
        self.tournament.create_new_round()
        self.tournament.save()
        self.display()
        self.round = self.tournament.get_latest_round()
        pass

    def display(self):
        print()
        print("**Round Menu**")
        print()
        round_view = RoundView(self.tournament.get_latest_round())
        round_view.display()
        pass

    def get_command(self):
        """Returns True if the rounds are done."""
        print("Current Round:" + str(self.tournament.current_round) + " Number of rounds: " + str(self.tournament.number_of_rounds))
        while self.tournament.current_round <= self.tournament.number_of_rounds:
            print()
            for match_index, match in enumerate (self.round, 0):
                match_controller = Match_Controller(match)
                winner = match_controller.get_command()
                self.tournament.update_match([self.tournament.current_round, match_index, winner])                
            self.tournament.current_round += 1
            self.tournament.save()
            print()
            print("**New standings**")
            print()
            round_view = RoundView(self.tournament.get_latest_round())
            round_view.print_ranking(self.tournament.get_players_with_points())
            for match in self.round:
                self.tournament.calculate_match(match)
            if self.tournament.current_round == self.tournament.number_of_rounds:
                self.tournament.completed = True
                round_view.print_completed_tournament(self.tournament.get_players_with_points())
                self.tournament.save()
                break
            value = self.input_string("Do you want to continue to the next round? ('Y'/'N')")
            if value.upper() == 'Y' and self.tournament.current_round != self.tournament.number_of_rounds: 
                self.tournament.create_new_round()
