# -*- coding: utf-8 -*-

class Statistics:

    def __init__(self) -> None:
        self.__matches: list[dict] = []
        self.__wins: dict = {}
        self.__defeat: dict = {}
        self.__played: dict = {}
        self.__win_rate: float = 0

    @property
    def matches(self) -> list[dict]:
        return self.__matches

    @matches.setter
    def matches(self, matches: list[dict]) -> None:
        self.__matches = matches

    @property
    def wins(self) -> dict:
        return self.__wins

    @wins.setter
    def wins(self, wins: dict):
        self.__wins = wins

    @property
    def defeat(self) -> dict:
        return self.__defeat

    @defeat.setter
    def defeat(self, defeat: dict):
        self.__defeat = defeat

    @property
    def played(self) -> dict:
        return self.__played

    @played.setter
    def played(self, played: dict):
        self.__played = played

    @property
    def win_rate(self):
        return self.__win_rate

    @win_rate.setter
    def win_rate(self, win_rate: float):
        self.__win_rate = win_rate


