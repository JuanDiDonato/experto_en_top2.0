# -*- coding: utf-8 -*-

# Python modules
import datetime
import time
from abc import ABC, abstractmethod  # Abstract Base Classes

# App Modules
from json import JSONDecodeError

import requests
from requests import Response

from ..model.summoner import Summoner


class RiotInterface(ABC):

    # Private fields
    __API_URL: str = "https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner}"

    #  Protected fields
    _URL_PARAMS: dict = {"api_key": "RGAPI-7299307d-8fe8-42cd-8d53-c6e6f14c28ab"} # Development token that expires
    _SUMMONER_PARAM: str = "{summoner}"
    _MATCH_PARAM: str = "{match}"
    _TIME_PARAM: str = "{time}"
    _PUU_ID_PARAM: str = "{puuid}"
    _PUU_ID: str = "puuid"
    _ACCOUNT_ID: str = "accountId"
    _INFO: str = "info"
    _PARTICIPANTS: str = "participants"
    _THREE_DAYS_AGO: int = int((time.time() - 259200))
    _SEVEN_DAYS_AGO: int = int((time.time() - 604800))
    _summoners: list[Summoner] = []  # TODO: Replace this list for db

    @abstractmethod
    def find_statistics(self, summoner_name: str) -> Summoner:
        pass

    def _get_summoner_account_data(self, summoner_name: str) -> Summoner:

        """
        Get and set account id and puu id of summoner by summoner name from riot api
        :param summoner_name:  Name of summoner in League of Legends
        """

        summoner: Summoner = self.__find_summoner(summoner_name)
        if summoner.puu_id is "" or summoner.account_id is "":
            print(f"Not data for summoner {summoner_name}, request to api in progress")
            url: str = self.__API_URL.replace(self._SUMMONER_PARAM, summoner_name)

            try:
                response: Response = requests.get(url, self._URL_PARAMS)
                if response.status_code == 200:
                    response = response.json()
                    summoner.puu_id = response[self._PUU_ID]
                    summoner.account_id = response[self._ACCOUNT_ID]
            except JSONDecodeError as e:
                print(e.msg)

        # TODO : Add PyMongo and save this in MongoDB
        self._summoners.append(summoner)

        return summoner

    def __find_summoner(self, summoner_name: str) -> Summoner:
        summoners: list[Summoner] = self._summoners
        for summoner in summoners:
            #  If already summoner saved
            if summoner.summoner_name == summoner_name:
                return summoner

        return Summoner(summoner_name)
