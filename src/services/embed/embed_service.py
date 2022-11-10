# -*- coding: utf-8 -*-
from discord.ext.commands import Context

from src.interface.embed_interface import EmbedBuilderInterface
from src.model.summoner import Summoner
from src.utils.embed.games.league_of_legends.embed_lol_statistics_builder import EmbedLolStatisticsBuilder
from src.utils.embed.games.team_fight_tactics.embed_tft_statistics_builder import EmbedTftStatisticsBuilder


class EmbedService:

    """
    Send messages to discord channel
    """

    __embed_builder: EmbedBuilderInterface

    async def send_lol_statistics(self, ctx: Context, summoner: Summoner):

        """
        Show statistics of summoner
        :param ctx: Discord context
        :param summoner: Summoner to show statistics
        """
        self.__embed_builder = EmbedLolStatisticsBuilder()

        title: str = "Statistics"
        description: str = f"Statistics of the last 3 days of " \
                           f"{summoner.summoner_name}"

        await self.__embed_builder.create_embed(title, description).with_statistics(summoner.lol_statistics) \
            .send_embed(ctx=ctx)

    async def send_tft_statistics(self, ctx: Context, summoner: Summoner):

        self.__embed_builder = EmbedTftStatisticsBuilder()

        title: str = "Estadisticas de TFT"
        description: str = f"Estadisticas de la ultima semana de " \
                           f"{summoner.summoner_name}"

        await self.__embed_builder.create_embed(title, description).with_statistics(summoner.tft_statistics) \
            .send_embed(ctx=ctx)

