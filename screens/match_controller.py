from .base_screen import BaseScreen
from models.match import Match 
from screens.match import MatchView

class Match_Controller(BaseScreen):
    def __init__(self, match: Match):
        self.match = match
        pass

    def get_command(self):
        print("Who won? Player 1 or Player 2")
        print("Enter '3' for a tie game.")
        match_view = MatchView(self.match)
        match_view.display()
        # print(self.match)
        correct_input = False
        while not correct_input:
            input = self.input_string()
            if input == '1' or input == '2':
                correct_input = True
                return self.match['players'][int(input) - 1]
            elif input == '3':
                correct_input = True
                return None