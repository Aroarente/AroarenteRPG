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

class Down_Armours:
    def __init__(self, name, eqquiped, rarity, description, dmg_reduction):
        self.name = name
        self.eqquiped = eqquiped
        self.rarity = rarity
        self.description = description
        self.dmg_reduction = dmg_reduction
        self.part = "Down"

class Up_Armours:
    def __init__(self, name, eqquiped, rarity, description, dmg_reduction):
        self.name = name
        self.eqquiped = eqquiped
        self.rarity = rarity
        self.description = description
        self.dmg_reduction = dmg_reduction # %
        self.part = "Up"

eqquiped_down_armour = ""
eqquiped_up_armour = ""
class Iron_Chestplate(Up_Armours):
    data = save.load_game()
    last_save = data["variables"]["last_save"]
    if last_save not in data["saves"]:
        last_save = "save1"
    save_data = data["saves"][last_save]
    eqquiped_down_armour = save_data["current_down_armor"]
    eqquiped_up_armour = save_data["current_up_armor"]

    def __init__(self):
        super().__init__(
            name="Iron Chestplate",
            eqquiped=eqquiped_up_armour == "Iron Chestplate",
            rarity="Common",
            description="Classic iron chestplate that reduce some damage.",
            dmg_reduction=10
        )

    def dmg_reduction(self, target):
        pass

    def draw(self, screen):
        pass

    def draw_icon(self, screen):
        pass