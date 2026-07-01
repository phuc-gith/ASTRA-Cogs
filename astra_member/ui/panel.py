import discord


class MemberPanel(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=180)
        self.bot = bot

    @discord.ui.button(label="Test Welcome", emoji="👋", style=discord.ButtonStyle.primary)
    async def test_welcome(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Chạy lệnh này để test welcome:\n```!welcomeset greeting test```",
            ephemeral=True,
        )

    @discord.ui.button(label="Show Settings", emoji="📋", style=discord.ButtonStyle.secondary)
    async def show_settings(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Chạy lệnh này để xem cấu hình welcome:\n```!welcomeset settings```",
            ephemeral=True,
        )

    @discord.ui.button(label="Help Welcome", emoji="🛠", style=discord.ButtonStyle.secondary)
    async def help_welcome(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Các lệnh quan trọng:\n"
            "```text\n"
            "!welcomeset greeting channel #welcome\n"
            "!welcomeset greeting toggle\n"
            "!welcomeset greeting test\n"
            "!welcomeset embed toggle\n"
            "!welcomeset embed colour #A855F7\n"
            "!welcomeset goodbye channel #goodbye\n"
            "!welcomeset goodbye toggle\n"
            "```",
            ephemeral=True,
        )