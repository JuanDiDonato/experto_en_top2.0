# -*- coding: utf-8 -*-

# Python Modules
import math
import logging
from operator import itemgetter

# App Modules
from .embed_builder import EmbedBuilder
from ..model.statistics import Statistics

# Logging level config
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class EmbedStatisticsBuilder(EmbedBuilder):

    """
    Builder that extends of EmbedBuilder and add statistics support
    """

    __statistics: Statistics

    def __init__(self) -> None:
        super().__init__()

    def with_statistics(self, statistics: Statistics) -> EmbedBuilder:
        self.__statistics = statistics
        self.__process_statistics()
        return self

    def __process_statistics(self):
        logging.info("Setting summoner statistics")
        self.__set_wins()
        self.__set_defeats()
        self.__set_win_rate()
        self.__set_matches_played()

    def __set_wins(self):
        wins = self.__statistics.wins
        if len(wins) > 0:
            most_wins = max(wins.items(), key=itemgetter(1))[0]  # Retorna con que campeon gano mas
            self.with_field(
                name=f"Win more matches with {most_wins}",
                value=f" {wins[most_wins]} victories",
            )

    def __set_defeats(self):
        defeats = self.__statistics.defeat
        if len(defeats) > 0:
            most_defeat = max(defeats.items(), key=itemgetter(1))[0]  # Retorna con que campeon perdio mas
            self.with_field(
                name=f"Lost more matches with {most_defeat}",
                value=f"{defeats[most_defeat]} defeats",
            )

    def __set_win_rate(self):
        win_rate = self.__statistics.win_rate
        self.with_field(name=f"Percentage of wins", value=f"{str(math.trunc(win_rate * 100))}%")

    def __set_matches_played(self):
        matches: dict = self.__statistics.played
        wins: dict = self.__statistics.wins
        for c, p in matches.items():
            try:
                win_rate = int((wins[c] / p) * 100)
            except KeyError:
                win_rate = 0

            self.with_field(
                name=f"Played {p} matches with {c}", value=f" Win rate: {win_rate} %"
            )
