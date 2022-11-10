# -*- coding: utf-8 -*-
from src.model.lol_statistics import LolStatistics
from src.model.summoner import Summoner
from src.services.riot.league_of_legends.riot_lol_service import RiotLolService
from src.interface.statistics_interface import StatisticsServiceInterface
from src.services.riot.riot_service import RiotService


class LolStatisticsService(StatisticsServiceInterface):

    """
    Handle statistics lol data
    """

    __SUMMONER: str = "summoner"
    __STATISTICS: str = "statistics"
    __CHAMP: str = "champ"
    __WIN: str = "win"

    def __init__(self) -> None:
        self._service_name = "League of Legends"

    def get_service_name(self) -> str:
        return self._service_name

    def get_statistics(self, discord_id: str) -> Summoner:
        summoner_name: str = self._summoners.get(discord_id)
        riot_service: RiotService = RiotService(RiotLolService())
        summoner: Summoner = riot_service.get_summoner_data(summoner_name)
        summoner.discord_id = discord_id
        lol_statistics: LolStatistics = summoner.lol_statistics
        self.__process_statistics(lol_statistics)
        return summoner

    def __process_statistics(self, lol_statistics: LolStatistics) -> None:

        """
        Process and set statistics of summoner
        :param lol_statistics: Statistics to process
        """

        wins = {}
        defeat = {}
        played = {}
        win_count = 0
        def_count = 0
        matches: list[dict] = lol_statistics.matches

        for match in matches:

            champ: str = match[self.__CHAMP]
            try:
                played[champ] = played[champ] + 1
            except KeyError:
                played[champ] = 1

            if match[self.__WIN]:
                win_count = win_count + 1
                try:
                    wins[champ] = wins[champ] + 1
                except KeyError:
                    wins[champ] = 1
            else:
                def_count = def_count + 1
                try:
                    defeat[champ] = defeat[champ] + 1
                except KeyError:
                    defeat[champ] = 1

        lol_statistics.wins = wins
        lol_statistics.played = played
        lol_statistics.defeat = defeat

        all_matches: int = len(lol_statistics.matches)
        if all_matches == 0:
            lol_statistics.win_rate = 0
        else:
            lol_statistics.win_rate = (win_count / all_matches)
