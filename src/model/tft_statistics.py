# -*- coding: utf-8 -*-

class TftStatistics:

    """
    Model of Team Fight Tactics statistics
    """

    def __init__(self) -> None:
        self.__matches: list[dict] = []
        self.__placements: list[int] = []
        self.__levels: list[int] = []
        self.__rounds: list[int] = []
        self.__traits: dict = {}

    # Getters
    @property
    def matches(self) -> list[dict]:
        return self.__matches

    @property
    def levels(self) -> list[int]:
        return self.__levels

    @property
    def placements(self) -> list[int]:
        return self.__placements

    @property
    def rounds(self) -> list[int]:
        return self.__rounds

    @property
    def traits(self) -> dict:
        return self.__traits

    # Setter
    @matches.setter
    def matches(self, matches: list[dict]) -> None:
        self.__matches = matches

    @levels.setter
    def levels(self, levels: list[int]) -> None:
        self.__levels = levels

    @rounds.setter
    def rounds(self, rounds: list[int]) -> None:
        self.__rounds = rounds

    @placements.setter
    def placements(self, placements: list[int]) -> None:
        self.__placements = placements

    @traits.setter
    def traits(self, traits: dict) -> None:
        self.__traits = traits
