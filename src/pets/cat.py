from src.pets.base import VirtualPet
from assets.cat.cat_assets import cat_gifs

class CatPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://media.discordapp.net/attachments/1243271483225149500/1243272029143040163/cute-cat-inspired-in-tamagotchi-design-.png?ex=6652304e&is=6650dece&hm=b4f1724ddef3e88bf6374413b2799f112e458816cc9b5c231b144cfc29640123&=&format=webp&quality=lossless&width=388&height=388"

    def get_action_gif(self, action):
        return cat_gifs[action]