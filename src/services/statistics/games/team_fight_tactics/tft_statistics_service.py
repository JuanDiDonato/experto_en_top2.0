# -*- coding: utf-8 -*-
from operator import itemgetter

from src.interface.statistics_interface import StatisticsServiceInterface
from src.model.summoner import Summoner
from src.model.tft_statistics import TftStatistics
from src.services.riot.team_fight_tactics.riot_tft_service import RiotTftService
from src.services.riot.riot_service import RiotService


class TftStatisticsService(StatisticsServiceInterface):

    def __init__(self) -> None:
        self._service_name = "Team Fight Tactics"

    def get_service_name(self) -> str:
        return self._service_name

    def get_statistics(self, discord_id: str) -> Summoner:
        riot_service: RiotService = RiotService(RiotTftService())
        summoner_name: str = self._summoners.get(discord_id)
        summoner: Summoner = riot_service.get_summoner_data(summoner_name)
        return self.__process_statistics(summoner)

    def __process_statistics(self, summoner: Summoner):
        tft_statistics: TftStatistics = summoner.tft_statistics

        if tft_statistics is not None:
            matches: list[dict] = tft_statistics.matches
            placements: list[int] = []
            levels: list[int] = []
            last_rounds: list[int] = []
            traits_used: dict = {}
            top_four: list = []
            top_eight: list = []

            for match in matches:
                placement: int = match.get("placement")
                placements.append(placement)
                levels.append(match.get("level"))
                last_rounds.append(match.get("last_round"))

                traits: list[dict] = match.get("traits")
                trait_used: str = self.__get_used_traits(traits)
                if placement <= 4:
                    top_four.append(trait_used)
                else:
                    top_eight.append(trait_used)

            traits_used["wins"] = top_four
            traits_used["defeats"] = top_eight
            tft_statistics.rounds = last_rounds
            tft_statistics.levels = levels
            tft_statistics.placements = placements
            tft_statistics.traits = traits_used

        summoner.tft_statistics = tft_statistics
        return summoner

    def __get_used_traits(self, traits: list[dict]) -> str:
        traits_used: dict = {}
        for t in traits:
            tier_current: int = t.get("tier_current")
            if t.get("tier_current") > 0:
                name: str = t.get("name")
                traits_used[name] = tier_current

        if len(traits_used) > 0:
            return max(traits_used.items(), key=itemgetter(1))[0]
        else:
            return "Sin composicion"

