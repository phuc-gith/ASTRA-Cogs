from .astra_member import AstraMember

async def setup(bot):
    await bot.add_cog(AstraMember(bot))