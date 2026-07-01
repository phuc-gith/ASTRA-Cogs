from redbot.core import commands

from .commands.general import GeneralCommands


class AstraMember(commands.Cog, GeneralCommands):
    """ASTRA member management."""

    def __init__(self, bot):
        self.bot = bot