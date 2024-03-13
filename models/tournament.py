# Create tournament
# Create name
# A venue
# A start and end date
# A list of registered players
# A number of rounds
# A number corresponding to the current round being played

class Tournament:
    """A local tournament"""
    def __init__(self, name, venue, start_date, end_date, players, round_number, filepath):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.round_number = round_number
        self.current_round = 0
        self.filepath = filepath
