from src.pets.base import VirtualPet
from assets.fish.fish_assets import fish_gifs

class FishPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = 'https://media.discordapp.net/attachments/1243271483225149500/1243272030258725026/gold-fish-inspired-in-tamagotchi-design-.png?ex=6650dece&is=664f8d4e&hm=3e93f61a907d3a5872aeb2945b915c8e82cf7d289dea6acf6d3a887299391e0d&=&format=webp&quality=lossless&width=390&height=390'

    def get_action_gif(self, action):
        return fish_gifs[action]