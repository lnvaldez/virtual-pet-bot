from src.pets.base import VirtualPet
from assets.penguin.penguin_assets import penguin_gifs

class PenguinPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://tinyurl.com/yp9bvyhc" 

    def get_action_gif(self, action):
        return penguin_gifs[action]