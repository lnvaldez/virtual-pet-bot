from src.pets.base import VirtualPet
from assets.cat.cat_assets import cat_gifs

class CatPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://tinyurl.com/4dtzt8xn"

    def get_action_gif(self, action):
        return cat_gifs[action]