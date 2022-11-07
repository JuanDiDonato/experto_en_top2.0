# -*- coding: utf-8 -*-
import logging
import time
from json import JSONDecodeError

import requests
from requests import Response

from ..model.summoner import Summoner
from ..model.statistics import Statistics

# Logging level config
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class RiotService:
    __API_URL: str = "https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner}"
    __API_MATCHES_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={time}"
    __API_MATCHES_DETAILS_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/{match}"
    __URL_PARAMS: dict = {"api_key": "INSERT API KEY HERE!"}
    __SUMMONER_PARAM: str = "{summoner}"
    __MATCH_PARAM: str = "{match}"
    __TIME_PARAM: str = "{time}"
    __PUU_ID_PARAM: str = "{puuid}"
    __PUU_ID: str = "puuid"
    __ACCOUNT_ID: str = "accountId"
    __INFO: str = "info"
    __PARTICIPANTS: str = "participants"
    __THREE_DAYS_AGO: int = int((time.time() - 259200))

    def get_summoner_account_data(self, summoner_name: str) -> Summoner:

        """
        Get and set account id and puu id of summoner by summoner name from riot api
        :param summoner_name:  Name of summoner in League of Legends
        """
        summoner: Summoner = Summoner(summoner_name)
        url: str = self.__API_URL.replace(self.__SUMMONER_PARAM, summoner_name)

        try:
            logging.info(f"Getting {summoner_name} data")
            response: Response = requests.get(url, self.__URL_PARAMS)
            if response.status_code == 200:
                response = response.json()
                summoner.puu_id = response[self.__PUU_ID]
                summoner.account_id = response[self.__ACCOUNT_ID]
        except JSONDecodeError as e:
            print(e.msg)

        self.__get_summoner_matches(summoner)
        return summoner

    def __get_summoner_matches(self, summoner: Summoner):

        """
        Get matches of summoner by puu id and set data in statistics class
        """
        puu_id: str = summoner.puu_id
        matches: dict = {}
        statistics: Statistics = Statistics()

        try:
            logging.info(f"Getting {summoner.summoner_name} matches")
            url: str = self.__API_MATCHES_URL.replace(self.__PUU_ID_PARAM, puu_id) \
                .replace(self.__TIME_PARAM, str(self.__THREE_DAYS_AGO))
            response: Response = requests.get(url, self.__URL_PARAMS)
            if response.status_code == 200:
                matches = response.json()
        except JSONDecodeError as e:
            print(e.msg)

        matches_results: list[dict] = []
        for match in matches:
            url: str = self.__API_MATCHES_DETAILS_URL.replace(self.__MATCH_PARAM, match)
            response = requests.get(url, self.__URL_PARAMS).json()

            for result in response[self.__INFO][self.__PARTICIPANTS]:
                if result[self.__PUU_ID] == puu_id:
                    match_result: dict = {"champ": result["championName"], "win": result["win"]}
                    matches_results.append(match_result)

        statistics.matches = matches_results
        summoner.statistics = statistics
