import random 
import discord

# Crear clase VirtualPet, de la cual heredan todos los pets

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(20, 60)
        self.happiness = random.randint(1, 50)
        self.energy = random.randint(1, 50)
        self.img_url = "https://example.com/default_pet_image.png"  

    # Recibir un valor de color en base al valor happiness o energy

    def get_color_coded_value(self, value):
        if value < 30:
            color = '🔴'
        elif 30 <= value < 70:
            color = '🟡'
        else:
            color = '🟢'
        return f"{color} {value}"
    
    # Recibir un valor de color para hunger
    # Es diferente ya que el hambre del pet deberia disminuir, no aumentar

    def get_hunger_colors(self, value):
        if value < 30:
            color = '🟢'
        elif 30 <= value < 70:
            color = '🟡'
        else:
            color = '🔴'
        return f"{color} {value}"
    
    # Funciones para alimentar, jugar, dormir, y checkear el estado de la mascota
    # update_status() actualiza todas las funciones

    async def feed(self, interaction):
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(100, self.happiness + 5)
        self.energy = min(100, self.energy + 5)
        await self.update_status(interaction, "fed", discord.Color.green(), self.get_action_gif("feed"))

    async def play(self, interaction):
        self.hunger = min(100, self.hunger + 5)
        self.happiness = min(100, self.happiness + 10)
        self.energy = max(0, self.energy - 10)
        await self.update_status(interaction, "had a great time playing", discord.Color.blue(), self.get_action_gif("play"))

    async def sleep(self, interaction):
        self.hunger = min(100, self.hunger + 5)
        self.happiness = max(0, self.happiness - 5)
        self.energy = min(100, self.energy + 15)
        await self.update_status(interaction, "is well-rested now", discord.Color.purple(), self.get_action_gif("sleep"))

    async def check_status(self, interaction):
        total = (self.happiness + self.energy) - self.hunger

        if total < 50:
            status_message = f"{self.name} needs more attention!"
        elif total < 100:
            status_message = f"{self.name} is doing okay, but could use some more care."
        else:
            status_message = f"{self.name} is in great shape!"

        await interaction.response.send_message(status_message, ephemeral=True)

    async def update_status(self, interaction, action, color, img_url):
        embed = discord.Embed(
            title=f"{self.name} {action}!",
            description=f"Hunger: {self.get_hunger_colors(self.hunger)}\nHappiness: {self.get_color_coded_value(self.happiness)}\nEnergy: {self.get_color_coded_value(self.energy)}",
            color=color
        )
        embed.set_image(url=img_url)
        embed.set_footer(text="Your pet is glad you interacted with them!")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    def get_action_gif(self, action):
        return "https://example.com/default_action.gif"  
    
pet_dict = {}
