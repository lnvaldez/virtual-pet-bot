from src.pets.base import VirtualPet
from assets.dog.dog_assets import dog_gifs

class DogPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://media.discordapp.net/attachments/1243271483225149500/1243272030548262922/cute-dog-poodle-inspired-in-tamagotchi-design-.png?ex=6652304e&is=6650dece&hm=ff58215d7b7ec9276fb8cb8d9df04a0c9aa544b25cf04642f3cf3e5e353846b3&=&format=webp&quality=lossless&width=390&height=390"  

    def get_action_gif(self, action):
        return dog_gifs[action]