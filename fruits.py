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

class Fruits:
    def __init__(self, name, s1_energy_drain, s2_energy_drain, s3_energy_drain, s1_name, s2_name, s3_name, s1_dmg, s2_dmg, s3_dmg, s1_mas, s2_mas, s3_mas, eqquiped, rarity):
        self.name = name
        self.eqquiped = eqquiped
        self.rarity = rarity

        self.s1_energy_drain = s1_energy_drain
        self.s2_energy_drain = s2_energy_drain
        self.s3_energy_drain = s3_energy_drain

        self.s1_name = s1_name
        self.s2_name = s2_name
        self.s3_name = s3_name

        self.s1_dmg = s1_dmg
        self.s2_dmg = s2_dmg
        self.s3_dmg = s3_dmg

        self.s1_mas = s1_mas
        self.s2_mas = s2_mas
        self.s3_mas = s3_mas

eqquiped_fruit = ""
class Blade(Fruits):
    data = save.load_game()
    last_save = data["variables"]["last_save"]
    if last_save not in data["saves"]:
        last_save = "save1"
    save_data = data["saves"][last_save]
    eqquiped_fruit = save_data["current_fruit"]

    def __init__(self):
        super().__init__(
            name="Blade",
            eqquiped=eqquiped_fruit == "Blade",
            rarity="Common",
            s1_energy_drain=10, #ZMIEŃ <
            s2_energy_drain=20,
            s3_energy_drain=30, #ZMIEŃ >
            s1_name="Huge Slash",
            s2_name="Rapid Slashes",
            s3_name="Ultimate Slash",
            s1_dmg=10,          #ZMIEŃ <
            s2_dmg=20,
            s3_dmg=30,
            s1_mas=1,
            s2_mas=10,
            s3_mas=20           #ZMIEŃ >
        )

    def attack(self, target, player, s):
        if s == 1:
            dmg = self.s1_dmg
            energy_drain = self.s1_energy_drain
        elif s == 2:
            dmg = self.s2_dmg
            energy_drain = self.s2_energy_drain
        elif s == 3:
            dmg = self.s3_dmg
            energy_drain = self.s3_energy_drain
        else:
            dmg = self.s1_dmg
            energy_drain = self.s1_energy_drain

        # Zabierz energię
        player.energy -= energy_drain

        # Zadaj obrażenia
        target.hp -= dmg
        if target.hp < target.max_hp:
            target.hp = target.max_hp

    def draw_icon(self, screen):
        pass

    def draw_s1_icon(self, screen):
        pass

    def draw_s2_icon(self, screen):
        pass

    def draw_s3_icon(self, screen):
        pass

    def draw_s1(self, screen):
        pass

    def draw_s2(self, screen):
        pass

    def draw_s3(self, screen):
        pass