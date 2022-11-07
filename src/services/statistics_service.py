# -*- coding: utf-8 -*-

from ..model.statistics import Statistics
from ..model.summoner import Summoner
from .riot_service import RiotService


class StatisticsService:

    """
    Handle statistics data
    """

    __riot: RiotService = RiotService()
    __SUMMONER: str = "summoner"
    __STATISTICS: str = "statistics"
    __CHAMP: str = "champ"
    __WIN: str = "win"
    __summoners = {
        "<@411704033225605130>": "D1D0",
        "<@602993773940572220>": "KARTTA",
        "<@748722234931282020>": "P4RF3CTO",
        "<@258683657038856193>": "Nezah",
        "<@583500343426547712>": "elioelmufa",
        "<@544348597991243786>": "MaitoChoy",
        "<@712826508229476382>": "Behamoth",
        "<@515334245166743574>": "BALANCE iRELIA",
    }

    def get_statistics(self, discord_id: str) -> Summoner:
        summoner_name: str = self.__summoners.get(discord_id)
        summoner: Summoner = self.__riot.get_summoner_account_data(summoner_name)
        summoner.discord_id = discord_id
        statistics: Statistics = summoner.statistics
        self.__process_statistics(statistics)
        return summoner

    def __process_statistics(self, statistics: Statistics) -> None:

        """
        Process and set statistics of summoner
        :param statistics: Statistics to process
        """

        wins = {}
        defeat = {}
        played = {}
        win_count = 0
        def_count = 0
        matches: list[dict] = statistics.matches

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

        statistics.wins = wins
        statistics.played = played
        statistics.defeat = defeat

        all_matches: int = len(statistics.matches)
        if all_matches == 0:
            statistics.win_rate = 0
        else:
            statistics.win_rate = (win_count / all_matches)
