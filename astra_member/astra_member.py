from redbot.core import commands


class AstraMember(commands.Cog):
    """ASTRA member management."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def astrahello(self, ctx):
        """Test ASTRA cog."""
        await ctx.send("ASTRA Member cog đã hoạt động 🐾")