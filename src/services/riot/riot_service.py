# -*- coding: utf-8 -*-
from src.interface.riot_interface import RiotInterface
from src.model.summoner import Summoner


class RiotService:

    """
    Class to implement pattern Strategy
    """

    def __init__(self, service: RiotInterface):
        self.__service: RiotInterface = service

    @property
    def service(self) -> RiotInterface:
        return self.__service

    @service.setter
    def service(self, service: RiotInterface) -> None:
        self.__service = service

    def get_summoner_data(self, summoner_name: str) -> Summoner:
        return self.__service.find_statistics(summoner_name)
