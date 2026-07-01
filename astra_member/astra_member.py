from redbot.core import commands
from .utils.template import render_template

class AstraMember(commands.Cog):
    """ASTRA member management."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def astrahello(self, ctx):
        """Test ASTRA cog."""
        await ctx.send("ASTRA Member cog đã hoạt động 🐾")
@commands.command()
    async def renderdemo(self, ctx, *, text: str):
        """Test ASTRA template renderer."""
        result = render_template(text, ctx.author)
        await ctx.send(result)