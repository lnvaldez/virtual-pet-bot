from src.pets.base import VirtualPet
from assets.squirrel.squirrel_assets import squirrel_gifs

class SquirrelPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://media.discordapp.net/attachments/1243271483225149500/1243272029671784528/squirrel-inspired-in-tamagotchi-design-.png?ex=6652304e&is=6650dece&hm=ffe54da89d6dc5dba62436ef589276a4000d214f0e2316e518503540b1522fca&=&format=webp&quality=lossless&width=388&height=388"

    def get_action_gif(self, action):
        return squirrel_gifs[action]