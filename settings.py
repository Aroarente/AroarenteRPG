#IMPORTOWANIE

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import subprocess
import sys
try:
    import pygame
except:
    install("pygame")
    import pygame
import ctypes

#IMPORTOWANIE - BRANIE WIDTH/HEIGHT

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

WIDTH = user32.GetSystemMetrics(0)
HEIGHT = user32.GetSystemMetrics(1)
USER_AVERGE = (HEIGHT + WIDTH) // 2

#BRANIE WIDTH/HEIGHT - ZMIENNE

BASE_WIDTH = 2560
BASE_HEIGHT = 1440
BASE_AVERGE = (BASE_HEIGHT + BASE_WIDTH) // 2

FPS = 60

#ZMIENNE - FUNKKCJE

def scale_width(item):
    return round(item * WIDTH / BASE_WIDTH)
def scale_height(item):
    return round(item * HEIGHT / BASE_HEIGHT)
def scale_item(item):
    return round(item * USER_AVERGE / BASE_AVERGE)

#FUNKCJE