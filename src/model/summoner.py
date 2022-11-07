# -*- coding: utf-8 -*-
from .statistics import Statistics

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
        self.__statistics: Statistics

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
    def statistics(self) -> Statistics:
        return self.__statistics

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

    @statistics.setter
    def statistics(self, statistics: Statistics):
        self.__statistics = statistics





