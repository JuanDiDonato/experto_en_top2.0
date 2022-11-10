# -*- coding: utf-8 -*-

# This file is an entrypoint to discord bot. Here are defined all commands of the bot.

import discord
from discord.ext import commands

from src.services.statistics.games.league_of_legends.lol_statistics_service import LolStatisticsService
from src.services.statistics.statistics_service import StatisticService
from src.model.summoner import Summoner
from src.services.embed.embed_service import EmbedService
from src.services.statistics.games.team_fight_tactics.tft_statistics_service import TftStatisticsService

bot = commands.Bot(command_prefix="!")  # Commands prefix
embed_service: EmbedService = EmbedService()


@bot.event
async def on_ready():
    """
    When bot is coming up
    """

    await bot.change_presence(activity=discord.Game(name="Hi! Insert here a message!"))
    print("Bot connected")


@bot.command()
async def lol(ctx, discord_id: str) -> None:
    """
    :param discord_id: id of user in discord channel
    :param ctx: Discord channel context
    """

    statistics_service: StatisticService = StatisticService(LolStatisticsService())

    if discord_id is not None or discord_id != "":
        summoner: Summoner = statistics_service.find_summoner_statistics(discord_id)
        await embed_service.send_lol_statistics(ctx, summoner)


@bot.command()
async def tft(ctx, discord_id: str) -> None:
    """
    :param discord_id: id of user in discord channel
    :param ctx: Discord channel context
    """
    statistics_service: StatisticService = StatisticService(TftStatisticsService())

    if discord_id is not None or discord_id != "":
        summoner: Summoner = statistics_service.find_summoner_statistics(discord_id)
        await embed_service.send_tft_statistics(ctx, summoner)


if __name__ == "__main__":
    bot.run("DISCORD TOKEN HERE!")
