# -*- coding: utf-8 -*-

# Python Modules
import math
import logging
from operator import itemgetter

# App Modules
from src.utils.embed.embed_builder import EmbedBuilder
from src.model.lol_statistics import LolStatistics

# Logging level config
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class EmbedLolStatisticsBuilder(EmbedBuilder):

    """
    Builder that extends of EmbedBuilder and add statistics support
    """

    __lol_statistics: LolStatistics

    def __init__(self) -> None:
        super().__init__()

    def with_statistics(self, statistics: LolStatistics) -> EmbedBuilder:
        self.__lol_statistics = statistics
        self.__process_statistics()
        return self

    def __process_statistics(self):
        logging.info("Setting summoner statistics")
        self.__set_wins()
        self.__set_defeats()
        self.__set_win_rate()
        self.__set_matches_played()

    def __set_wins(self):
        wins = self.__lol_statistics.wins
        if len(wins) > 0:
            most_wins = max(wins.items(), key=itemgetter(1))[0]  # Retorna con que campeon gano mas
            self.with_field(
                name=f"Mayor cantidad de victorias con {most_wins}",
                value=f" {wins[most_wins]} victorias",
            )

    def __set_defeats(self):
        defeats = self.__lol_statistics.defeat
        if len(defeats) > 0:
            most_defeat = max(defeats.items(), key=itemgetter(1))[0]  # Retorna con que campeon perdio mas
            self.with_field(
                name=f"Muchas derrotas con {most_defeat}",
                value=f"{defeats[most_defeat]} derrotas",
            )

    def __set_win_rate(self):
        win_rate = self.__lol_statistics.win_rate
        self.with_field(name=f"Porcentaje de victorias total ", value=f"{str(math.trunc(win_rate * 100))}%")

    def __set_matches_played(self):
        matches: dict = self.__lol_statistics.played
        wins: dict = self.__lol_statistics.wins
        one_match: list[str] = []
        for c, p in matches.items():
            if p == 1:
                one_match.append(c)
            else:
                try:
                    win_rate = int((wins[c] / p) * 100)
                except KeyError:
                    win_rate = 0

                self.with_field(
                    name=f"Participo en {p} partidas con {c}", value=f" Porcentaje de victorias: {win_rate} %"
                )

        champs: str = " "
        for c in one_match:
            champs = champs + c + "\n"

        self.with_field(
            name=f"Jugo solo una partida con", value=champs
        )
