from .base_screen import BaseScreen
# Does not have a tournament model because it is passed from calling class.
from .tournament.view import TournamentView
from models.round import Round

class TournamentController(BaseScreen):
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
        self.round = Round()
        pass

    def get_command(self):
        self.tournament_view.display()
        continue_tournament = self.tournament_view.get_command() # Asks if user wants to continue tournament (Y/N)
        current_round = self.tournament.current_round
        while continue_tournament:
            # create a new round with that tournament
            self.tournament.create_new_round()
            self.tournament.save()
            # get the latest round
            self.tournament.rounds.print_round(self.tournament.rounds[current_round])
            # display that round
            # get the winners of each round
            print("Who won these matches?")
            continue_tournament = False
            pass
        
    