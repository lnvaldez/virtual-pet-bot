from src.pets.base import VirtualPet
from assets.penguin.penguin_assets import penguin_gifs

class PenguinPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://media.discordapp.net/attachments/1243271483225149500/1243272029419995157/penguin-inspired-in-tamagotchi-design-.png?ex=6652304e&is=6650dece&hm=34deee839db068ef34c61c378021cb1e7aba0c1158c4a4a4190b51df004fc5ce&=&format=webp&quality=lossless&width=388&height=388" 

    def get_action_gif(self, action):
        return penguin_gifs[action]