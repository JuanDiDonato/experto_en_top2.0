# -*- coding: utf-8 -*-
import logging
from json import JSONDecodeError

import requests
from requests import Response

from src.interface.riot_interface import RiotInterface
from src.model.summoner import Summoner
from src.model.tft_statistics import TftStatistics

# Logging level config
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class RiotTftService(RiotInterface):
    #  Private fields
    __API_MATCHES_URL = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?startTime={time}"
    __API_MATCHES_DETAILS_URL = "https://americas.api.riotgames.com/tft/match/v1/matches/{match}"

    def find_statistics(self, summoner_name: str) -> Summoner:
        summoner: Summoner = self._get_summoner_account_data(summoner_name)
        self.__get_summoner_matches(summoner)
        return summoner

    def __get_summoner_matches(self, summoner: Summoner) -> Summoner:

        puu_id: str = summoner.puu_id
        matches: dict = {}
        tft_statistics: TftStatistics = TftStatistics()

        try:
            logging.info(f"Getting {summoner.summoner_name} tft matches")
            url: str = self.__API_MATCHES_URL.replace(self._PUU_ID_PARAM, puu_id) \
                .replace(self._TIME_PARAM, str(self._SEVEN_DAYS_AGO))
            response: Response = requests.get(url, self._URL_PARAMS)
            if response.status_code == 200:
                matches = response.json()
        except JSONDecodeError as e:
            print(e.msg)

        matches_results: list[dict] = []
        for match in matches:
            url: str = self.__API_MATCHES_DETAILS_URL.replace(self._MATCH_PARAM, match)
            response = requests.get(url, self._URL_PARAMS).json()

            for result in response[self._INFO][self._PARTICIPANTS]:
                if result[self._PUU_ID] == puu_id:
                    match_result: dict = {
                        "level": result["level"],
                        "last_round": result["last_round"],
                        "placement": result["placement"],
                        "traits": self.__get_traits(result["traits"])
                        # "units": result["units"]
                    }
                    matches_results.append(match_result)

        tft_statistics.matches = matches_results
        summoner.tft_statistics = tft_statistics
        return summoner

    def __get_traits(self,traits: list[dict]) -> list[dict]:
        active_traits: list[dict] = []
        for trait in traits:
            if trait.get("tier_current") > 0:
                active_traits.append(trait)
        return active_traits



