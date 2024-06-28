from commands.context import Context
from models import Tournaments

from .base import BaseCommand


class TournamentCreateCmd(BaseCommand):
    """Command to create a club"""

    def __init__(self, name):
        self.name = name

    def execute(self):
        """Uses a ClubManager instance to create the club and add it to the list of managed clubs"""
        tm = Tournaments()
        club = tm.create(self.name)
        return Context("club-view", club=club)