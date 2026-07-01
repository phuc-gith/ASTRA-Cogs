from redbot.core import commands
import discord

from ..utils.template import render_template
from ..ui.panel import MemberPanel


class GeneralCommands:
    @commands.command()
    async def astrahello(self, ctx):
        """Test ASTRA cog."""
        await ctx.send("ASTRA Member cog đã hoạt động 🐾")

    @commands.command()
    async def renderdemo(self, ctx, *, text: str):
        """Test ASTRA template renderer."""
        result = render_template(text, ctx.author)
        await ctx.send(result)
    @commands.group(name="amember")
    async def amember(self, ctx):
        """ASTRA member management commands."""
        pass

    @amember.command(name="panel")
    async def amember_panel(self, ctx):
        """Open ASTRA member control panel."""
        embed = discord.Embed(
            title="🐾 ASTRA Member Panel",
            description="Bảng điều khiển nhanh cho Welcome / Goodbye.",
            color=discord.Color.purple(),
        )

        await ctx.send(embed=embed, view=MemberPanel(self.bot))