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

class maps:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

class Map3x3y(maps):
    def __init__(self):
        super().__init__(
            position_x=3,
            position_y=3
        )

    def draw(self, screen):
        pass