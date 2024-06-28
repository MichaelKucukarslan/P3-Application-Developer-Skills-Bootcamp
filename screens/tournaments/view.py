from models.printer import Printer 

class TournamentsView():
    """Screen displayed when viewing the tournaments menu"""
    def __init__(self):
        self.printer = Printer()
        pass

    def print_title(self):
        print("")
        print("**Tournaments Menu**")

    def print_tournaments(self, tournaments):
        for idx, tournament in enumerate(tournaments, 1):
            print(idx, tournament.name)

    def print_menu(self):
        print()
        print("Type a number to access a current tournament.")
        print("Type C to create a new tournament.")
        print("Type B to go back.")
        