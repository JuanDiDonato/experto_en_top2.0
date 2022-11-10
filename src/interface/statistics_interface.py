# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

from src.model.summoner import Summoner


class StatisticsServiceInterface(ABC):
    _summoners = {  # TODO: Save in database
        "<@411704033225605130>": "D1D0",
        "<@602993773940572220>": "KARTTA",
        "<@748722234931282020>": "P4RF3CTO",
        "<@258683657038856193>": "Nezah",
        "<@583500343426547712>": "elioelmufa",
        "<@544348597991243786>": "MaitoChoy",
        "<@712826508229476382>": "Behamoth",
        "<@515334245166743574>": "BALANCE iRELIA",
    }
    _service_name: str

    @abstractmethod
    def get_statistics(self, discord_id: str) -> Summoner:
        pass

    @abstractmethod
    def get_service_name(self) -> str:
        return self._service_name
