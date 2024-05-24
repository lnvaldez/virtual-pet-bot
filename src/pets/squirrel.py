from src.pets.base import VirtualPet
from assets.squirrel.squirrel_assets import squirrel_gifs

class SquirrelPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://tinyurl.com/6rfp3thk"

    def get_action_gif(self, action):
        return squirrel_gifs[action]