# -*- coding: utf-8 -*-

# This file is an entrypoint to discord bot. Here are defined all commands of the bot.

import discord
from discord.ext import commands

from src.services.statistics_service import StatisticsService
from src.model.summoner import Summoner
from src.services.embed_service import EmbedService

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
async def statistics(ctx, discord_id: str) -> None:

    """
    :param discord_id: id of user in discord channel
    :param ctx: Discord channel context
    :return: Statistics in League of Legends of all channel members
    """

    statistics_service: StatisticsService = StatisticsService()

    if discord_id is not None or discord_id != "":
        summoner: Summoner = statistics_service.get_statistics(discord_id)
        await embed_service.send_statistics(ctx, summoner)


if __name__ == "__main__":
    bot.run("INSERT TOKEN HERE")
