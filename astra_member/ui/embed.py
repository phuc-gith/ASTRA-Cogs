import discord


def build_welcome_embed(member: discord.Member) -> discord.Embed:
    embed = discord.Embed(
        title="👋 Welcome!",
        description=f"Chào mừng {member.mention} đến với **{member.guild.name}**!",
        color=discord.Color.green(),
    )

    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=f"User ID: {member.id}")

    return embed