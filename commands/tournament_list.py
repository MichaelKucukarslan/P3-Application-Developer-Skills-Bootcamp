from commands.context import Context
from models import TournamentManager
from models import ClubManager

from .base import BaseCommand


class TournamentListCmd(BaseCommand):
    """Command to get the list of clubs"""

    def execute(self):
        # tm = TournamentManager()
        # return Context("tournament-menu", tournaments=tm.tournaments)
        cm = ClubManager()
        return Context("main-menu", clubs=cm.clubs)