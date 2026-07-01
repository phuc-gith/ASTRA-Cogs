import discord


def render_template(text: str | None, member: discord.Member) -> str | None:
    if text is None:
        return None

    guild = member.guild

    placeholders = {
        "{user}": member.mention,
        "{user_name}": member.name,
        "{user_display}": member.display_name,
        "{user_id}": str(member.id),
        "{user_avatar}": member.display_avatar.url,
        "{server}": guild.name,
        "{server_id}": str(guild.id),
        "{member_count}": str(guild.member_count or 0),
        "{server_icon}": guild.icon.url if guild.icon else "",
    }

    result = text

    for key, value in placeholders.items():
        result = result.replace(key, value)

    return result