# -*- coding: utf-8 -*-
import logging
from json import JSONDecodeError

import requests
from requests import Response

from src.model.summoner import Summoner
from src.model.lol_statistics import LolStatistics
from src.interface.riot_interface import RiotInterface

# Logging level config
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class RiotLolService(RiotInterface):
    """
    Handle all request and data from Riot API
    """

    __API_MATCHES_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={time}"
    __API_MATCHES_DETAILS_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/{match}"

    def find_statistics(self, summoner_name: str) -> Summoner:
        summoner: Summoner = self._get_summoner_account_data(summoner_name)
        return self.__get_summoner_matches(summoner)

    def __get_summoner_matches(self, summoner: Summoner) -> Summoner:

        """
        Get matches of summoner by puu id and set data in statistics class
        :param summoner: Summoner to get matches
        """

        puu_id: str = summoner.puu_id
        matches: dict = {}
        lol_statistics: LolStatistics = LolStatistics()

        try:
            logging.info(f"Getting {summoner.summoner_name} matches")
            url: str = self.__API_MATCHES_URL.replace(self._PUU_ID_PARAM, puu_id) \
                .replace(self._TIME_PARAM, str(self._THREE_DAYS_AGO))
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
                    match_result: dict = {"champ": result["championName"], "win": result["win"]}
                    matches_results.append(match_result)

        lol_statistics.matches = matches_results
        summoner.lol_statistics = lol_statistics
        return summoner
