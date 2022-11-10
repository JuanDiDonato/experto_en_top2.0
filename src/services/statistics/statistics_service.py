# -*- coding: utf-8 -*-
import logging

from src.interface.statistics_interface import StatisticsServiceInterface

# Logging level config
from src.model.summoner import Summoner

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class StatisticService:

    """
    Class to implement pattern Strategy
    """

    def __init__(self, service: StatisticsServiceInterface) -> None:
        self.__service: StatisticsServiceInterface = service

    @property
    def service(self) -> StatisticsServiceInterface:
        return self.__service

    @service.setter
    def service(self, service: StatisticsServiceInterface) -> None:
        self.__service = service

    def find_summoner_statistics(self, discord_id: str) -> Summoner:
        logging.info(f"Getting statistics from {self.__service.get_service_name()} service")
        return self.__service.get_statistics(discord_id)
