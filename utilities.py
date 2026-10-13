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

class Utilities:
    def __init__(self, name, eqquiped, description, rarity):
        self.name = name
        self.eqquiped = eqquiped
        self.description = description
        self.rarity = rarity

eqquiped_utility = ""
class Health_Potion(Utilities):
    data = save.load_game()
    last_save = data["variables"]["last_save"]
    if last_save not in data["saves"]:
        last_save = "save1"
    save_data = data["saves"][last_save]
    eqquiped_utility = save_data["current_sword"]

    def __init__(self):
        super().__init__(
            name="Health Potion",
            eqquiped=eqquiped_utility == "Health Potion",
            description="Classic health potion that heals 20hp.",
            rarity="Common"
        )

    def effect(self, target):
        target.hp += 20
        if target.hp >= target.max_hp:
            target.hp = target.max_hp

    def draw(self, screen):
        pass

    def draw_icon(self, screen):
        pass