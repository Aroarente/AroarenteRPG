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

class Utilities:
    def __init__(self, name, eqquiped):
        self.name = name
        self.eqquiped = eqquiped

class Health_Potion(Utilities):
    def __init__(self):
        super().__init__(
            name="Health Potion",
            eqquiped=False
        )

    def effect(self):
        pass

    def draw(self, screen):
        pass

    def draw_icon(self, screen):
        pass