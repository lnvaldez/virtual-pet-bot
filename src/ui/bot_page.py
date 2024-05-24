import discord 
from src.integration.ollama import generate_response
import asyncio

class BotPage(discord.ui.View):
    def __init__(self, pet):
        super().__init__()
        self.pet = pet

    @discord.ui.button(label="Talk", style=discord.ButtonStyle.primary)
    async def say_hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("What would you like to talk about?", ephemeral=True)

        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            user_message = await interaction.client.wait_for('message', check=check, timeout=60)
            user_input = user_message.content
            response = generate_response(user_input)
            await interaction.followup.send(response)
        except asyncio.TimeoutError:
            await interaction.followup.send("Sorry, you took too long to respond.")

    @discord.ui.button(label='Feed', style=discord.ButtonStyle.primary)
    async def feed_pet(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.pet.feed(interaction)

    @discord.ui.button(label='Play', style=discord.ButtonStyle.primary)
    async def play_with_pet(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.pet.play(interaction)

    @discord.ui.button(label='Sleep', style=discord.ButtonStyle.primary)
    async def put_pet_to_sleep(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.pet.sleep(interaction)

    @discord.ui.button(label='Status', style=discord.ButtonStyle.primary)
    async def check_pet_status(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.pet.check_status(interaction)
