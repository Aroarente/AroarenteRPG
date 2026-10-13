def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import subprocess
import sys
try:
    import pygame
except:
    install("pygame")
    import pygame
import settings
import save

class Pets:
    def __init__(self, name, eqquiped, description, rarity):
        self.name = name
        self.eqquiped = eqquiped
        self.description = description
        self.rarity = rarity

eqquiped_pet = ""
class Dog(Pets):
    data = save.load_game()
    last_save = data["variables"]["last_save"]
    if last_save not in data["saves"]:
        last_save = "save1"
    save_data = data["saves"][last_save]
    eqquiped_gun = save_data["current_pet"]

    def __init__(self):
        super().__init__(
            name="Dog",
            eqquiped=eqquiped_pet == "Dog",
            description="Very loyal dog, Gives some buffs.",
            rarity="Common"
        )

    def effect(self, target):
        pass

    def draw(self, screen):
        pass

    def draw_icon(self, screen):
        pass