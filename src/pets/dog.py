from src.pets.base import VirtualPet
from assets.dog.dog_assets import dog_gifs

class DogPet(VirtualPet):
    def __init__(self, name):
        super().__init__(name)
        self.img_url = "https://tinyurl.com/5bzy4jwm"  

    def get_action_gif(self, action):
        return dog_gifs[action]