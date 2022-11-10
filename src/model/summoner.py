# -*- coding: utf-8 -*-
from .lol_statistics import LolStatistics
from .tft_statistics import TftStatistics


class Summoner:

    """
    Model of summoner
    """

    # Constructor
    def __init__(self, summoner_name: str) -> None:
        self.__discord_id: str = ""
        self.__summoner_name: str = summoner_name
        self.__puu_id: str = ""
        self.__account_id: str = ""
        self.__lol_statistics: LolStatistics
        self.__tft_statistics: TftStatistics

    # Getters
    @property
    def discord_id(self) -> str:
        return self.__discord_id

    @property
    def summoner_name(self) -> str:
        return self.__summoner_name

    @property
    def puu_id(self) -> str:
        return self.__puu_id

    @property
    def account_id(self) -> str:
        return self.__account_id

    @property
    def lol_statistics(self) -> LolStatistics:
        return self.__lol_statistics

    @property
    def tft_statistics(self) -> TftStatistics:
        return self.__tft_statistics

    # Setters
    @discord_id.setter
    def discord_id(self, discord_id: str) -> None:
        self.__discord_id = discord_id

    @puu_id.setter
    def puu_id(self, puu_id: str) -> None:
        self.__puu_id = puu_id

    @account_id.setter
    def account_id(self, account_id: str) -> None:
        self.__account_id = account_id

    @lol_statistics.setter
    def lol_statistics(self, lol_statistics: LolStatistics):
        self.__lol_statistics = lol_statistics

    @tft_statistics.setter
    def tft_statistics(self, tft_statistics: TftStatistics) -> None:
        self.__tft_statistics = tft_statistics
