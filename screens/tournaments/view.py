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
        data = [['Index', 'Name', 'Start Date', 'Completed']]
        for idx, tournament in enumerate(tournaments, 1):
            data.append([
                idx,
                tournament.name,
                tournament.start_date,
                tournament.completed
                ])
        self.printer.print_rows_of_info(data)

    def print_menu(self):
        print()
        print("Type a number to access a current tournament.")
        print("Type C to create a new tournament.")
        print("Type B to go back.")
