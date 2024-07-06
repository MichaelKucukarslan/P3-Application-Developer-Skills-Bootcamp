from ..base_screen import BaseScreen

from datetime import datetime


class TournamentEdit(BaseScreen):
    """Screen displayed when creating a club"""

    display = "## Create tournament"

    def get_command(self):
        print("Type in the name of the tournament:")
        name = self.input_string()
        print("Type in the venue of the tournament:")
        venue = self.input_string()
        print("Type in the start date of the tournament:")
        date_entry = input('Example (i.e. 2017,7,1)')
        year, month, day = map(int, date_entry.split(','))
        start_date = datetime(year, month, day)
        print("Type in the end date of the tournament:")
        date_entry = input('Example (i.e. 2017,7,3)')
        year, month, day = map(int, date_entry.split(','))
        end_date = datetime(year, month, day)
        # Adding players is done in the next view
        # Calculating rounds is done after players have been entered
