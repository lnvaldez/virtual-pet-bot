import discord
from src.pets.base import VirtualPet, pet_dict
from src.pets.cat import CatPet
from src.pets.dog import DogPet
from src.pets.penguin import PenguinPet
from src.pets.squirrel import SquirrelPet
from src.pets.fish import FishPet
from src.integration.ollama import generate_response
import asyncio

pet_types = {
    "penguin": PenguinPet,
    "dog": DogPet,
    "cat": CatPet,
    "squirrel": SquirrelPet,
    "fish": FishPet
}

async def create_pet(ctx, name, pet_type):
    user_id = ctx.author.id
    if user_id in pet_dict:
        await ctx.send(f"You already have a pet named {pet_dict[user_id].name}!")
    else:
        pet_class = pet_types.get(pet_type.lower(), VirtualPet)
        pet_dict[user_id] = pet_class(name)
        embed = discord.Embed(
            title=f"{name} is your new {pet_type} pet!",
            description=f"Take good care of {name}.",
            color=discord.Color.blue()
        )
        embed.set_image(url=pet_dict[user_id].img_url)
        embed.set_footer(text=f"Created by {ctx.author.display_name}")
        await ctx.send(f"Virtual {pet_type} pet {name} created for {ctx.author.mention}!", embed=embed)

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
