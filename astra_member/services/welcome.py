import discord

from ..ui.embed import build_welcome_embed


class WelcomeService:
    def __init__(self, bot):
        self.bot = bot

    async def send(self, member: discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")

        if channel is None:
            return

        embed = build_welcome_embed(member)
        await channel.send(embed=embed)