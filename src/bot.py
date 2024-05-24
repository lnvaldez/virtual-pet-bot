import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
from src.response import create_pet
from src.pets.base import VirtualPet, pet_dict
from src.ui.bot_page import BotPage

# Cargar la variable del ambiente desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Setup bot
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command(name='info')
async def info(ctx):
    user_id = ctx.author.id
    if user_id not in pet_dict:
        await ctx.send("You don't have a pet yet! Create one with `!create_pet [name] [type]`")
        return

    pet = pet_dict[user_id]
    embed = discord.Embed(
        title=f"{pet.name}'s Status",
        description="Here is the current status of your pet:",
        color=discord.Color.gold()
    )
    embed.set_author(name="Virtual Pets!", icon_url='https://acortar.link/oAnMvm')
    embed.set_thumbnail(url=pet.img_url)

    # Añadir campos con colores para hunger, happiness, y energy
    embed.add_field(name="Hunger", value=pet.get_hunger_colors(pet.hunger), inline=True)
    embed.add_field(name="Happiness", value=pet.get_color_coded_value(pet.happiness), inline=True)
    embed.add_field(name="Energy", value=pet.get_color_coded_value(pet.energy), inline=True)

    embed.set_footer(text="Hunger - Energy - Happiness")

    view = BotPage(pet)
    await ctx.send(embed=embed, view=view)

@client.command(name='create_pet')
async def create_pet_command(ctx, name: str, pet_type: str):
    await create_pet(ctx, name, pet_type)

def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()
