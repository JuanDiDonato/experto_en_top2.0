# -*- coding: utf-8 -*-
from discord.ext.commands import Context

from ..model.summoner import Summoner
from ..utils.embed_statistics_builder import EmbedStatisticsBuilder


class EmbedService:

    """
    Send messages to discord channel
    """

    def __init__(self) -> None:
        self.__embed_builder: EmbedStatisticsBuilder = EmbedStatisticsBuilder()

    async def send_statistics(self, ctx: Context, summoner: Summoner):

        """
        Show statistics of summoner
        :param ctx: Discord context
        :param summoner: Summoner to show statistics
        """

        title: str = "Statistics"
        description: str = f"Statistics of the last 3 days of " \
                           f"{summoner.summoner_name}"

        await self.__embed_builder.create_embed(title, description).with_statistics(summoner.statistics) \
            .send_embed(ctx=ctx)
