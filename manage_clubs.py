from commands import ClubListCmd, TournamentListCmd
from screens import ClubCreate, ClubView, MainController, PlayerEdit, PlayerView, TournamentView, TournamentsController


class App:
    """The main controller for the club management program"""

    SCREENS = {
        "main-menu": MainController,
        "club-create": ClubCreate,
        "club-view": ClubView,
        "tournament-view": TournamentView,
        "tournament-menu": TournamentsController,
        "tournament-list": TournamentListCmd,
        "player-view": PlayerView,
        "player-edit": PlayerEdit,
        "player-create": PlayerEdit,
        "exit": False,
    }

    def __init__(self):
        # We start with the list of clubs (= main menu)
        command = ClubListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            # Get the screen class from the mapping
            screen = self.SCREENS[self.context.screen]
            try:
                # Run the screen and get the command
                command = screen(**self.context.kwargs).run()
                # Run the command and get a context back
                self.context = command()
            except KeyboardInterrupt:
                # Ctrl-C
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    app = App()
    app.run()
