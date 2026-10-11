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

class Swords:
    def __init__(self, dmg, rld, rarity, name, eqquiped):
        self.dmg = dmg
        self.rld = rld #ROUNDS
        self.rarity = rarity
        self.name = name
        self.eqquiped = eqquiped

class Katana(Swords):

    def __init__(self):
        super().__init__(
            dmg=5,
            rld=1,
            rarity="Common",
            name="Katana",
            eqquiped=False
        )

    def attack(self, target):
        target.hp -= self.dmg
        if target.hp < target.max_hp:
            target.hp = target.max_hp

    def draw(self, screen, x, y):
        # =========================
        # RĘKOJEŚĆ
        # =========================

        # główna rękojeść
        pygame.draw.rect(
            screen,
            (25, 25, 28),
            (x - 4, y, 8, 28)
        )

        # ozdobne owinięcie
        for i in range(2, 27, 6):
            pygame.draw.line(
                screen,
                (180, 180, 180),
                (x - 4, y + i),
                (x + 4, y + i + 4),
                2
            )

        # końcówka rękojeści
        pygame.draw.circle(
            screen,
            (210, 170, 60),
            (x, y + 29),
            4
        )

        # =========================
        # JELEC
        # =========================

        pygame.draw.line(
            screen,
            (220, 180, 65),
            (x - 10, y),
            (x + 10, y),
            4
        )

        pygame.draw.circle(
            screen,
            (245, 205, 80),
            (x, y),
            3
        )

        # =========================
        # OSTRZE
        # =========================

        pygame.draw.polygon(
            screen,
            (210, 215, 220),
            [
                (x - 4, y),
                (x + 4, y),
                (x + 6, y - 75),
                (x, y - 92),
                (x - 6, y - 75)
            ]
        )

        # ciemniejsza krawędź
        pygame.draw.line(
            screen,
            (120, 125, 130),
            (x + 4, y - 3),
            (x + 6, y - 75),
            2
        )

        # połysk
        pygame.draw.line(
            screen,
            (250, 250, 250),
            (x - 2, y - 8),
            (x - 3, y - 65),
            2
        )