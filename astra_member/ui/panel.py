import discord


class WelcomeMessageModal(discord.ui.Modal, title="Add Welcome Message"):
    message = discord.ui.TextInput(
        label="Welcome message",
        placeholder="Ví dụ: Xin chào {0.mention}! Chào mừng đến với {1.name} 🌙",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=1500,
    )

    async def on_submit(self, interaction: discord.Interaction):
        bot = interaction.client
        ctx = await bot.get_context(interaction.message)

        command = bot.get_command("welcomeset greeting add")
        if command is None:
            await interaction.response.send_message(
                "Không tìm thấy command `welcomeset greeting add`.",
                ephemeral=True,
            )
            return

        ctx.author = interaction.user
        ctx.guild = interaction.guild
        ctx.channel = interaction.channel

        await command(ctx, message=str(self.message))

        await interaction.response.send_message(
            "Đã thêm welcome message ✅",
            ephemeral=True,
        )


class MemberPanel(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=300)
        self.bot = bot

    @discord.ui.button(label="Add Welcome", emoji="👋", style=discord.ButtonStyle.primary)
    async def add_welcome(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(WelcomeMessageModal())

    @discord.ui.button(label="Show Settings", emoji="📋", style=discord.ButtonStyle.secondary)
    async def show_settings(self, interaction: discord.Interaction, button: discord.ui.Button):
        command = self.bot.get_command("welcomeset settings")
        ctx = await self.bot.get_context(interaction.message)
        ctx.author = interaction.user
        await interaction.response.defer(ephemeral=True)
        await command(ctx)

    @discord.ui.button(label="Test Welcome", emoji="🧪", style=discord.ButtonStyle.success)
    async def test_welcome(self, interaction: discord.Interaction, button: discord.ui.Button):
        command = self.bot.get_command("welcomeset greeting test")
        ctx = await self.bot.get_context(interaction.message)
        ctx.author = interaction.user
        await interaction.response.defer(ephemeral=True)
        await command(ctx)