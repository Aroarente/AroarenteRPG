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

class Swords:
    def __init__(self, dmg, rld, rarity, name, eqquiped, description):
        self.dmg = dmg
        self.rld = rld #ROUNDS
        self.rarity = rarity
        self.name = name
        self.description = description
        self.eqquiped = eqquiped

eqquiped_sword = ""
class Katana(Swords):

    data = save.load_game()
    last_save = data["variables"]["last_save"]
    if last_save not in data["saves"]:
        last_save = "save1"
    save_data = data["saves"][last_save]
    eqquiped_sword = save_data["current_sword"]

    def __init__(self):
        super().__init__(
            dmg=10,
            rld=1,
            rarity="Common",
            name="Katana",
            description="Classic sword. Good for beginners.",
            eqquiped=eqquiped_sword == "Katana"
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

    def draw_icon(self, screen, center_x, center_y):
        # Slot rysowany tutaj, a nie w ui.py.
        slot_size = 124
        slot = pygame.Rect(
            int(center_x - slot_size // 2),
            int(center_y - slot_size // 2),
            slot_size,
            slot_size
        )

        pygame.draw.rect(screen, (57, 32, 19), slot.move(3, 4), border_radius=8)
        pygame.draw.rect(screen, (111, 66, 37), slot, border_radius=8)
        pygame.draw.rect(screen, (54, 31, 19), slot, width=3, border_radius=8)
        pygame.draw.line(
            screen, (168, 117, 73),
            (slot.x + 8, slot.y + 4), (slot.right - 8, slot.y + 4), 2
        )

        # Katana dopasowana do większego slotu 124x124.
        cx = int(center_x)
        cy = int(center_y + 24)

        # Cień i ostrze
        pygame.draw.polygon(screen, (65, 66, 72), [
            (cx - 3, cy - 1), (cx + 3, cy - 1),
            (cx + 8, cy - 60), (cx, cy - 70), (cx - 8, cy - 60)
        ])
        pygame.draw.polygon(screen, (210, 215, 220), [
            (cx - 2, cy - 2), (cx + 2, cy - 2),
            (cx + 7, cy - 59), (cx, cy - 68), (cx - 7, cy - 59)
        ])
        pygame.draw.line(screen, (250, 250, 250), (cx - 1, cy - 9), (cx - 2, cy - 54), 1)
        pygame.draw.line(screen, (120, 125, 130), (cx + 2, cy - 4), (cx + 5, cy - 57), 1)

        # Jelec
        pygame.draw.line(screen, (220, 180, 65), (cx - 10, cy), (cx + 10, cy), 3)
        pygame.draw.circle(screen, (245, 205, 80), (cx, cy), 2)

        # Rękojeść
        pygame.draw.rect(screen, (25, 25, 28), (cx - 3, cy + 2, 6, 14), border_radius=1)
        for i in range(4, 15, 5):
            pygame.draw.line(screen, (180, 180, 180),
                             (cx - 3, cy + i), (cx + 3, cy + i + 2), 1)
        pygame.draw.circle(screen, (210, 170, 60), (cx, cy + 19), 2)