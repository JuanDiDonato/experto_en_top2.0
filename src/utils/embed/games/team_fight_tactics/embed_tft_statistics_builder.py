# -*- coding: utf-8 -*-
import logging
import math

from src.model.tft_statistics import TftStatistics
from src.utils.embed.embed_builder import EmbedBuilder

# Logging level config
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class EmbedTftStatisticsBuilder(EmbedBuilder):
    __tft_statistics: TftStatistics

    def __init__(self) -> None:
        super().__init__()
        self.__TFT7b: str = "TFT7b_"
        self.__TFT7: str = "TFT7_"
        self.__SET7: str = "Set7_"

    def with_statistics(self, statistics: TftStatistics) -> EmbedBuilder:
        self.__tft_statistics = statistics
        self.__process_statistics()
        return self

    def __process_statistics(self):
        logging.info("Setting summoner statistics")
        levels: list[int] = self.__tft_statistics.levels
        placements: list[int] = self.__tft_statistics.placements
        rounds: list[int] = self.__tft_statistics.rounds

        if len(levels) == 0 and len(placements) == 0 and len(rounds) == 0:
            self.with_field(name="Oh no!", value="No hay estadisticas disponibles")
        else:
            self.__set_average(levels, "nivel")
            self.__set_average(placements, "poscicion final")
            self.__set_average(rounds, "rondas jugadas")
            self.__set_traits()

    def __set_average(self, values: list[int], field: str):

        if len(values) > 0:
            total: int = 0
            for value in values:
                total = total + value

            average: int = math.trunc(total / len(values))
            self.with_field(name=f"Promedio de {field}", value=str(average))

    def __set_traits(self):
        traits: dict = self.__tft_statistics.traits
        if len(traits) > 0:
            for k, v in traits.items():
                if len(v) > 0:
                    value: str = " "
                    for trait in v:
                        trait = trait.replace(self.__SET7, "")
                        value = value + trait + "\n"

                    if k == "wins":
                        self.with_field(name=f"En top 4 con:", value=value)
                    else:
                        self.with_field(name=f"Muy lejos de los puntos con:", value=value)
