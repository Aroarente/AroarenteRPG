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
import settings
import player
import save
import math
import swords
import guns
import ui
import fruits

def format_number(n):
    if n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
        if n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} TQC"
        elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} BQC"
        elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} MQC"
        elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} KQC"
        else:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} QC"
    elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} C"
    elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000:.1f} QD"
    elif n >= 1_000_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000:.1f} D"
    elif n >= 1_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000:.1f} QN"
    elif n >= 1_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000:.1f} N"
    elif n >= 1_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000:.1f} O"
    elif n >= 1_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000:.1f} QS"
    elif n >= 1_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000:.1f} S"
    elif n >= 1_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000:.1f} Q"
    elif n >= 1_000_000_000_000:
        return f"{n/1_000_000_000_000:.1f} T"
    elif n >= 1_000_000_000:
        return f"{n/1_000_000_000:.1f} B"
    elif n >= 1_000_000:
        return f"{n/1_000_000:.1f} M"
    elif n >= 1_000:
        return f"{n/1_000:.1f} K"
    else:
        return str(n)

#IMPORTOWANIE - GUI

pygame.init()
clock = pygame.time.Clock()
Player = player.player()
game_ui = ui.UI()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Aroarente RPG : Explore the world")

#GUI - ZMIENNE

running = True
game_state = "menu"
game_menu_state = "menu"
game_game_state = "cutsceene1"
just_entered_settings = False
just_entered_last_save = False
just_entered_load_save = False
dialogue_in_cutsceene1 = False

# =========================================================
# ZMIENNE CUTSCENE 1
# =========================================================

demon_walk_step = 0

npc_1_alive = True
npc_2_alive = True
npc_3_alive = True
npc_4_alive = True

# Zabieranie NPC
demon_taking_npc = False
demon_take_timer = 0

# 1.5 sekundy przy 60 FPS
demon_take_duration = 90

cutscene1_started = False
cutscene1_fade = 255
cutscene1_fade_done = False
cutscene1_wait = 0
cutscene1_wait_done = False
# =========================================================
# FADE KOŃCOWY CUTSCENY
# =========================================================

cutscene1_end_fade = 0
cutscene1_end_fade_done = False

# =========================================================
# FADE PO PRZEJŚCIU DO GRY
# =========================================================

game_fade = 255
game_fade_done = False

#CLASSY - GUI

class textures:
    @staticmethod
    def draw_tree(x, y):
        # Pień
        pygame.draw.rect(
            screen,
            (100, 65, 35),
            (
                (x - 15),
                (y),
                (30),
                (90)
            )
        )
        # Korona
        pygame.draw.circle(
            screen,
            (40, 130, 50),
            (
                (x),
                (y - 30)
            ),
            (50)
        )
        pygame.draw.circle(
            screen,
            (30, 120, 40),
            (
                (x - 40),
                (y)
            ),
            (40)
        )
        pygame.draw.circle(
            screen,
            (50, 145, 55),
            (
                (x + 40),
                (y)
            ),
            (40)
        )
        pygame.draw.circle(
            screen,
            (45, 140, 50),
            (
                (x),
                (y - 60)
            ),
            (45)
        )

    @staticmethod
    def draw_rock(x, y):
        # Lewa część skały
        pygame.draw.polygon(
            screen,
            (90, 90, 90),
            [
                ((x - 65), (y + 10)),
                ((x - 60), (y - 25)),
                ((x - 40), (y - 45)),
                ((x - 10), (y - 35)),
                ((x + 5), (y)),
                ((x - 5), (y + 25)),
                ((x - 45), (y + 30))
            ]
        )

        # Prawa część skały
        pygame.draw.polygon(
            screen,
            (105, 105, 105),
            [
                ((x - 5), (y)),
                ((x + 10), (y - 35)),
                ((x + 40), (y - 45)),
                ((x + 65), (y - 20)),
                ((x + 65), (y + 15)),
                ((x + 45), (y + 30)),
                ((x + 5), (y + 25))
            ]
        )

        # Górna część skały
        pygame.draw.polygon(
            screen,
            (125, 125, 125),
            [
                ((x - 35), (y - 25)),
                ((x - 25), (y - 60)),
                ((x), (y - 75)),
                ((x + 28), (y - 55)),
                ((x + 35), (y - 25)),
                ((x + 15), (y - 5)),
                ((x - 10), (y - 5))
            ]
        )

    @staticmethod
    def draw_stall(x, y, roof_color):
        # Słupki
        pygame.draw.rect(
            screen,
            (100, 65, 35),
            (
                (x - 110),
                (y - 80),
                (20),
                (210)
            )
        )

        pygame.draw.rect(
            screen,
            (100, 65, 35),
            (
                (x + 90),
                (y - 80),
                (20),
                (210)
            )
        )

        # Blat
        pygame.draw.rect(
            screen,
            (130, 80, 40),
            (
                (x - 130),
                (y + 100),
                (260),
                (30)
            )
        )

        # Daszek
        pygame.draw.polygon(
            screen,
            roof_color,
            [
                ((x - 140), (y - 130)),
                ((x + 140), (y - 130)),
                ((x + 115), (y - 80)),
                ((x - 115), (y - 80))
            ]
        )

        # Jasne pasy na daszku
        pygame.draw.polygon(
            screen,
            (230, 190, 100),
            [
                ((x - 80), (y - 130)),
                ((x - 30), (y - 130)),
                ((x - 40), (y - 80)),
                ((x - 90), (y - 80))
            ]
        )

        pygame.draw.polygon(
            screen,
            (230, 190, 100),
            [
                ((x + 30), (y - 130)),
                ((x + 80), (y - 130)),
                ((x + 90), (y - 80)),
                ((x + 40), (y - 80))
            ]
        )

        # LADА
        pygame.draw.rect(
            screen,
            (105, 60, 30),
            (
                (x - 130),
                (y + 90),
                (260),
                (45)
            )
        )

        # Górna część lady
        pygame.draw.rect(
            screen,
            (155, 95, 45),
            (
                (x - 135),
                (y + 82),
                (270),
                (15)
            )
        )

        # ZWISAJĄCE LAMPY

        # Lewa lampa
        pygame.draw.line(
            screen,
            (50, 40, 30),
            ((x - 90), (y - 80)),
            ((x - 90), (y - 35)),
            (4)
        )

        pygame.draw.rect(
            screen,
            (70, 55, 35),
            (
                (x - 105),
                (y - 35),
                (30),
                (35)
            )
        )

        pygame.draw.rect(
            screen,
            (255, 210, 80),
            (
                (x - 100),
                (y - 30),
                (20),
                (25)
            )
        )

        # Prawa lampa
        pygame.draw.line(
            screen,
            (50, 40, 30),
            ((x + 90), (y - 80)),
            ((x + 90), (y - 35)),
            (4)
        )

        pygame.draw.rect(
            screen,
            (70, 55, 35),
            (
                (x + 75),
                (y - 35),
                (30),
                (35)
            )
        )

        pygame.draw.rect(
            screen,
            (255, 210, 80),
            (
                (x + 80),
                (y - 30),
                (20),
                (25)
            )
        )

    @staticmethod
    def draw_npc(x, y, shirt_color):
        # =========================
        # NOGI
        # =========================

        pygame.draw.polygon(
            screen,
            (55, 55, 65),
            [
                ((x - 24), (y + 45)),
                ((x - 2), (y + 45)),
                ((x - 5), (y + 85)),
                ((x - 28), (y + 85))
            ]
        )

        pygame.draw.polygon(
            screen,
            (55, 55, 65),
            [
                ((x + 2), (y + 45)),
                ((x + 24), (y + 45)),
                ((x + 28), (y + 85)),
                ((x + 5), (y + 85))
            ]
        )

        # Buty
        pygame.draw.ellipse(
            screen,
            (35, 30, 25),
            (
                (x - 32),
                (y + 78),
                (30),
                (15)
            )
        )

        pygame.draw.ellipse(
            screen,
            (35, 30, 25),
            (
                (x + 2),
                (y + 78),
                (30),
                (15)
            )
        )

        # =========================
        # TUŁÓW
        # =========================

        pygame.draw.polygon(
            screen,
            shirt_color,
            [
                ((x - 30), (y - 5)),
                ((x + 30), (y - 5)),
                ((x + 27), (y + 50)),
                ((x - 27), (y + 50))
            ]
        )

        # Kołnierz
        pygame.draw.polygon(
            screen,
            (45, 80, 50),
            [
                ((x - 15), (y)),
                ((x), (y + 15)),
                ((x + 15), (y))
            ]
        )

        # Pas
        pygame.draw.rect(
            screen,
            (95, 55, 30),
            (
                (x - 29),
                (y + 37),
                (58),
                (10)
            )
        )

        # Klamra
        pygame.draw.rect(
            screen,
            (190, 155, 65),
            (
                (x - 5),
                (y + 36),
                (10),
                (12)
            )
        )

        # =========================
        # RAMIONA
        # =========================

        pygame.draw.circle(
            screen,
            shirt_color,
            ((x - 30), (y + 5)),
            (16)
        )

        pygame.draw.circle(
            screen,
            shirt_color,
            ((x + 30), (y + 5)),
            (16)
        )

        pygame.draw.line(
            screen,
            shirt_color,
            ((x - 40), (y + 10)),
            ((x - 38), (y + 42)),
            (13)
        )

        pygame.draw.line(
            screen,
            shirt_color,
            ((x + 40), (y + 10)),
            ((x + 38), (y + 42)),
            (13)
        )

        # Dłonie
        pygame.draw.circle(
            screen,
            (215, 165, 115),
            ((x - 38), (y + 47)),
            (9)
        )

        pygame.draw.circle(
            screen,
            (215, 165, 115),
            ((x + 38), (y + 47)),
            (9)
        )

        # =========================
        # SZYJA
        # =========================

        pygame.draw.rect(
            screen,
            (215, 165, 115),
            (
                (x - 11),
                (y - 18),
                (22),
                (18)
            )
        )

        # =========================
        # USZY
        # =========================

        pygame.draw.circle(
            screen,
            (205, 150, 105),
            ((x - 31), (y - 40)),
            (9)
        )

        pygame.draw.circle(
            screen,
            (205, 150, 105),
            ((x + 31), (y - 40)),
            (9)
        )

        # =========================
        # GŁOWA
        # =========================

        pygame.draw.ellipse(
            screen,
            (225, 175, 125),
            (
                (x - 30),
                (y - 72),
                (60),
                (65)
            )
        )

        # =========================
        # WŁOSY
        # =========================

        pygame.draw.ellipse(
            screen,
            (65, 38, 20),
            (
                (x - 32),
                (y - 78),
                (64),
                (38)
            )
        )

        # Grzywka
        pygame.draw.polygon(
            screen,
            (65, 38, 20),
            [
                ((x - 30), (y - 55)),
                ((x - 15), (y - 65)),
                ((x - 5), (y - 52)),
                ((x + 10), (y - 66)),
                ((x + 30), (y - 55)),
                ((x + 25), (y - 42)),
                ((x - 25), (y - 42))
            ]
        )

        # =========================
        # OCZY
        # =========================

        pygame.draw.ellipse(
            screen,
            (245, 245, 235),
            (
                (x - 21),
                (y - 44),
                (15),
                (9)
            )
        )

        pygame.draw.ellipse(
            screen,
            (245, 245, 235),
            (
                (x + 6),
                (y - 44),
                (15),
                (9)
            )
        )

        pygame.draw.circle(
            screen,
            (35, 35, 35),
            ((x - 13), (y - 40)),
            (4)
        )

        pygame.draw.circle(
            screen,
            (35, 35, 35),
            ((x + 13), (y - 40)),
            (4)
        )

        # =========================
        # NOS
        # =========================

        pygame.draw.polygon(
            screen,
            (195, 140, 95),
            [
                ((x), (y - 40)),
                ((x - 5), (y - 25)),
                ((x + 6), (y - 25))
            ]
        )

        # =========================
        # BRODA
        # =========================

        pygame.draw.arc(
            screen,
            (75, 45, 25),
            (
                (x - 18),
                (y - 25),
                (36),
                (28)
            ),
            0,
            3.14,
            (6)
        )

        # Usta
        pygame.draw.line(
            screen,
            (110, 55, 45),
            ((x - 7), (y - 19)),
            ((x + 7), (y - 19)),
            (2)
        )

    @staticmethod
    def draw_hell_demon(x, y, walk_animation=0, walking=False):
        # =====================================
        # KOLORY
        # =====================================

        body = (165, 45, 45)
        body_light = (210, 65, 50)
        body_dark = (95, 25, 30)

        skin = (190, 55, 50)
        skin_light = (225, 75, 55)
        skin_dark = (105, 25, 30)

        wing = (55, 25, 35)
        wing_light = (105, 35, 50)

        horn = (235, 190, 125)
        horn_dark = (150, 100, 65)

        eye_white = (255, 220, 90)
        eye = (45, 10, 10)

        mouth = (45, 10, 15)
        teeth = (245, 230, 180)

        foot = (65, 20, 25)
        tail = (110, 25, 30)

        # =====================================
        # ANIMACJA CHODZENIA
        # =====================================

        if walking:
            leg_offset = math.sin(walk_animation) * 7
            arm_offset = math.sin(walk_animation) * 5
            body_offset = abs(math.sin(walk_animation)) * 2
        else:
            leg_offset = 0
            arm_offset = 0
            body_offset = 0

        y = y - body_offset

        # =====================================
        # OGON
        # =====================================

        pygame.draw.line(
            screen,
            tail,
            (
                (x + 25),
                (y + 60)
            ),
            (
                (x + 75),
                (y + 90)
            ),
            (10)
        )

        pygame.draw.line(
            screen,
            tail,
            (
                (x + 75),
                (y + 90)
            ),
            (
                (x + 105),
                (y + 65)
            ),
            (9)
        )

        pygame.draw.polygon(
            screen,
            body_dark,
            [
                ((x + 100), (y + 65)),
                ((x + 118), (y + 57)),
                ((x + 107), (y + 75))
            ]
        )

        # =====================================
        # SKRZYDŁA
        # =====================================

        pygame.draw.polygon(
            screen,
            wing,
            [
                ((x - 35), (y - 5)),
                ((x - 65), (y - 35)),
                ((x - 105), (y - 65)),
                ((x - 120), (y - 45)),
                ((x - 110), (y - 5)),
                ((x - 90), (y + 25)),
                ((x - 55), (y + 35))
            ]
        )

        pygame.draw.polygon(
            screen,
            wing,
            [
                ((x + 35), (y - 5)),
                ((x + 65), (y - 35)),
                ((x + 105), (y - 65)),
                ((x + 120), (y - 45)),
                ((x + 110), (y - 5)),
                ((x + 90), (y + 25)),
                ((x + 55), (y + 35))
            ]
        )

        pygame.draw.polygon(
            screen,
            wing_light,
            [
                ((x - 45), (y - 8)),
                ((x - 70), (y - 30)),
                ((x - 98), (y - 52)),
                ((x - 88), (y - 15)),
                ((x - 60), (y + 20))
            ]
        )

        pygame.draw.polygon(
            screen,
            wing_light,
            [
                ((x + 45), (y - 8)),
                ((x + 70), (y - 30)),
                ((x + 98), (y - 52)),
                ((x + 88), (y - 15)),
                ((x + 60), (y + 20))
            ]
        )

        # =====================================
        # NOGI
        # =====================================

        pygame.draw.polygon(
            screen,
            body_dark,
            [
                ((x - 28), (y + 60 + leg_offset)),
                ((x - 7), (y + 60 - leg_offset)),
                ((x - 12), (y + 105 - leg_offset)),
                ((x - 35), (y + 105 + leg_offset))
            ]
        )

        pygame.draw.polygon(
            screen,
            body_dark,
            [
                ((x + 7), (y + 60 - leg_offset)),
                ((x + 28), (y + 60 + leg_offset)),
                ((x + 35), (y + 105 + leg_offset)),
                ((x + 12), (y + 105 - leg_offset))
            ]
        )

        # =====================================
        # STOPY
        # =====================================

        pygame.draw.ellipse(
            screen,
            foot,
            (
                (x - 45 - leg_offset),
                (y + 98 + leg_offset),
                (43),
                (19)
            )
        )

        pygame.draw.ellipse(
            screen,
            foot,
            (
                (x + 2 + leg_offset),
                (y + 98 - leg_offset),
                (43),
                (19)
            )
        )

        # =====================================
        # SZPONY STÓP
        # =====================================

        pygame.draw.polygon(
            screen,
            horn,
            [
                ((x - 40 - leg_offset), (y + 108 + leg_offset)),
                ((x - 48 - leg_offset), (y + 116 + leg_offset)),
                ((x - 32 - leg_offset), (y + 110 + leg_offset))
            ]
        )

        pygame.draw.polygon(
            screen,
            horn,
            [
                ((x + 35 + leg_offset), (y + 110 - leg_offset)),
                ((x + 48 + leg_offset), (y + 116 - leg_offset)),
                ((x + 43 + leg_offset), (y + 106 - leg_offset))
            ]
        )

        # =====================================
        # TUŁÓW
        # =====================================

        pygame.draw.polygon(
            screen,
            body,
            [
                ((x - 43), (y - 8)),
                ((x - 35), (y + 55)),
                ((x - 15), (y + 75)),
                ((x + 15), (y + 75)),
                ((x + 35), (y + 55)),
                ((x + 43), (y - 8)),
                ((x + 25), (y - 25)),
                ((x - 25), (y - 25))
            ]
        )

        # Brzuch
        pygame.draw.ellipse(
            screen,
            body_light,
            (
                (x - 27),
                (y + 3),
                (54),
                (65)
            )
        )

        pygame.draw.arc(
            screen,
            body_dark,
            (
                (x - 23),
                (y + 20),
                (46),
                (40)
            ),
            0,
            3.14,
            (5)
        )

        # =====================================
        # RAMIONA
        # =====================================

        pygame.draw.circle(
            screen,
            body,
            (
                (x - 40),
                (y)
            ),
            (14)
        )

        pygame.draw.circle(
            screen,
            body,
            (
                (x + 40),
                (y)
            ),
            (14)
        )

        # Lewe ramię
        pygame.draw.line(
            screen,
            body,
            (
                (x - 47),
                (y + 7)
            ),
            (
                (x - 65),
                (y + 40 + arm_offset)
            ),
            (13)
        )

        # Prawe ramię
        pygame.draw.line(
            screen,
            body,
            (
                (x + 47),
                (y + 7)
            ),
            (
                (x + 65),
                (y + 40 - arm_offset)
            ),
            (13)
        )

        # =====================================
        # DŁONIE
        # =====================================

        pygame.draw.circle(
            screen,
            skin,
            (
                (x - 67),
                (y + 45 + arm_offset)
            ),
            (10)
        )

        pygame.draw.circle(
            screen,
            skin,
            (
                (x + 67),
                (y + 45 - arm_offset)
            ),
            (10)
        )

        # Pazury lewej dłoni
        pygame.draw.line(
            screen,
            horn,
            (
                (x - 72),
                (y + 48 + arm_offset)
            ),
            (
                (x - 82),
                (y + 55 + arm_offset)
            ),
            (3)
        )

        # Pazury prawej dłoni
        pygame.draw.line(
            screen,
            horn,
            (
                (x + 72),
                (y + 48 - arm_offset)
            ),
            (
                (x + 82),
                (y + 55 - arm_offset)
            ),
            (3)
        )

        # =====================================
        # SZYJA
        # =====================================

        pygame.draw.rect(
            screen,
            skin_dark,
            (
                (x - 13),
                (y - 38),
                (26),
                (24)
            )
        )

        # =====================================
        # USZY
        # =====================================

        pygame.draw.polygon(
            screen,
            skin_dark,
            [
                ((x - 30), (y - 45)),
                ((x - 48), (y - 63)),
                ((x - 27), (y - 65))
            ]
        )

        pygame.draw.polygon(
            screen,
            skin_dark,
            [
                ((x + 30), (y - 45)),
                ((x + 48), (y - 63)),
                ((x + 27), (y - 65))
            ]
        )

        # =====================================
        # GŁOWA
        # =====================================

        pygame.draw.ellipse(
            screen,
            skin,
            (
                (x - 35),
                (y - 85),
                (70),
                (68)
            )
        )

        # =====================================
        # ROGI
        # =====================================

        pygame.draw.polygon(
            screen,
            horn,
            [
                ((x - 27), (y - 72)),
                ((x - 48), (y - 108)),
                ((x - 42), (y - 68))
            ]
        )

        pygame.draw.line(
            screen,
            horn_dark,
            (
                (x - 30),
                (y - 76)
            ),
            (
                (x - 44),
                (y - 100)
            ),
            (4)
        )

        pygame.draw.polygon(
            screen,
            horn,
            [
                ((x + 27), (y - 72)),
                ((x + 48), (y - 108)),
                ((x + 42), (y - 68))
            ]
        )

        pygame.draw.line(
            screen,
            horn_dark,
            (
                (x + 30),
                (y - 76)
            ),
            (
                (x + 44),
                (y - 100)
            ),
            (4)
        )

        # =====================================
        # BRWI
        # =====================================

        pygame.draw.line(
            screen,
            body_dark,
            (
                (x - 25),
                (y - 49)
            ),
            (
                (x - 7),
                (y - 55)
            ),
            (5)
        )

        pygame.draw.line(
            screen,
            body_dark,
            (
                (x + 7),
                (y - 55)
            ),
            (
                (x + 25),
                (y - 49)
            ),
            (5)
        )

        # =====================================
        # OCZY
        # =====================================

        pygame.draw.ellipse(
            screen,
            eye_white,
            (
                (x - 24),
                (y - 46),
                (18),
                (13)
            )
        )

        pygame.draw.ellipse(
            screen,
            eye_white,
            (
                (x + 6),
                (y - 46),
                (18),
                (13)
            )
        )

        pygame.draw.circle(
            screen,
            eye,
            (
                (x - 15),
                (y - 39)
            ),
            (4)
        )

        pygame.draw.circle(
            screen,
            eye,
            (
                (x + 15),
                (y - 39)
            ),
            (4)
        )

        # Błysk w oku
        pygame.draw.circle(
            screen,
            (255, 255, 180),
            (
                (x - 13),
                (y - 41)
            ),
            (2)
        )

        pygame.draw.circle(
            screen,
            (255, 255, 180),
            (
                (x + 17),
                (y - 41)
            ),
            (2)
        )

        # =====================================
        # NOS
        # =====================================

        pygame.draw.polygon(
            screen,
            skin_dark,
            [
                ((x), (y - 39)),
                ((x - 7), (y - 24)),
                ((x + 7), (y - 24))
            ]
        )

        # =====================================
        # MAŁY UŚMIECH
        # =====================================

        pygame.draw.ellipse(
            screen,
            mouth,
            (
                (x - 17),
                (y - 18),
                (34),
                (20)
            )
        )

        # Zęby
        pygame.draw.polygon(
            screen,
            teeth,
            [
                ((x - 13), (y - 16)),
                ((x - 7), (y - 7)),
                ((x), (y - 15)),
                ((x + 7), (y - 7)),
                ((x + 13), (y - 16))
            ]
        )

        # Dolna warga
        pygame.draw.arc(
            screen,
            (145, 40, 45),
            (
                (x - 12),
                (y - 10),
                (24),
                (12)
            ),
            0,
            3.14,
            (2)
        )

        # =====================================
        # KOLCE NA GŁOWIE
        # =====================================

        pygame.draw.polygon(
            screen,
            body_dark,
            [
                ((x - 20), (y - 78)),
                ((x - 12), (y - 94)),
                ((x - 5), (y - 78))
            ]
        )

        pygame.draw.polygon(
            screen,
            body_dark,
            [
                ((x + 5), (y - 78)),
                ((x + 13), (y - 94)),
                ((x + 21), (y - 78))
            ]
        )

class Demon:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.target_x = x
        self.target_y = y

        self.moving_to_target = False

        # =========================
        # RUCH
        # =========================

        self.speed = 3

        # =========================
        # ANIMACJA CHODZENIA
        # =========================

        self.walking = False
        self.walk_animation = 0
        self.walk_animation_speed = 0.20

    # =========================================================
    # USTAWIENIE POZYCJI
    # =========================================================

    def set_position(self, x, y):

        self.x = x
        self.y = y

    # =========================================================
    # RUCH DO CELU
    # =========================================================

    def move_to(self, x, y, speed=None):

        if speed is None:
            speed = self.speed

        self.target_x = x
        self.target_y = y
        self.speed = speed

        self.moving_to_target = True
        self.walking = True

        dx = self.target_x - self.x
        dy = self.target_y - self.y

        distance = math.sqrt(dx * dx + dy * dy)

        # =========================
        # DOTARŁ DO CELU
        # =========================

        if distance <= speed:
            self.x = self.target_x
            self.y = self.target_y

            self.moving_to_target = False
            self.walking = False
            self.walk_animation = 0

            return True

        # =========================
        # RUCH
        # =========================

        dx /= distance
        dy /= distance

        self.x += dx * speed
        self.y += dy * speed

        return False

    def stop_moving_to(self):

        self.moving_to_target = False
        self.walking = False

    # =========================================================
    # ANIMACJA
    # =========================================================

    def update_animation(self):

        if self.walking:

            self.walk_animation += self.walk_animation_speed

            if self.walk_animation >= math.pi * 2:

                self.walk_animation -= math.pi * 2

        else:

            self.walk_animation = 0

    # =========================================================
    # RYSOWANIE
    # =========================================================

    def draw(self, screen):

        self.update_animation()

        textures.draw_hell_demon(
            self.x,
            self.y,
            self.walk_animation,
            self.walking
        )

class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        color=(60, 120, 200),
        hover_color=(80, 150, 230)
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.color = color
        self.hover_color = hover_color

        self.text_color = (255, 255, 255)

        self.enabled = True

        self.font = pygame.font.Font(
            None,
            (45)
        )

    # =========================================================
    # SPRAWDZANIE CZY MYSZKA JEST NAD PRZYCISKIEM
    # =========================================================

    def is_hovered(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        x = (self.x)
        y = (self.y)
        width = (self.width)
        height = (self.height)

        return (
            x <= mouse_x <= x + width
            and
            y <= mouse_y <= y + height
        )

    # =========================================================
    # RYSOWANIE
    # =========================================================

    def draw(self, screen):

        x = (self.x)
        y = (self.y)
        width = (self.width)
        height = (self.height)

        # =====================================================
        # KOLOR
        # =====================================================

        if not self.enabled:

            # ZABLOKOWANY
            color = (45, 45, 45)
            border_color = (25, 25, 25)

        else:

            # NORMALNY
            color = self.color
            border_color = (35, 70, 100)

            # =================================================
            # HOVER
            # =================================================

            if self.is_hovered():

                color = self.hover_color

                new_width = width * 1.05
                new_height = height * 1.05

                x -= (new_width - width) / 2
                y -= (new_height - height) / 2

                width = new_width
                height = new_height

        # =====================================================
        # CIEŃ
        # =====================================================

        pygame.draw.rect(
            screen,
            (35, 35, 35),
            (
                int(x),
                int(y + (7)),
                int(width),
                int(height)
            ),
            border_radius=(12)
        )

        # =====================================================
        # OBRAMÓWKA
        # =====================================================

        pygame.draw.rect(
            screen,
            border_color,
            (
                int(x),
                int(y),
                int(width),
                int(height)
            ),
            border_radius=(12)
        )

        # =====================================================
        # ŚRODEK
        # =====================================================

        border_size = (4)

        pygame.draw.rect(
            screen,
            color,
            (
                int(x + border_size),
                int(y + border_size),
                int(width - border_size * 2),
                int(height - border_size * 2)
            ),
            border_radius=(9)
        )

        # =====================================================
        # TEKST
        # =====================================================

        if isinstance(self.text, list):

            # -------------------------------------------------
            # TEKST WIELU LINII
            # -------------------------------------------------

            text_surfaces = []

            for line in self.text:

                surface = self.font.render(
                    str(line),
                    True,
                    self.text_color
                )

                text_surfaces.append(surface)

            spacing = (8)

            total_height = (
                sum(
                    surface.get_height()
                    for surface in text_surfaces
                )
                +
                spacing * (len(text_surfaces) - 1)
            )

            current_y = (
                y
                + height / 2
                - total_height / 2
            )

            for surface in text_surfaces:

                text_rect = surface.get_rect(
                    center=(
                        int(x + width / 2),
                        int(
                            current_y
                            + surface.get_height() / 2
                        )
                    )
                )

                screen.blit(
                    surface,
                    text_rect
                )

                current_y += (
                    surface.get_height()
                    + spacing
                )

        else:

            # -------------------------------------------------
            # ZWYKŁY TEKST
            # -------------------------------------------------

            text_surface = self.font.render(
                str(self.text),
                True,
                self.text_color
            )

            text_rect = text_surface.get_rect(
                center=(
                    int(x + width / 2),
                    int(y + height / 2)
                )
            )

            screen.blit(
                text_surface,
                text_rect
            )

    # =========================================================
    # KLIKNIĘCIE
    # =========================================================

    def clicked(self):

        # ZABLOKOWANY = NIE MOŻNA KLIKNĄĆ
        if not self.enabled:
            return False

        return self.is_hovered()

class Entry:
    def __init__(self, x, y, width, height, placeholder=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder

        self.text = ""
        self.active = False
        self.max_length = 15

        self.font = pygame.font.Font(None, (40))
        self.counter_font = pygame.font.Font(None, (30))

    def draw(self, screen):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Normalne wymiary
        x = (self.x)
        y = (self.y)
        width = (self.width)
        height = (self.height)

        # ==========================================
        # SPRAWDZENIE NAJECHANIA
        # ==========================================

        hovered = (
                x <= mouse_x <= x + width
                and
                y <= mouse_y <= y + height
        )

        if hovered:
            # Powiększenie o 5%
            new_width = width * 1.05
            new_height = height * 1.05

            # Wyśrodkowanie
            x = x - (new_width - width) / 2
            y = y - (new_height - height) / 2

            width = new_width
            height = new_height

        # ==========================================
        # CIEŃ
        # ==========================================

        pygame.draw.rect(
            screen,
            (35, 35, 35),
            (
                int(x),
                int(y + (7)),
                int(width),
                int(height)
            ),
            border_radius=(12)
        )

        # ==========================================
        # OBRAMÓWKA
        # ==========================================

        pygame.draw.rect(
            screen,
            (35, 70, 100),
            (
                int(x),
                int(y),
                int(width),
                int(height)
            ),
            border_radius=(12)
        )

        # ==========================================
        # ŚRODEK
        # ==========================================

        pygame.draw.rect(
            screen,
            (60, 120, 200),
            (
                int(x + (4)),
                int(y + (4)),
                int(width - (8)),
                int(height - (8))
            ),
            border_radius=(9)
        )

        # ==========================================
        # TEKST
        # ==========================================

        if self.text:
            text_surface = self.font.render(
                self.text,
                True,
                (255, 255, 255)
            )
        else:
            text_surface = self.font.render(
                self.placeholder,
                True,
                (180, 180, 180)
            )

        text_rect = text_surface.get_rect(
            midleft=(
                int(x + (20)),
                int(y + height / 2)
            )
        )

        screen.blit(text_surface, text_rect)

        # ==========================================
        # LICZNIK ZNAKÓW
        # ==========================================

        counter_surface = self.counter_font.render(
            f"{len(self.text)}/{self.max_length}",
            True,
            (255, 255, 255)
        )

        counter_rect = counter_surface.get_rect(
            midright=(
                int(x + width - (15)),
                int(y + height / 2)
            )
        )

        screen.blit(counter_surface, counter_rect)

        # ==========================================
        # KURSOR
        # ==========================================

        if self.active:
            cursor_x = (
                    x
                    + (20)
                    + self.font.size(self.text)[0]
            )

            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (
                    int(cursor_x),
                    int(y + (25)),
                    (2),
                    int(height - (50))
                )
            )

    def handle_event(self, event):

        # KLIKNIĘCIE MYSZKĄ
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                mouse_x, mouse_y = event.pos

                x = (self.x)
                y = (self.y)
                width = (self.width)
                height = (self.height)

                # Kliknięto w Entry
                if (
                    x <= mouse_x <= x + width
                    and
                    y <= mouse_y <= y + height
                ):
                    self.active = True
                else:
                    # Kliknięto poza Entry
                    self.active = False

                return

        # Jeśli Entry nie jest aktywne,
        # nie można wpisywać
        if not self.active:
            return

        # KLAWISZE
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pygame.K_RETURN:
                self.active = False

            else:
                # MAX 15 ZNAKÓW
                if len(self.text) < self.max_length:
                    self.text += event.unicode

def draw_multiline_text_with_frame(
    screen,
    lines,
    font,
    center,
    animation=False,
    color=(60, 120, 200)
):
    # =========================================
    # ANIMACJA
    # =========================================

    if animation:
        if not hasattr(draw_multiline_text_with_frame, "animation_start"):
            draw_multiline_text_with_frame.animation_start = pygame.time.get_ticks()

        elapsed = (
            pygame.time.get_ticks()
            - draw_multiline_text_with_frame.animation_start
        )

        animation_duration = 300

        progress = min(
            elapsed / animation_duration,
            1.0
        )

        # Płynniejsza animacja
        progress = 1 - (1 - progress) ** 3

    else:
        progress = 1.0

    # =========================================
    # RENDEROWANIE TEKSTU
    # =========================================

    rendered_lines = []

    for line in lines:
        rendered_lines.append(
            font.render(
                line,
                True,
                (255, 255, 255)
            )
        )

    # =========================================
    # ODSTĘP MIĘDZY LINIAMI
    # =========================================

    spacing = (10)

    # =========================================
    # SZEROKOŚĆ TEKSTU
    # =========================================

    max_width = max(
        text.get_width()
        for text in rendered_lines
    )

    # =========================================
    # WYSOKOŚĆ TEKSTU
    # =========================================

    total_height = (
        sum(
            text.get_height()
            for text in rendered_lines
        )
        +
        spacing * (len(rendered_lines) - 1)
    )

    # =========================================
    # PADDING
    # =========================================

    padding_x = (25)
    padding_y = (20)

    # =========================================
    # PEŁNY ROZMIAR RAMKI
    # =========================================

    full_width = max_width + padding_x * 2
    full_height = total_height + padding_y * 2

    # =========================================
    # ROZMIAR ANIMOWANY
    # =========================================

    frame_width = int(full_width * progress)
    frame_height = int(full_height * progress)

    frame_rect = pygame.Rect(
        center[0] - frame_width // 2,
        center[1] - frame_height // 2,
        frame_width,
        frame_height
    )

    # =========================================
    # CIEŃ
    # =========================================

    shadow_rect = frame_rect.copy()
    shadow_rect.y += (7)

    pygame.draw.rect(
        screen,
        (5, 5, 10),
        shadow_rect,
        border_radius=(12)
    )

    # =========================================
    # OBRAMÓWKA
    # =========================================

    pygame.draw.rect(
        screen,
        (10, 20, 70),
        frame_rect,
        border_radius=(12)
    )

    # =========================================
    # TŁO
    # =========================================

    border_size = (4)

    inner_rect = pygame.Rect(
        frame_rect.x + border_size,
        frame_rect.y + border_size,
        max(
            1,
            frame_rect.width - border_size * 2
        ),
        max(
            1,
            frame_rect.height - border_size * 2
        )
    )

    pygame.draw.rect(
        screen,
        color,
        inner_rect,
        border_radius=(9)
    )

    # =========================================
    # TEKST
    # =========================================

    y = center[1] - total_height // 2

    for text_surface in rendered_lines:

        # =====================================
        # ANIMOWANIE TEKSTU
        # =====================================

        if animation:

            text_width = max(
                1,
                int(
                    text_surface.get_width()
                    * progress
                )
            )

            text_height = max(
                1,
                int(
                    text_surface.get_height()
                    * progress
                )
            )

            animated_text = pygame.transform.smoothscale(
                text_surface,
                (
                    text_width,
                    text_height
                )
            )

        else:
            animated_text = text_surface

        # =====================================
        # POZYCJA TEKSTU
        # =====================================

        text_rect = animated_text.get_rect(
            center=(
                center[0],
                y + text_surface.get_height() // 2
            )
        )

        # =====================================
        # RYSOWANIE TEKSTU
        # =====================================

        screen.blit(
            animated_text,
            text_rect
        )

        y += text_surface.get_height() + spacing

settings_button = Button(
    75, 1125, 450, 125,
    "SETTINGS",
    (60, 120, 200),
    (80, 150, 230)
)
new_game_button = Button(
    75, 325, 450, 125,
    "NEW GAME",
    (60, 120, 200),
    (80, 150, 230)
)
load_game_button = Button(
    75, 525, 450, 125,
    "LOAD GAME",
    (60, 120, 200),
    (80, 150, 230)
)
fast_load_game_button = Button(
    75, 725, 450, 125,
    "LAST SAVE",
    (60, 120, 200),
    (80, 150, 230)
)
help_save_button = Button(
    75, 925, 450, 125,
    "RECOVER SAVE",
    (60, 120, 200),
    (80, 150, 230)
)

# CZERWONY BACK
back_button = Button(
    75, 1175, 450, 125,
    "BACK",
    (190, 55, 55),
    (225, 75, 75)
)

create_button = Button(
    75, 1030, 450, 125,
    "CREATE",
    (60, 120, 200),
    (80, 150, 230)
)
character_name_entry = Entry(
    75,
    325,
    450,
    100,
    "Enter character name..."
)
character_name = ""
selected_elemental = None
selected_difficulty = None

water_elemental_button = Button(
    90, 565, 200, 60,
    "WATER",
    (30, 90, 220),
    (50, 120, 255)
)
nature_elemental_button = Button(
    315, 565, 200, 60,
    "NATURE",
    (40, 180, 70),
    (60, 215, 90)
)
wind_elemental_button = Button(
    90, 640, 200, 60,
    "WIND",
    (100, 100, 100),
    (130, 130, 130)
)
fire_elemental_button = Button(
    315, 640, 200, 60,
    "FIRE",
    (230, 130, 30),
    (255, 160, 50)
)

easy_difficulty_button = Button(
    90, 855, 200, 60,
    "EASY",
    (40, 180, 70),
    (60, 215, 90)
)
normal_difficulty_button = Button(
    315, 855, 200, 60,
    "NORMAL",
    (220, 180, 30),
    (245, 205, 50)
)
hard_difficulty_button = Button(
    90, 930, 200, 60,
    "HARD",
    (230, 130, 30),
    (255, 160, 50)
)
impossible_difficulty_button = Button(
    315, 930, 200, 60,
    "IMPOSSIBLE",
    (200, 50, 50),
    (230, 70, 70)
)

fast_load_game_confirm_button = Button(
    75, 775, 450, 125,
    "CONFIRM",
    (60, 120, 200),
    (80, 150, 230)
)

save_file_1_button = Button(
    465, 325, 100, 100,
    "i",
    (60, 120, 200),
    (80, 150, 230)
)

save_file_2_button = Button(
    465, 525, 100, 100,
    "i",
    (60, 120, 200),
    (80, 150, 230)
)

save_file_3_button = Button(
    465, 725, 100, 100,
    "i",
    (60, 120, 200),
    (80, 150, 230)
)

save_file_4_button = Button(
    465, 925, 100, 100,
    "i",
    (60, 120, 200),
    (80, 150, 230)
)

delete_save_button = Button(
    75, 1025, 450, 125,
    "DELETE SAVE",
    (190, 55, 55),
    (225, 75, 75)
)

data = save.load_game()
#Save bezposredenio w grze

name1 = data["saves"]["save1"]["character_name"]
if name1 == "":
    name1 = "Empty"
save_file_1_button2 = Button(
    50, 325, 375, 100,
    [
        "<    SAVE 1    >",
        f"Name: {name1}"
    ]
)
if name1 == "Empty":
    save_file_1_button2.enabled = False
else:
     save_file_1_button2.enabled = True

name2 = data["saves"]["save2"]["character_name"]
if name2 == "":
    name2 = "Empty"
save_file_2_button2 = Button(
    50, 525, 375, 100,
    [
        "<    SAVE 2    >",
        f"Name: {name2}"
    ]
)
if name2 == "Empty":
    save_file_2_button2.enabled = False
else:
    save_file_2_button2.enabled = True

name3 = data["saves"]["save3"]["character_name"]
if name3 == "":
    name3 = "Empty"
save_file_3_button2 = Button(
    50, 725, 375, 100,
    [
        "<    SAVE 3    >",
        f"Name: {name3}"
    ]
)
if name3 == "Empty":
    save_file_3_button2.enabled = False
else:
    save_file_3_button2.enabled = True

name4 = data["saves"]["save4"]["character_name"]
if name4 == "":
    name4 = "Empty"
save_file_4_button2 = Button(
    50, 925, 375, 100,
    [
        "<    SAVE 4    >",
        f"Name: {name4}"
    ]
)
if name4 == "Empty":
    save_file_4_button2.enabled = False
else:
    save_file_4_button2.enabled = True

font = pygame.font.Font(None, (75))
font2 = pygame.font.Font(None, (50))
font3 = pygame.font.Font(None, (35))
text = font.render("Aroarente RPG :", True, (255, 255, 255))
text2 = font.render("Explore the world", True, (255, 255, 255))

#SAVE - CLASSY
dialogue_step = 0
last_dialogue_step = -1
dialogue_timer = 0
#LOOP - SAVE

katana = swords.Katana()
while running:
    clock.tick(settings.FPS)

    if game_state == "menu":
        for event in pygame.event.get():
            character_name_entry.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if game_menu_state == "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if settings_button.clicked():
                            game_menu_state = "settings"
                            just_entered_settings = True

                        if new_game_button.clicked():
                            game_menu_state = "new_game"

                        if load_game_button.clicked():
                            game_menu_state = "load_game"
                            just_entered_load_save = True

                        if fast_load_game_button.clicked():
                            game_menu_state = "last_save"
                            just_entered_last_save = True

                        if help_save_button.clicked():
                            game_menu_state = "recover_save"

            if game_menu_state == "new_game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if create_button.clicked():
                            if len(character_name_entry.text) >= 3 and selected_elemental is not None and selected_difficulty is not None:
                                character_name = character_name_entry.text

                        if water_elemental_button.clicked():
                            selected_elemental = "water"

                        elif nature_elemental_button.clicked():
                            selected_elemental = "nature"

                        elif wind_elemental_button.clicked():
                            selected_elemental = "wind"

                        elif fire_elemental_button.clicked():
                            selected_elemental = "fire"

                        if easy_difficulty_button.clicked():
                            selected_difficulty = "easy"

                        elif normal_difficulty_button.clicked():
                            selected_difficulty = "normal"

                        elif hard_difficulty_button.clicked():
                            selected_difficulty = "hard"

                        elif impossible_difficulty_button.clicked():
                            selected_difficulty = "impossible"

                        if create_button.clicked():
                            empty_saves = []
                            for save_name, save_data in data["saves"].items():
                                if save_data["character_name"] == "":
                                    empty_saves.append(save_name)

                            if len(empty_saves) > 0:
                                save_name = empty_saves[0]

                                data["saves"][save_name]["character_name"] = character_name
                                data["saves"][save_name]["elemental"] = selected_elemental
                                data["saves"][save_name]["difficulty"] = selected_difficulty

                                data["variables"]["last_save"] = save_name

                                save.save_game(data)

                            game_menu_state = "menu"
                            selected_elemental = None
                            selected_difficulty = None
                            character_name = ""
                            character_name_entry.text = ""
                            game_state = "game"
                            game_game_state = "cutsceene1"

                            #__________________________________
                            dialogue_in_cutsceene1 = False

                            # =========================================================
                            # ZMIENNE CUTSCENE 1
                            # =========================================================

                            demon_walk_step = 0

                            npc_1_alive = True
                            npc_2_alive = True
                            npc_3_alive = True
                            npc_4_alive = True

                            # Zabieranie NPC
                            demon_taking_npc = False
                            demon_take_timer = 0

                            # 1.5 sekundy przy 60 FPS
                            demon_take_duration = 90

                            cutscene1_started = False
                            cutscene1_fade = 255
                            cutscene1_fade_done = False
                            cutscene1_wait = 0
                            cutscene1_wait_done = False
                            # =========================================================
                            # FADE KOŃCOWY CUTSCENY
                            # =========================================================

                            cutscene1_end_fade = 0
                            cutscene1_end_fade_done = False

                            # =========================================================
                            # FADE PO PRZEJŚCIU DO GRY
                            # =========================================================

                            game_fade = 255
                            game_fade_done = False
                            #__________________________________

                            data = save.load_game()
                            # Save bezposredenio w grze

                            name1 = data["saves"]["save1"]["character_name"]
                            if name1 == "":
                                name1 = "Empty"
                            save_file_1_button2 = Button(
                                50, 325, 375, 100,
                                [
                                    "<    SAVE 1    >",
                                    f"Name: {name1}"
                                ]
                            )
                            if name1 == "Empty":
                                save_file_1_button2.enabled = False
                            else:
                                save_file_1_button2.enabled = True

                            name2 = data["saves"]["save2"]["character_name"]
                            if name2 == "":
                                name2 = "Empty"
                            save_file_2_button2 = Button(
                                50, 525, 375, 100,
                                [
                                    "<    SAVE 2    >",
                                    f"Name: {name2}"
                                ]
                            )
                            if name2 == "Empty":
                                save_file_2_button2.enabled = False
                            else:
                                save_file_2_button2.enabled = True

                            name3 = data["saves"]["save3"]["character_name"]
                            if name3 == "":
                                name3 = "Empty"
                            save_file_3_button2 = Button(
                                50, 725, 375, 100,
                                [
                                    "<    SAVE 3    >",
                                    f"Name: {name3}"
                                ]
                            )
                            if name3 == "Empty":
                                save_file_3_button2.enabled = False
                            else:
                                save_file_3_button2.enabled = True

                            name4 = data["saves"]["save4"]["character_name"]
                            if name4 == "":
                                name4 = "Empty"
                            save_file_4_button2 = Button(
                                50, 925, 375, 100,
                                [
                                    "<    SAVE 4    >",
                                    f"Name: {name4}"
                                ]
                            )
                            if name4 == "Empty":
                                save_file_4_button2.enabled = False
                            else:
                                save_file_4_button2.enabled = True

            if game_menu_state == "last_save":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not just_entered_last_save:
                        if fast_load_game_confirm_button.clicked():
                            last_save = data["variables"]["last_save"]
                            if data["saves"][last_save]["cutsceene1_completed"] == False:
                                game_state = "game"
                                game_game_state = "cutsceene1"
                            else:
                                game_state = "game"
                                game_game_state = "game"

            if game_menu_state == "load_game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if not just_entered_load_save:
                            if save_file_1_button2.clicked():
                                data["variables"]["last_save"] = "save1"
                                save.save_game(data)
                                game_state = "game"
                                last_save = data["variables"]["last_save"]
                                if data["saves"][last_save]["cutsceene1_completed"] == False:
                                    game_state = "game"
                                    game_game_state = "cutsceene1"
                                else:
                                    game_state = "game"
                                    game_game_state = "game"
                                save.save_game(data)
                            if save_file_2_button2.clicked():
                                data["variables"]["last_save"] = "save2"
                                save.save_game(data)
                                game_state = "game"
                                last_save = data["variables"]["last_save"]
                                if data["saves"][last_save]["cutsceene1_completed"] == False:
                                    game_state = "game"
                                    game_game_state = "cutsceene1"
                                else:
                                    game_state = "game"
                                    game_game_state = "game"
                                save.save_game(data)
                            if save_file_3_button2.clicked():
                                data["variables"]["last_save"] = "save3"
                                save.save_game(data)
                                game_state = "game"
                                last_save = data["variables"]["last_save"]
                                if data["saves"][last_save]["cutsceene1_completed"] == False:
                                    game_state = "game"
                                    game_game_state = "cutsceene1"
                                else:
                                    game_state = "game"
                                    game_game_state = "game"
                                save.save_game(data)
                            if save_file_4_button2.clicked():
                                data["variables"]["last_save"] = "save4"
                                save.save_game(data)
                                game_state = "game"
                                last_save = data["variables"]["last_save"]
                                if data["saves"][last_save]["cutsceene1_completed"] == False:
                                    game_state = "game"
                                    game_game_state = "cutsceene1"
                                else:
                                    game_state = "game"
                                    game_game_state = "game"
                                save.save_game(data)

                        if save_file_1_button.clicked():
                            game_menu_state = "load_game_save_1"
                        if save_file_2_button.clicked():
                            game_menu_state = "load_game_save_2"
                        if save_file_3_button.clicked():
                            game_menu_state = "load_game_save_3"
                        if save_file_4_button.clicked():
                            game_menu_state = "load_game_save_4"

            if game_menu_state in (
                    "load_game_save_1",
                    "load_game_save_2",
                    "load_game_save_3",
                    "load_game_save_4"
            ):

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:

                        # wybór save'a
                        if game_menu_state == "load_game":
                            if save_file_1_button.clicked():
                                game_menu_state = "load_game_save_1"

                            elif save_file_2_button.clicked():
                                game_menu_state = "load_game_save_2"

                            elif save_file_3_button.clicked():
                                game_menu_state = "load_game_save_3"

                            elif save_file_4_button.clicked():
                                game_menu_state = "load_game_save_4"

                        # USUWANIE SAVE'A
                        elif game_menu_state in (
                                "load_game_save_1",
                                "load_game_save_2",
                                "load_game_save_3",
                                "load_game_save_4"
                        ):
                            if delete_save_button.clicked():

                                save_number = game_menu_state[-1]
                                save_name = f"save{save_number}"

                                data["saves"][save_name] = {
                                    "character_name": "",
                                    "elemental": "",
                                    "difficulty": "",
                                    "fruits_in_eq": [],
                                    "current_fruit": "",
                                    "swords_in_eq": [],
                                    "current_sword": "",
                                    "guns_in_eq": [],
                                    "current_gun": "",
                                    "up_armors_in_eq": [],
                                    "current_up_armor": "",
                                    "down_armors_in_eq": [],
                                    "current_down_aromor": "",
                                    "utilies_in_eq": [],
                                    "current_utility": "",
                                    "quests_done": 0,
                                    "quest_doing_rn": 0,
                                    "game_progression": 0,
                                    "current_location_X": 1280,
                                    "current_location_y": 720,
                                    "current_world": "Kingdom",
                                    "worlds_unlocked": ["Kingdom"],
                                    "current_map_on_x": 4,
                                    "current_map_on_y": 4
                                }

                                if data["variables"]["last_save"] == save_name:
                                    data["variables"]["last_save"] = "save0"
                                    save.save_game(data)

                                save.save_game(data)
                                data = save.load_game()
                                # Save bezposredenio w grze

                                name1 = data["saves"]["save1"]["character_name"]
                                if name1 == "":
                                    name1 = "Empty"
                                save_file_1_button2 = Button(
                                    50, 325, 375, 100,
                                    [
                                        "<    SAVE 1    >",
                                        f"Name: {name1}"
                                    ]
                                )
                                if name1 == "Empty":
                                    save_file_1_button2.enabled = False
                                else:
                                    save_file_1_button2.enabled = True

                                name2 = data["saves"]["save2"]["character_name"]
                                if name2 == "":
                                    name2 = "Empty"
                                save_file_2_button2 = Button(
                                    50, 525, 375, 100,
                                    [
                                        "<    SAVE 2    >",
                                        f"Name: {name2}"
                                    ]
                                )
                                if name2 == "Empty":
                                    save_file_2_button2.enabled = False
                                else:
                                    save_file_2_button2.enabled = True

                                name3 = data["saves"]["save3"]["character_name"]
                                if name3 == "":
                                    name3 = "Empty"
                                save_file_3_button2 = Button(
                                    50, 725, 375, 100,
                                    [
                                        "<    SAVE 3    >",
                                        f"Name: {name3}"
                                    ]
                                )
                                if name3 == "Empty":
                                    save_file_3_button2.enabled = False
                                else:
                                    save_file_3_button2.enabled = True

                                name4 = data["saves"]["save4"]["character_name"]
                                if name4 == "":
                                    name4 = "Empty"
                                save_file_4_button2 = Button(
                                    50, 925, 375, 100,
                                    [
                                        "<    SAVE 4    >",
                                        f"Name: {name4}"
                                    ]
                                )
                                if name4 == "Empty":
                                    save_file_4_button2.enabled = False
                                else:
                                    save_file_4_button2.enabled = True
                                game_menu_state = "menu"
                                game_menu_state = "load_game"

            if game_menu_state != "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not just_entered_settings:
                        if back_button.clicked():
                            if game_menu_state != "load_game_save_1" and game_menu_state != "load_game_save_2" and game_menu_state != "load_game_save_3" and game_menu_state != "load_game_save_4":
                                game_menu_state = "menu"
                            else:
                                game_menu_state = "load_game"

        screen.fill((80, 160, 60))

        # =====================================================
        # DROGA — FANTASY RPG
        # Naturalne krawędzie i gładka powierzchnia
        # =====================================================

        road_center_x = settings.WIDTH // 2
        road_center_y = settings.HEIGHT // 2

        # =====================================================
        # KOLORY
        # =====================================================

        road_shadow = (65, 48, 35)
        road_border = (91, 65, 44)
        road_border_mid = (119, 84, 54)
        road_border_light = (143, 103, 66)

        road_base = (153, 112, 73)
        road_surface = (174, 132, 88)
        road_surface_light = (179, 137, 92)

        # =====================================================
        # WYMIARY DROGI
        # =====================================================

        horizontal_top = road_center_y - 260
        horizontal_bottom = road_center_y + 10

        vertical_left = road_center_x - 145
        vertical_right = road_center_x + 125

        junction_left = road_center_x - 315
        junction_right = road_center_x + 315
        junction_top = road_center_y - 425
        junction_bottom = road_center_y + 210

        # =====================================================
        # 1. ZEWNĘTRZNY CIEŃ
        # =====================================================

        # Pozioma część drogi
        pygame.draw.rect(
            screen,
            road_shadow,
            (
                -5,
                horizontal_top - 5,
                settings.WIDTH + 10,
                horizontal_bottom - horizontal_top + 10
            )
        )

        # Pionowa część drogi
        pygame.draw.rect(
            screen,
            road_shadow,
            (
                vertical_left - 5,
                -5,
                vertical_right - vertical_left + 10,
                settings.HEIGHT + 10
            )
        )

        # Skrzyżowanie
        pygame.draw.rect(
            screen,
            road_shadow,
            (
                junction_left - 5,
                junction_top - 5,
                junction_right - junction_left + 10,
                junction_bottom - junction_top + 10
            ),
            border_radius=48
        )

        # =====================================================
        # 2. CIEMNE OBRZEŻE
        # =====================================================

        pygame.draw.rect(
            screen,
            road_border,
            (
                0,
                horizontal_top,
                settings.WIDTH,
                horizontal_bottom - horizontal_top
            )
        )

        pygame.draw.rect(
            screen,
            road_border,
            (
                vertical_left,
                0,
                vertical_right - vertical_left,
                settings.HEIGHT
            )
        )

        pygame.draw.rect(
            screen,
            road_border,
            (
                junction_left,
                junction_top,
                junction_right - junction_left,
                junction_bottom - junction_top
            ),
            border_radius=44
        )

        # =====================================================
        # 3. WEWNĘTRZNA WARSTWA OBRZEŻA
        # =====================================================

        pygame.draw.rect(
            screen,
            road_border_mid,
            (
                0,
                horizontal_top + 5,
                settings.WIDTH,
                horizontal_bottom - horizontal_top - 10
            )
        )

        pygame.draw.rect(
            screen,
            road_border_mid,
            (
                vertical_left + 5,
                0,
                vertical_right - vertical_left - 10,
                settings.HEIGHT
            )
        )

        pygame.draw.rect(
            screen,
            road_border_mid,
            (
                junction_left + 5,
                junction_top + 5,
                junction_right - junction_left - 10,
                junction_bottom - junction_top - 10
            ),
            border_radius=39
        )

        # =====================================================
        # 4. GŁÓWNA POWIERZCHNIA DROGI
        # =====================================================

        pygame.draw.rect(
            screen,
            road_base,
            (
                0,
                horizontal_top + 12,
                settings.WIDTH,
                horizontal_bottom - horizontal_top - 24
            )
        )

        pygame.draw.rect(
            screen,
            road_base,
            (
                vertical_left + 12,
                0,
                vertical_right - vertical_left - 24,
                settings.HEIGHT
            )
        )

        pygame.draw.rect(
            screen,
            road_base,
            (
                junction_left + 12,
                junction_top + 12,
                junction_right - junction_left - 24,
                junction_bottom - junction_top - 24
            ),
            border_radius=32
        )

        # =====================================================
        # 5. GŁADKA WARSTWA ŚRODKOWA
        # =====================================================

        pygame.draw.rect(
            screen,
            road_surface,
            (
                0,
                horizontal_top + 18,
                settings.WIDTH,
                horizontal_bottom - horizontal_top - 36
            )
        )

        pygame.draw.rect(
            screen,
            road_surface,
            (
                vertical_left + 18,
                0,
                vertical_right - vertical_left - 36,
                settings.HEIGHT
            )
        )

        pygame.draw.rect(
            screen,
            road_surface,
            (
                junction_left + 18,
                junction_top + 18,
                junction_right - junction_left - 36,
                junction_bottom - junction_top - 36
            ),
            border_radius=26
        )

        # =====================================================
        # 6. NATURALNE, ŁAGODNE KRAWĘDZIE
        # =====================================================

        # Delikatne rozjaśnienie górnej krawędzi poziomej drogi.
        # Nie tworzy linii przez środek drogi.

        pygame.draw.rect(
            screen,
            road_border_light,
            (
                0,
                horizontal_top + 5,
                settings.WIDTH,
                3
            )
        )

        # Delikatne rozjaśnienie lewej krawędzi pionowej drogi.

        pygame.draw.rect(
            screen,
            road_border_light,
            (
                vertical_left + 5,
                0,
                3,
                settings.HEIGHT
            )
        )

        # =====================================================
        # 7. WYGŁADZENIE POWIERZCHNI SKRZYŻOWANIA
        # =====================================================

        # Jednolita powierzchnia, bez plam i ozdobnych kształtów.

        pygame.draw.rect(
            screen,
            road_surface_light,
            (
                junction_left + 25,
                junction_top + 25,
                junction_right - junction_left - 50,
                junction_bottom - junction_top - 50
            ),
            border_radius=22
        )

        # Przywrócenie gładkiego koloru na całej powierzchni
        # skrzyżowania, aby nie powstała odrębna plama.

        pygame.draw.rect(
            screen,
            road_surface,
            (
                junction_left + 29,
                junction_top + 29,
                junction_right - junction_left - 58,
                junction_bottom - junction_top - 58
            ),
            border_radius=19
        )

        # =====================================================
        # 8. KAMIENIE — FANTASY RPG
        # =====================================================

        stone_shadow = (76, 53, 37)
        stone_outline = (101, 72, 49)

        stone_colors = [
            (145, 105, 70),
            (160, 117, 79),
            (173, 132, 91),
            (138, 101, 72),
            (181, 140, 99),
        ]

        stone_highlights = [
            (180, 139, 98),
            (190, 149, 108),
            (170, 130, 91),
        ]

        import random

        # =====================================================
        # 8. KAMIENIE — LOSOWO ROZMIESZCZONE NA DRODZE
        # =====================================================

        # Użyj stałego ziarna, żeby pozycje nie zmieniały się
        # przy każdym wywołaniu rysowania.
        random.seed(42)

        road_stones = []

        stone_count = 65
        stone_w_min, stone_w_max = 20, 30
        stone_h_min, stone_h_max = 10, 15

        for i in range(stone_count):
            stone_w = random.randint(stone_w_min, stone_w_max)
            stone_h = random.randint(stone_h_min, stone_h_max)

            # Wybór części drogi:
            # 0 = pozioma, 1 = pionowa, 2 = skrzyżowanie
            road_part = random.choices(
                [0, 1, 2],
                weights=[4, 3, 5],
                k=1
            )[0]

            if road_part == 0:
                # Pozioma droga
                stone_x = random.randint(
                    0,
                    max(0, settings.WIDTH - stone_w)
                )
                stone_y = random.randint(
                    horizontal_top,
                    max(horizontal_top, horizontal_bottom - stone_h)
                )

            elif road_part == 1:
                # Pionowa droga
                stone_x = random.randint(
                    vertical_left,
                    max(vertical_left, vertical_right - stone_w)
                )
                stone_y = random.randint(
                    0,
                    max(0, settings.HEIGHT - stone_h)
                )

            else:
                # Skrzyżowanie
                stone_x = random.randint(
                    junction_left,
                    max(junction_left, junction_right - stone_w)
                )
                stone_y = random.randint(
                    junction_top,
                    max(junction_top, junction_bottom - stone_h)
                )

            variant = random.randrange(5)

            road_stones.append(
                (stone_x, stone_y, stone_w, stone_h, variant)
            )

        # Nieregularne kształty kamieni
        stone_shapes = [
            [
                (0.08, 0.35), (0.27, 0.06), (0.68, 0.02),
                (0.96, 0.30), (0.88, 0.72), (0.61, 0.96),
                (0.20, 0.86), (0.02, 0.57)
            ],
            [
                (0.04, 0.28), (0.38, 0.02), (0.79, 0.12),
                (0.98, 0.48), (0.77, 0.91), (0.35, 0.98),
                (0.06, 0.70)
            ],
            [
                (0.15, 0.05), (0.75, 0.03), (0.99, 0.42),
                (0.83, 0.81), (0.48, 0.98), (0.10, 0.76),
                (0.01, 0.36)
            ],
        ]

        # Rysowanie kamieni
        for i, (stone_x, stone_y, stone_w, stone_h, variant) in enumerate(road_stones):

            if not (
                    -stone_w <= stone_x < settings.WIDTH
                    and -stone_h <= stone_y < settings.HEIGHT
            ):
                continue

            shape = stone_shapes[i % len(stone_shapes)]

            points = [
                (
                    int(stone_x + px * stone_w),
                    int(stone_y + py * stone_h)
                )
                for px, py in shape
            ]

            # Cień
            pygame.draw.polygon(
                screen,
                stone_shadow,
                [(x + 2, y + 2) for x, y in points]
            )

            # Kontur
            pygame.draw.polygon(
                screen,
                stone_outline,
                points
            )

            # Powierzchnia
            inset_points = [
                (
                    int(stone_x + (x - stone_x) * 0.86),
                    int(stone_y + (y - stone_y) * 0.76 + stone_h * 0.10)
                )
                for x, y in points
            ]

            pygame.draw.polygon(
                screen,
                stone_colors[variant % len(stone_colors)],
                inset_points
            )

            # Delikatny refleks
            highlight_points = [
                (
                    int(stone_x + px * stone_w * 0.65 + stone_w * 0.10),
                    int(stone_y + py * stone_h * 0.40 + stone_h * 0.10)
                )
                for px, py in shape[:3]
            ]

            pygame.draw.polygon(
                screen,
                stone_highlights[variant % len(stone_highlights)],
                highlight_points
            )

        # STALLS
        textures.draw_npc(810, 370, (50, 140, 70))
        textures.draw_stall(800, 340, (170, 50, 50))
        textures.draw_npc(310, 370, (180, 50, 50))
        textures.draw_stall(300, 340, (220, 170, 50))
        textures.draw_npc(1810, 370, (220, 170, 50))
        textures.draw_stall(1800, 340, (50, 140, 70))
        textures.draw_npc(2310, 370, (130, 60, 160))
        textures.draw_stall(2300, 340, (50, 90, 180))

        # LAKE
        pygame.draw.circle(
            screen,
            (50, 140, 220),
            ((2000), (1000)),
            (200)
        )

        pygame.draw.circle(
            screen,
            (50, 140, 220),
            ((2150), (1150)),
            (140)
        )

        # TREES AND ROCKS
        textures.draw_tree(365, 110)
        textures.draw_rock(900, 150)
        textures.draw_tree(2015, 125)
        textures.draw_rock(1650, 150)
        textures.draw_rock(2315, 125)
        textures.draw_rock(2315, 1000)
        textures.draw_rock(2165, 1300)
        textures.draw_tree(1700, 975)
        textures.draw_tree(300, 975)
        textures.draw_tree(800, 1025)
        textures.draw_tree(500, 1200)

        Player.draw(screen)

        shadow = pygame.Surface(((600), settings.HEIGHT), pygame.SRCALPHA)
        shadow.fill((40, 40, 40, 180))
        screen.blit(shadow, (0, 0))

        # =========================
        # TYTUŁ + CIEŃ
        # =========================

        text_rect = text.get_rect(
            center=((300), (100))
        )

        # Cień
        shadow_text_rect = text.get_rect(
            center=(
                (300) + (5),
                (100) + (5)
            )
        )

        screen.blit(
            font.render("Aroarente RPG :", True, (35, 35, 35)),
            shadow_text_rect
        )

        screen.blit(text, text_rect)

        # =========================
        # PODTYTUŁ + CIEŃ
        # =========================

        text2_rect = text2.get_rect(
            center=((300), (200))
        )

        # Cień
        shadow_text2_rect = text2.get_rect(
            center=(
                (300) + (5),
                (200) + (5)
            )
        )

        screen.blit(
            font.render("Explore the world", True, (35, 35, 35)),
            shadow_text2_rect
        )

        screen.blit(text2, text2_rect)

        if game_menu_state == "load_game":
            just_entered_load_save = False
            empty_saves = []
            for save_name, save_data in data["saves"].items():
                if save_data["character_name"] == "":
                    empty_saves.append(save_name)

            if "save1" in empty_saves:
                save_file_1_button.enabled = False
            else:
                save_file_1_button.enabled = True
            if "save2" in empty_saves:
                save_file_2_button.enabled = False
            else:
                save_file_2_button.enabled = True
            if "save3" in empty_saves:
                save_file_3_button.enabled = False
            else:
                save_file_3_button.enabled = True
            if "save4" in empty_saves:
                save_file_4_button.enabled = False
            else:
                save_file_4_button.enabled = True

            save_file_1_button.draw(screen)
            save_file_2_button.draw(screen)
            save_file_3_button.draw(screen)
            save_file_4_button.draw(screen)

            save_file_1_button2.draw(screen)
            save_file_2_button2.draw(screen)
            save_file_3_button2.draw(screen)
            save_file_4_button2.draw(screen)

        if game_menu_state == "last_save":
            just_entered_last_save = False
            fast_load_game_confirm_button.draw(screen)
            draw_multiline_text_with_frame(
                screen,
                [
                    "Are you sure",
                    "you want to",
                    "load your last",
                    "played save?"
                ],
                font2,
                ((300), (610))
            )

        if game_menu_state == "load_game_save_1":
            save_data = data['saves']['save1']
            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Name: {save_data["character_name"]} >"
                ],
                font2,
                ((300), (350))
            )
            if save_data["current_fruit"] == "":
                save_data["current_fruit"] = "None"
            if save_data["current_sword"] == "":
                save_data["current_sword"] = "None"
            if save_data["current_gun"] == "":
                save_data["current_gun"] = "None"
            if save_data["current_up_armor"] == "":
                save_data["current_up_armor"] = "None"
            if save_data["current_down_armor"] == "":
                save_data["current_down_armor"] = "None"
            if save_data["current_utility"] == "":
                save_data["current_utility"] = "None"
            draw_multiline_text_with_frame(
                screen,
                [
                    f"Difficulty: {save_data["difficulty"]}",
                    f"Elemental: {save_data["elemental"]}",
                    f"Fruit: {save_data["current_fruit"]}",
                    f"Sword: {save_data["current_sword"]}",
                    f"Gun: {save_data["current_gun"]}",
                    f"Upper armor: {save_data["current_up_armor"]}",
                    f"Down armor: {save_data["current_down_armor"]}",
                    f"Utility: {save_data["current_utility"]}",
                    f"Last seen: {save_data["current_world"]}"
                ],
                font3,
                ((300), (610))
            )
            save_data["current_fruit"] = ""
            save_data["current_sword"] = ""
            save_data["current_gun"] = ""
            save_data["current_up_armor"] = ""
            save_data["current_down_armor"] = ""
            save_data["current_utility"] = ""

            save_data["game_progression"] = int(
                (save_data["quests_done"] / data["variables"]["max_quests"]) * 100
            )
            save.save_game(data)

            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Progres: {save_data["game_progression"]}% >"
                ],
                font2,
                ((300), (870))
            )

            delete_save_button.draw(screen)

        if game_menu_state == "load_game_save_2":
            save_data = data['saves']['save2']
            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Name: {save_data["character_name"]} >"
                ],
                font2,
                ((300), (350))
            )
            if save_data["current_fruit"] == "":
                save_data["current_fruit"] = "None"
            if save_data["current_sword"] == "":
                save_data["current_sword"] = "None"
            if save_data["current_gun"] == "":
                save_data["current_gun"] = "None"
            if save_data["current_up_armor"] == "":
                save_data["current_up_armor"] = "None"
            if save_data["current_down_armor"] == "":
                save_data["current_down_armor"] = "None"
            if save_data["current_utility"] == "":
                save_data["current_utility"] = "None"
            draw_multiline_text_with_frame(
                screen,
                [
                    f"Difficulty: {save_data["difficulty"]}",
                    f"Elemental: {save_data["elemental"]}",
                    f"Fruit: {save_data["current_fruit"]}",
                    f"Sword: {save_data["current_sword"]}",
                    f"Gun: {save_data["current_gun"]}",
                    f"Upper armor: {save_data["current_up_armor"]}",
                    f"Down armor: {save_data["current_down_armor"]}",
                    f"Utility: {save_data["current_utility"]}",
                    f"Last seen: {save_data["current_world"]}"
                ],
                font3,
                ((300), (610))
            )
            save_data["current_fruit"] = ""
            save_data["current_sword"] = ""
            save_data["current_gun"] = ""
            save_data["current_up_armor"] = ""
            save_data["current_down_armor"] = ""
            save_data["current_utility"] = ""

            save_data["game_progression"] = int(
                (save_data["quests_done"] / data["variables"]["max_quests"]) * 100
            )
            save.save_game(data)

            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Progres: {save_data["game_progression"]}% >"
                ],
                font2,
                ((300), (870))
            )

            delete_save_button.draw(screen)

        if game_menu_state == "load_game_save_3":
            save_data = data['saves']['save3']
            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Name: {save_data["character_name"]} >"
                ],
                font2,
                ((300), (350))
            )
            if save_data["current_fruit"] == "":
                save_data["current_fruit"] = "None"
            if save_data["current_sword"] == "":
                save_data["current_sword"] = "None"
            if save_data["current_gun"] == "":
                save_data["current_gun"] = "None"
            if save_data["current_up_armor"] == "":
                save_data["current_up_armor"] = "None"
            if save_data["current_down_armor"] == "":
                save_data["current_down_armor"] = "None"
            if save_data["current_utility"] == "":
                save_data["current_utility"] = "None"
            draw_multiline_text_with_frame(
                screen,
                [
                    f"Difficulty: {save_data["difficulty"]}",
                    f"Elemental: {save_data["elemental"]}",
                    f"Fruit: {save_data["current_fruit"]}",
                    f"Sword: {save_data["current_sword"]}",
                    f"Gun: {save_data["current_gun"]}",
                    f"Upper armor: {save_data["current_up_armor"]}",
                    f"Down armor: {save_data["current_down_armor"]}",
                    f"Utility: {save_data["current_utility"]}",
                    f"Last seen: {save_data["current_world"]}"
                ],
                font3,
                ((300), (610))
            )
            save_data["current_fruit"] = ""
            save_data["current_sword"] = ""
            save_data["current_gun"] = ""
            save_data["current_up_armor"] = ""
            save_data["current_down_armor"] = ""
            save_data["current_utility"] = ""

            save_data["game_progression"] = int(
                (save_data["quests_done"] / data["variables"]["max_quests"]) * 100
            )
            save.save_game(data)

            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Progres: {save_data["game_progression"]}% >"
                ],
                font2,
                ((300), (870))
            )

            delete_save_button.draw(screen)

        if game_menu_state == "load_game_save_4":
            save_data = data['saves']['save4']
            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Name: {save_data["character_name"]} >"
                ],
                font2,
                ((300), (350))
            )
            if save_data["current_fruit"] == "":
                save_data["current_fruit"] = "None"
            if save_data["current_sword"] == "":
                save_data["current_sword"] = "None"
            if save_data["current_gun"] == "":
                save_data["current_gun"] = "None"
            if save_data["current_up_armor"] == "":
                save_data["current_up_armor"] = "None"
            if save_data["current_down_armor"] == "":
                save_data["current_down_armor"] = "None"
            if save_data["current_utility"] == "":
                save_data["current_utility"] = "None"
            draw_multiline_text_with_frame(
                screen,
                [
                    f"Difficulty: {save_data["difficulty"]}",
                    f"Elemental: {save_data["elemental"]}",
                    f"Fruit: {save_data["current_fruit"]}",
                    f"Sword: {save_data["current_sword"]}",
                    f"Gun: {save_data["current_gun"]}",
                    f"Upper armor: {save_data["current_up_armor"]}",
                    f"Down armor: {save_data["current_down_armor"]}",
                    f"Utility: {save_data["current_utility"]}",
                    f"Last seen: {save_data["current_world"]}"
                ],
                font3,
                ((300), (610))
            )
            save_data["current_fruit"] = ""
            save_data["current_sword"] = ""
            save_data["current_gun"] = ""
            save_data["current_up_armor"] = ""
            save_data["current_down_armor"] = ""
            save_data["current_utility"] = ""

            save_data["game_progression"] = int(
                (save_data["quests_done"] / data["variables"]["max_quests"]) * 100
            )
            save.save_game(data)

            draw_multiline_text_with_frame(
                screen,
                [
                    f"< Progres: {save_data["game_progression"]}% >"
                ],
                font2,
                ((300), (870))
            )

            delete_save_button.draw(screen)

        if game_menu_state == "new_game":
            create_button.enabled = (
                    len(character_name_entry.text) >= 3
                    and selected_elemental is not None
                    and selected_difficulty is not None
            )

            character_name_entry.draw(screen)
            create_button.draw(screen)

            # ==========================================
            # ELEMENTALE
            # ==========================================

            water_elemental_button.enabled = selected_elemental != "water"
            nature_elemental_button.enabled = selected_elemental != "nature"
            wind_elemental_button.enabled = selected_elemental != "wind"
            fire_elemental_button.enabled = selected_elemental != "fire"

            water_elemental_button.draw(screen)
            nature_elemental_button.draw(screen)
            wind_elemental_button.draw(screen)
            fire_elemental_button.draw(screen)

            easy_difficulty_button.enabled = selected_difficulty != "easy"
            normal_difficulty_button.enabled = selected_difficulty != "normal"
            hard_difficulty_button.enabled = selected_difficulty != "hard"
            impossible_difficulty_button.enabled = selected_difficulty != "impossible"

            easy_difficulty_button.draw(screen)
            normal_difficulty_button.draw(screen)
            hard_difficulty_button.draw(screen)
            impossible_difficulty_button.draw(screen)

            draw_multiline_text_with_frame(
                screen,
                [
                    "Choose an elemental"
                ],
                font2,
                ((300), (490))
            )

            draw_multiline_text_with_frame(
                screen,
                [
                    "     Select difficulty     "
                ],
                font2,
                ((300), (775))
            )

        if game_menu_state == "menu":
            if data["variables"]["last_save"] == "save0":
                fast_load_game_button.enabled = False
            else:
                fast_load_game_button.enabled = True

            empty_saves = []
            for save_name, save_data in data["saves"].items():
                if save_data["character_name"] == "":
                    empty_saves.append(save_name)

            if len(empty_saves) == 0:
                new_game_button.enabled = False
            else:
                new_game_button.enabled = True

            if len(empty_saves) <= 3:
                load_game_button.enabled = True
            else:
                load_game_button.enabled = False

            settings_button.draw(screen)
            new_game_button.draw(screen)
            load_game_button.draw(screen)
            fast_load_game_button.draw(screen)
            help_save_button.draw(screen)

        if game_menu_state == "recover_save":
            draw_multiline_text_with_frame(
                screen,
                [
                    "If you want to take",
                    "a save from your",
                    "other device you",
                    "need to go in",
                    "downloads and",
                    "take the",
                    "'AroarenteRpg_Data'",
                    "file and put it in",
                    "downloads on your",
                    "new device."
                ],
                font,
                ((300), (675))
            )

        if game_menu_state == "settings":
            draw_multiline_text_with_frame(
                screen,
                [
                    "No settings",
                    "for now.",
                    "Wait for",
                    "update (:"
                ],
                font,
                ((300), (675))
            )

        if game_menu_state != "menu":
            back_button.draw(screen)
            just_entered_settings = False

    #______________________________________________________________________________________________________________
    #                    MENU ------------------------------------------ GRA
    # _____________________________________________________________________________________________________________

    elif game_state == "game":

        # E, C, M i zwykłe sterowanie GUI działają wyłącznie
        # podczas właściwej gry, a nie podczas cutscenki.
        game_ui.set_game_active(
            game_game_state == "game"
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_game_state == "game":
                game_ui.handle_event(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = "menu"
                        game_menu_state = "menu"

            elif game_game_state == "cutsceene1":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_game_state = "game"

            elif game_game_state == "pvp":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

        if game_game_state == "cutsceene1":

            # =====================================================
            # USTAWIENIA RUCHU DEMONA
            # =====================================================

            demon_walk_y = (620)
            demon_npc_y = (430)

            demon_center_x = (1600)

            demon_npc_4_x = (2400)
            demon_npc_3_x = (1900)
            demon_npc_2_x = (900)
            demon_npc_1_x = (400)

            demon_escape_x = (2800)

            # 1.5 sekundy przy 60 FPS
            demon_take_duration = 90

            # =====================================================
            # TŁO
            # =====================================================

            screen.fill((80, 160, 60))

            # =====================================================
            # DROGA — FANTASY RPG
            # Naturalne krawędzie i gładka powierzchnia
            # =====================================================

            road_center_x = settings.WIDTH // 2
            road_center_y = settings.HEIGHT // 2

            # =====================================================
            # KOLORY
            # =====================================================

            road_shadow = (65, 48, 35)
            road_border = (91, 65, 44)
            road_border_mid = (119, 84, 54)
            road_border_light = (143, 103, 66)

            road_base = (153, 112, 73)
            road_surface = (174, 132, 88)
            road_surface_light = (179, 137, 92)

            # =====================================================
            # WYMIARY DROGI
            # =====================================================

            horizontal_top = road_center_y - 260
            horizontal_bottom = road_center_y + 10

            vertical_left = road_center_x - 145
            vertical_right = road_center_x + 125

            junction_left = road_center_x - 315
            junction_right = road_center_x + 315
            junction_top = road_center_y - 425
            junction_bottom = road_center_y + 210

            # =====================================================
            # 1. ZEWNĘTRZNY CIEŃ
            # =====================================================

            # Pozioma część drogi
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    -5,
                    horizontal_top - 5,
                    settings.WIDTH + 10,
                    horizontal_bottom - horizontal_top + 10
                )
            )

            # Pionowa część drogi
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    vertical_left - 5,
                    -5,
                    vertical_right - vertical_left + 10,
                    settings.HEIGHT + 10
                )
            )

            # Skrzyżowanie
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    junction_left - 5,
                    junction_top - 5,
                    junction_right - junction_left + 10,
                    junction_bottom - junction_top + 10
                ),
                border_radius=48
            )

            # =====================================================
            # 2. CIEMNE OBRZEŻE
            # =====================================================

            pygame.draw.rect(
                screen,
                road_border,
                (
                    0,
                    horizontal_top,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top
                )
            )

            pygame.draw.rect(
                screen,
                road_border,
                (
                    vertical_left,
                    0,
                    vertical_right - vertical_left,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_border,
                (
                    junction_left,
                    junction_top,
                    junction_right - junction_left,
                    junction_bottom - junction_top
                ),
                border_radius=44
            )

            # =====================================================
            # 3. WEWNĘTRZNA WARSTWA OBRZEŻA
            # =====================================================

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    0,
                    horizontal_top + 5,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 10
                )
            )

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    vertical_left + 5,
                    0,
                    vertical_right - vertical_left - 10,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    junction_left + 5,
                    junction_top + 5,
                    junction_right - junction_left - 10,
                    junction_bottom - junction_top - 10
                ),
                border_radius=39
            )

            # =====================================================
            # 4. GŁÓWNA POWIERZCHNIA DROGI
            # =====================================================

            pygame.draw.rect(
                screen,
                road_base,
                (
                    0,
                    horizontal_top + 12,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 24
                )
            )

            pygame.draw.rect(
                screen,
                road_base,
                (
                    vertical_left + 12,
                    0,
                    vertical_right - vertical_left - 24,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_base,
                (
                    junction_left + 12,
                    junction_top + 12,
                    junction_right - junction_left - 24,
                    junction_bottom - junction_top - 24
                ),
                border_radius=32
            )

            # =====================================================
            # 5. GŁADKA WARSTWA ŚRODKOWA
            # =====================================================

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    0,
                    horizontal_top + 18,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 36
                )
            )

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    vertical_left + 18,
                    0,
                    vertical_right - vertical_left - 36,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    junction_left + 18,
                    junction_top + 18,
                    junction_right - junction_left - 36,
                    junction_bottom - junction_top - 36
                ),
                border_radius=26
            )

            # =====================================================
            # 6. NATURALNE, ŁAGODNE KRAWĘDZIE
            # =====================================================

            # Delikatne rozjaśnienie górnej krawędzi poziomej drogi.
            # Nie tworzy linii przez środek drogi.

            pygame.draw.rect(
                screen,
                road_border_light,
                (
                    0,
                    horizontal_top + 5,
                    settings.WIDTH,
                    3
                )
            )

            # Delikatne rozjaśnienie lewej krawędzi pionowej drogi.

            pygame.draw.rect(
                screen,
                road_border_light,
                (
                    vertical_left + 5,
                    0,
                    3,
                    settings.HEIGHT
                )
            )

            # =====================================================
            # 7. WYGŁADZENIE POWIERZCHNI SKRZYŻOWANIA
            # =====================================================

            # Jednolita powierzchnia, bez plam i ozdobnych kształtów.

            pygame.draw.rect(
                screen,
                road_surface_light,
                (
                    junction_left + 25,
                    junction_top + 25,
                    junction_right - junction_left - 50,
                    junction_bottom - junction_top - 50
                ),
                border_radius=22
            )

            # Przywrócenie gładkiego koloru na całej powierzchni
            # skrzyżowania, aby nie powstała odrębna plama.

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    junction_left + 29,
                    junction_top + 29,
                    junction_right - junction_left - 58,
                    junction_bottom - junction_top - 58
                ),
                border_radius=19
            )

            # =====================================================
            # 8. KAMIENIE — FANTASY RPG
            # =====================================================

            stone_shadow = (76, 53, 37)
            stone_outline = (101, 72, 49)

            stone_colors = [
                (145, 105, 70),
                (160, 117, 79),
                (173, 132, 91),
                (138, 101, 72),
                (181, 140, 99),
            ]

            stone_highlights = [
                (180, 139, 98),
                (190, 149, 108),
                (170, 130, 91),
            ]

            import random

            # =====================================================
            # 8. KAMIENIE — LOSOWO ROZMIESZCZONE NA DRODZE
            # =====================================================

            # Użyj stałego ziarna, żeby pozycje nie zmieniały się
            # przy każdym wywołaniu rysowania.
            random.seed(42)

            road_stones = []

            stone_count = 65
            stone_w_min, stone_w_max = 20, 30
            stone_h_min, stone_h_max = 10, 15

            for i in range(stone_count):
                stone_w = random.randint(stone_w_min, stone_w_max)
                stone_h = random.randint(stone_h_min, stone_h_max)

                # Wybór części drogi:
                # 0 = pozioma, 1 = pionowa, 2 = skrzyżowanie
                road_part = random.choices(
                    [0, 1, 2],
                    weights=[4, 3, 5],
                    k=1
                )[0]

                if road_part == 0:
                    # Pozioma droga
                    stone_x = random.randint(
                        0,
                        max(0, settings.WIDTH - stone_w)
                    )
                    stone_y = random.randint(
                        horizontal_top,
                        max(horizontal_top, horizontal_bottom - stone_h)
                    )

                elif road_part == 1:
                    # Pionowa droga
                    stone_x = random.randint(
                        vertical_left,
                        max(vertical_left, vertical_right - stone_w)
                    )
                    stone_y = random.randint(
                        0,
                        max(0, settings.HEIGHT - stone_h)
                    )

                else:
                    # Skrzyżowanie
                    stone_x = random.randint(
                        junction_left,
                        max(junction_left, junction_right - stone_w)
                    )
                    stone_y = random.randint(
                        junction_top,
                        max(junction_top, junction_bottom - stone_h)
                    )

                variant = random.randrange(5)

                road_stones.append(
                    (stone_x, stone_y, stone_w, stone_h, variant)
                )

            # Nieregularne kształty kamieni
            stone_shapes = [
                [
                    (0.08, 0.35), (0.27, 0.06), (0.68, 0.02),
                    (0.96, 0.30), (0.88, 0.72), (0.61, 0.96),
                    (0.20, 0.86), (0.02, 0.57)
                ],
                [
                    (0.04, 0.28), (0.38, 0.02), (0.79, 0.12),
                    (0.98, 0.48), (0.77, 0.91), (0.35, 0.98),
                    (0.06, 0.70)
                ],
                [
                    (0.15, 0.05), (0.75, 0.03), (0.99, 0.42),
                    (0.83, 0.81), (0.48, 0.98), (0.10, 0.76),
                    (0.01, 0.36)
                ],
            ]

            # Rysowanie kamieni
            for i, (stone_x, stone_y, stone_w, stone_h, variant) in enumerate(road_stones):

                if not (
                        -stone_w <= stone_x < settings.WIDTH
                        and -stone_h <= stone_y < settings.HEIGHT
                ):
                    continue

                shape = stone_shapes[i % len(stone_shapes)]

                points = [
                    (
                        int(stone_x + px * stone_w),
                        int(stone_y + py * stone_h)
                    )
                    for px, py in shape
                ]

                # Cień
                pygame.draw.polygon(
                    screen,
                    stone_shadow,
                    [(x + 2, y + 2) for x, y in points]
                )

                # Kontur
                pygame.draw.polygon(
                    screen,
                    stone_outline,
                    points
                )

                # Powierzchnia
                inset_points = [
                    (
                        int(stone_x + (x - stone_x) * 0.86),
                        int(stone_y + (y - stone_y) * 0.76 + stone_h * 0.10)
                    )
                    for x, y in points
                ]

                pygame.draw.polygon(
                    screen,
                    stone_colors[variant % len(stone_colors)],
                    inset_points
                )

                # Delikatny refleks
                highlight_points = [
                    (
                        int(stone_x + px * stone_w * 0.65 + stone_w * 0.10),
                        int(stone_y + py * stone_h * 0.40 + stone_h * 0.10)
                    )
                    for px, py in shape[:3]
                ]

                pygame.draw.polygon(
                    screen,
                    stone_highlights[variant % len(stone_highlights)],
                    highlight_points
                )

            # =====================================================
            # STOISKO 1 - LEWE
            # =====================================================

            if npc_1_alive:
                textures.draw_npc(
                    310,
                    370,
                    (180, 50, 50)
                )

            textures.draw_stall(
                300,
                340,
                (220, 170, 50)
            )

            # =====================================================
            # STOISKO 2
            # =====================================================

            if npc_2_alive:
                textures.draw_npc(
                    810,
                    370,
                    (50, 140, 70)
                )

            textures.draw_stall(
                800,
                340,
                (170, 50, 50)
            )

            # =====================================================
            # STOISKO 3
            # =====================================================

            if npc_3_alive:
                textures.draw_npc(
                    1810,
                    370,
                    (220, 170, 50)
                )

            textures.draw_stall(
                1800,
                340,
                (50, 140, 70)
            )

            # =====================================================
            # STOISKO 4 - PRAWE
            # =====================================================

            if npc_4_alive:
                textures.draw_npc(
                    2310,
                    370,
                    (130, 60, 160)
                )

            textures.draw_stall(
                2300,
                340,
                (50, 90, 180)
            )

            # =====================================================
            # JEZIORO
            # =====================================================

            pygame.draw.circle(
                screen,
                (50, 140, 220),
                (
                    (2000),
                    (1000)
                ),
                (200)
            )

            pygame.draw.circle(
                screen,
                (50, 140, 220),
                (
                    (2150),
                    (1150)
                ),
                (140)
            )

            # =====================================================
            # DRZEWA I KAMIENIE
            # =====================================================

            textures.draw_tree(365, 110)
            textures.draw_rock(900, 150)
            textures.draw_tree(2015, 125)
            textures.draw_rock(1650, 150)
            textures.draw_rock(2315, 125)
            textures.draw_rock(2315, 1000)
            textures.draw_rock(2165, 1300)

            textures.draw_tree(1700, 975)
            textures.draw_tree(300, 975)
            textures.draw_tree(800, 1025)
            textures.draw_tree(500, 1200)

            # =====================================================
            # USTAWIENIE GRACZA I DEMONA - TYLKO RAZ
            # =====================================================

            if not cutscene1_started:
                Player.set_position(
                    -50,
                    settings.HEIGHT // 2 - 100
                )

                demon = Demon(
                    (2700),
                    demon_walk_y
                )

                Player.moving_to_target = False
                Player.walking = False

                demon.moving_to_target = False

                demon_walk_step = 0

                npc_1_alive = True
                npc_2_alive = True
                npc_3_alive = True
                npc_4_alive = True

                demon_taking_npc = False
                demon_take_timer = 0

                demon_escaping = False
                demon_escape_finished = False

                cutscene1_started = True

            # =====================================================
            # FADE IN
            # =====================================================

            if not cutscene1_fade_done:

                cutscene1_fade -= 0.75

                if cutscene1_fade <= 0:
                    cutscene1_fade = 0
                    cutscene1_fade_done = True

            # =====================================================
            # OCZEKIWANIE PO FADE-IN
            # =====================================================

            if cutscene1_fade_done and not cutscene1_wait_done:

                cutscene1_wait -= 1

                if cutscene1_wait <= 0:
                    cutscene1_wait = 0
                    cutscene1_wait_done = True

                    Player.moving_to_target = True
                    demon.moving_to_target = True

            # =====================================================
            # RUCH GRACZA
            # =====================================================

            if cutscene1_wait_done:

                if Player.moving_to_target:
                    Player.move_to(
                        (950),
                        settings.HEIGHT // 2 - (100),
                        3
                    )

            # =====================================================
            # ZABIERANIE NPC
            # =====================================================

            if demon_taking_npc:

                demon_take_timer += 1

                if demon_take_timer >= demon_take_duration:

                    demon_take_timer = 0
                    demon_taking_npc = False

                    # ---------------------------------------------
                    # USUWANIE NPC
                    # ---------------------------------------------

                    if demon_walk_step == 0:

                        npc_4_alive = False

                    elif demon_walk_step == 1:

                        npc_3_alive = False

                    elif demon_walk_step == 2:

                        npc_2_alive = False

                    elif demon_walk_step == 3:

                        npc_1_alive = False

                    # ---------------------------------------------
                    # NASTĘPNE STOISKO
                    # ---------------------------------------------

                    demon_walk_step += 1

                    demon.moving_to_target = True

            # =====================================================
            # UCIECZKA DEMONA
            # =====================================================

            elif demon_escaping:

                demon_reached = demon.move_to(

                    demon_escape_x,

                    demon_walk_y,

                    3

                )

                if demon_reached:
                    demon.moving_to_target = False
                    demon_escaping = False
                    demon_escape_finished = True

                    # =================================================
                    # ZACZYNAMY KOŃCOWE ŚCIEMNIANIE
                    # =================================================

                    cutscene1_end_fade = 0
                    cutscene1_end_fade_done = False

            # =====================================================
            # RUCH DEMONA
            # =====================================================

            elif demon.moving_to_target:

                demon_reached = False

                # =================================================
                # PIERWSZE CHODZENIE - DO ŚRODKA
                # =================================================

                if dialogue_step < 4:

                    demon_reached = demon.move_to(
                        demon_center_x,
                        demon_walk_y,
                        2
                    )

                    if demon_reached:
                        demon.moving_to_target = False
                        dialogue_in_cutsceene1 = True

                # =================================================
                # CHODZENIE PO NPC
                # =================================================

                elif dialogue_step == 5:

                    # =============================================
                    # PRAWE STOISKO
                    # =============================================

                    if demon_walk_step == 0:

                        demon_reached = demon.move_to(
                            demon_npc_4_x,
                            demon_npc_y,
                            2
                        )

                        if demon_reached:
                            demon.moving_to_target = False
                            demon_taking_npc = True
                            demon_take_timer = 0

                    # =============================================
                    # STOISKO 3
                    # =============================================

                    elif demon_walk_step == 1:

                        demon_reached = demon.move_to(
                            demon_npc_3_x,
                            demon_npc_y,
                            2
                        )

                        if demon_reached:
                            demon.moving_to_target = False
                            demon_taking_npc = True
                            demon_take_timer = 0

                    # =============================================
                    # STOISKO 2
                    # =============================================

                    elif demon_walk_step == 2:

                        demon_reached = demon.move_to(
                            demon_npc_2_x,
                            demon_npc_y,
                            2
                        )

                        if demon_reached:
                            demon.moving_to_target = False
                            demon_taking_npc = True
                            demon_take_timer = 0

                    # =============================================
                    # LEWE STOISKO
                    # =============================================

                    elif demon_walk_step == 3:

                        demon_reached = demon.move_to(
                            demon_npc_1_x,
                            demon_npc_y,
                            2
                        )

                        if demon_reached:
                            demon.moving_to_target = False
                            demon_taking_npc = True
                            demon_take_timer = 0

                    # =============================================
                    # WRÓĆ NA ŚRODEK
                    # =============================================

                    elif demon_walk_step == 4:

                        demon_reached = demon.move_to(
                            demon_center_x,
                            demon_walk_y,
                            2
                        )

                        if demon_reached:
                            demon.moving_to_target = False

                            demon_walk_step = 5

                            # -------------------------------------
                            # DALSZY DIALOG
                            # -------------------------------------

                            dialogue_step = 6
                            dialogue_timer = 0

                            draw_multiline_text_with_frame.animation_start = (
                                pygame.time.get_ticks()
                            )

                            last_dialogue_step = 6

            # =====================================================
            # CZARNY EKRAN - FADE
            # =====================================================

            if cutscene1_fade > 0:
                fade_surface = pygame.Surface(
                    (
                        settings.WIDTH,
                        settings.HEIGHT
                    )
                )

                fade_surface.fill((0, 0, 0))

                fade_surface.set_alpha(
                    cutscene1_fade
                )

                screen.blit(
                    fade_surface,
                    (0, 0)
                )

            # =====================================================
            # DIALOGI
            # =====================================================

            if dialogue_in_cutsceene1:

                current_save = data["variables"]["last_save"]

                # =================================================
                # TIMER DIALOGU
                # =================================================

                dialogue_timer += 1

                if dialogue_timer >= 210:

                    # Dialog 7 jest ostatnim dialogiem.
                    # Nie przechodzimy do dialogu 8.
                    if dialogue_step < 7:
                        dialogue_timer = 0

                        # 5 = chodzenie demona
                        if dialogue_step != 5:
                            dialogue_step += 1

                # =================================================
                # ZMIANA DIALOGU
                # =================================================

                if dialogue_step != last_dialogue_step:

                    draw_multiline_text_with_frame.animation_start = (
                        pygame.time.get_ticks()
                    )

                    # =============================================
                    # START CHODZENIA
                    # =============================================

                    if dialogue_step == 5:
                        demon_walk_step = 0

                        demon_taking_npc = False
                        demon_take_timer = 0

                        demon.moving_to_target = True

                    last_dialogue_step = dialogue_step

                # =================================================
                # DIALOG 0
                # =================================================

                if dialogue_step == 0:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            f"< {data['saves'][current_save]['character_name']} >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "Who are you?"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1200)
                        ),
                        animation=True
                    )

                # =================================================
                # DIALOG 1
                # =================================================

                elif dialogue_step == 1:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "< Demon (Aroarente's servant) >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "I'm the Demon. The king of Kingdom",
                            "I will now take the villagers!"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1200)
                        ),
                        animation=True,
                        color=(255, 140, 0)
                    )

                # =================================================
                # DIALOG 2
                # =================================================

                elif dialogue_step == 2:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            f"< {data['saves'][current_save]['character_name']} >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "There's no way",
                            "I'm letting you do that."
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1200)
                        ),
                        animation=True
                    )

                # =================================================
                # DIALOG 3
                # =================================================

                elif dialogue_step == 3:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "< Demon (Aroarente's servant) >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "Then stop me."
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1200)
                        ),
                        animation=True,
                        color=(255, 140, 0)
                    )

                # =================================================
                # DIALOG 6
                # =================================================

                elif dialogue_step == 4:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            f"< {data['saves'][current_save]['character_name']} >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "I got something on me",
                            "what's that? I can't move!",
                            "Take it off me now!"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1250)
                        ),
                        animation=True
                    )

                # =================================================
                # DIALOG 7
                # =================================================

                elif dialogue_step == 5:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "< Demon (Aroarente's servant) >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "Your villagers belong to me now."
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1200)
                        ),
                        animation=True,
                        color=(255, 140, 0)
                    )

                # =================================================
                # DIALOG 8
                # =================================================

                elif dialogue_step == 6:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            f"< {data['saves'][current_save]['character_name']} >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "I won't let you get away with this."
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1200)
                        ),
                        animation=True
                    )

                # =================================================
                # DIALOG 9
                # =================================================

                elif dialogue_step == 7:

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "< Demon (Aroarente's servant) >"
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1050)
                        ),
                        animation=True,
                        color=(45, 45, 55)
                    )

                    draw_multiline_text_with_frame(
                        screen,
                        [
                            "I will be waiting",
                            "for you in my throne."
                        ],
                        font,
                        (
                            (settings.WIDTH // 2),
                            (1200)
                        ),
                        animation=True,
                        color=(255, 140, 0)
                    )

                # =================================================
                # PO OSTATNIM DIALOGU - UCIECZKA
                # =================================================

                if dialogue_step == 7 and dialogue_timer >= 210:
                    dialogue_timer = 0

                    dialogue_in_cutsceene1 = False

                    demon_escaping = True

                    demon.moving_to_target = True

            # =====================================================
            # RYSOWANIE
            # =====================================================

            Player.draw(screen)
            demon.draw(screen)

            # Podczas cutscenki pokazujemy tylko TAB z kłódką.
            # Przyciski E, C i M pozostają ukryte.
            game_ui.draw_locked_toggle(screen, game_game_state)

            # =====================================================
            # KOŃCOWE ŚCIEMNIANIE CUTSCENY
            # =====================================================

            if demon_escape_finished and not cutscene1_end_fade_done:

                cutscene1_end_fade += 2

                if cutscene1_end_fade >= 255:
                    cutscene1_end_fade = 255
                    cutscene1_end_fade_done = True

                    # =============================================
                    # DOPIERO TERAZ PRZECHODZIMY DO GRY
                    # =============================================

                    game_game_state = "game"
                    last_save = data["variables"]["last_save"]
                    data["saves"][last_save]["npc1_alive"] = npc_1_alive
                    data["saves"][last_save]["npc2_alive"] = npc_2_alive
                    data["saves"][last_save]["npc3_alive"] = npc_4_alive
                    data["saves"][last_save]["npc4_alive"] = npc_4_alive
                    save.save_game(data)

                    # Gra zaczyna się całkowicie czarna
                    game_fade = 255
                    game_fade_done = False

                    if data["saves"][last_save]["quest_doing_rn"] == 0:
                        data["saves"][last_save]["quest_doing_rn"] += 1
                    save.save_game(data)

                fade_surface = pygame.Surface(
                    (
                        settings.WIDTH,
                        settings.HEIGHT
                    )
                )

                fade_surface.fill((0, 0, 0))

                fade_surface.set_alpha(
                    int(cutscene1_end_fade)
                )

                screen.blit(
                    fade_surface,
                    (0, 0)
                )

        elif game_game_state == "game":

            last_save = data["variables"]["last_save"]
            if data["saves"][last_save]["cutsceene1_completed"] == False:
                data["saves"][last_save]["cutsceene1_completed"] = True
                save.save_game(data)

            data = save.load_game()
            npc_1_alive = data["saves"][last_save]["npc1_alive"]
            npc_2_alive = data["saves"][last_save]["npc2_alive"]
            npc_3_alive = data["saves"][last_save]["npc3_alive"]
            npc_4_alive = data["saves"][last_save]["npc4_alive"]

            screen.fill((80, 160, 60))

            # =====================================================
            # DROGA — FANTASY RPG
            # Naturalne krawędzie i gładka powierzchnia
            # =====================================================

            road_center_x = settings.WIDTH // 2
            road_center_y = settings.HEIGHT // 2

            # =====================================================
            # KOLORY
            # =====================================================

            road_shadow = (65, 48, 35)
            road_border = (91, 65, 44)
            road_border_mid = (119, 84, 54)
            road_border_light = (143, 103, 66)

            road_base = (153, 112, 73)
            road_surface = (174, 132, 88)
            road_surface_light = (179, 137, 92)

            # =====================================================
            # WYMIARY DROGI
            # =====================================================

            horizontal_top = road_center_y - 260
            horizontal_bottom = road_center_y + 10

            vertical_left = road_center_x - 145
            vertical_right = road_center_x + 125

            junction_left = road_center_x - 315
            junction_right = road_center_x + 315
            junction_top = road_center_y - 425
            junction_bottom = road_center_y + 210

            # =====================================================
            # 1. ZEWNĘTRZNY CIEŃ
            # =====================================================

            # Pozioma część drogi
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    -5,
                    horizontal_top - 5,
                    settings.WIDTH + 10,
                    horizontal_bottom - horizontal_top + 10
                )
            )

            # Pionowa część drogi
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    vertical_left - 5,
                    -5,
                    vertical_right - vertical_left + 10,
                    settings.HEIGHT + 10
                )
            )

            # Skrzyżowanie
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    junction_left - 5,
                    junction_top - 5,
                    junction_right - junction_left + 10,
                    junction_bottom - junction_top + 10
                ),
                border_radius=48
            )

            # =====================================================
            # 2. CIEMNE OBRZEŻE
            # =====================================================

            pygame.draw.rect(
                screen,
                road_border,
                (
                    0,
                    horizontal_top,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top
                )
            )

            pygame.draw.rect(
                screen,
                road_border,
                (
                    vertical_left,
                    0,
                    vertical_right - vertical_left,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_border,
                (
                    junction_left,
                    junction_top,
                    junction_right - junction_left,
                    junction_bottom - junction_top
                ),
                border_radius=44
            )

            # =====================================================
            # 3. WEWNĘTRZNA WARSTWA OBRZEŻA
            # =====================================================

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    0,
                    horizontal_top + 5,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 10
                )
            )

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    vertical_left + 5,
                    0,
                    vertical_right - vertical_left - 10,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    junction_left + 5,
                    junction_top + 5,
                    junction_right - junction_left - 10,
                    junction_bottom - junction_top - 10
                ),
                border_radius=39
            )

            # =====================================================
            # 4. GŁÓWNA POWIERZCHNIA DROGI
            # =====================================================

            pygame.draw.rect(
                screen,
                road_base,
                (
                    0,
                    horizontal_top + 12,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 24
                )
            )

            pygame.draw.rect(
                screen,
                road_base,
                (
                    vertical_left + 12,
                    0,
                    vertical_right - vertical_left - 24,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_base,
                (
                    junction_left + 12,
                    junction_top + 12,
                    junction_right - junction_left - 24,
                    junction_bottom - junction_top - 24
                ),
                border_radius=32
            )

            # =====================================================
            # 5. GŁADKA WARSTWA ŚRODKOWA
            # =====================================================

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    0,
                    horizontal_top + 18,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 36
                )
            )

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    vertical_left + 18,
                    0,
                    vertical_right - vertical_left - 36,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    junction_left + 18,
                    junction_top + 18,
                    junction_right - junction_left - 36,
                    junction_bottom - junction_top - 36
                ),
                border_radius=26
            )

            # =====================================================
            # 6. NATURALNE, ŁAGODNE KRAWĘDZIE
            # =====================================================

            # Delikatne rozjaśnienie górnej krawędzi poziomej drogi.
            # Nie tworzy linii przez środek drogi.

            pygame.draw.rect(
                screen,
                road_border_light,
                (
                    0,
                    horizontal_top + 5,
                    settings.WIDTH,
                    3
                )
            )

            # Delikatne rozjaśnienie lewej krawędzi pionowej drogi.

            pygame.draw.rect(
                screen,
                road_border_light,
                (
                    vertical_left + 5,
                    0,
                    3,
                    settings.HEIGHT
                )
            )

            # =====================================================
            # 7. WYGŁADZENIE POWIERZCHNI SKRZYŻOWANIA
            # =====================================================

            # Jednolita powierzchnia, bez plam i ozdobnych kształtów.

            pygame.draw.rect(
                screen,
                road_surface_light,
                (
                    junction_left + 25,
                    junction_top + 25,
                    junction_right - junction_left - 50,
                    junction_bottom - junction_top - 50
                ),
                border_radius=22
            )

            # Przywrócenie gładkiego koloru na całej powierzchni
            # skrzyżowania, aby nie powstała odrębna plama.

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    junction_left + 29,
                    junction_top + 29,
                    junction_right - junction_left - 58,
                    junction_bottom - junction_top - 58
                ),
                border_radius=19
            )

            # =====================================================
            # 8. KAMIENIE — FANTASY RPG
            # =====================================================

            stone_shadow = (76, 53, 37)
            stone_outline = (101, 72, 49)

            stone_colors = [
                (145, 105, 70),
                (160, 117, 79),
                (173, 132, 91),
                (138, 101, 72),
                (181, 140, 99),
            ]

            stone_highlights = [
                (180, 139, 98),
                (190, 149, 108),
                (170, 130, 91),
            ]

            import random

            # =====================================================
            # 8. KAMIENIE — LOSOWO ROZMIESZCZONE NA DRODZE
            # =====================================================

            # Użyj stałego ziarna, żeby pozycje nie zmieniały się
            # przy każdym wywołaniu rysowania.
            random.seed(42)

            road_stones = []

            stone_count = 65
            stone_w_min, stone_w_max = 20, 30
            stone_h_min, stone_h_max = 10, 15

            for i in range(stone_count):
                stone_w = random.randint(stone_w_min, stone_w_max)
                stone_h = random.randint(stone_h_min, stone_h_max)

                # Wybór części drogi:
                # 0 = pozioma, 1 = pionowa, 2 = skrzyżowanie
                road_part = random.choices(
                    [0, 1, 2],
                    weights=[4, 3, 5],
                    k=1
                )[0]

                if road_part == 0:
                    # Pozioma droga
                    stone_x = random.randint(
                        0,
                        max(0, settings.WIDTH - stone_w)
                    )
                    stone_y = random.randint(
                        horizontal_top,
                        max(horizontal_top, horizontal_bottom - stone_h)
                    )

                elif road_part == 1:
                    # Pionowa droga
                    stone_x = random.randint(
                        vertical_left,
                        max(vertical_left, vertical_right - stone_w)
                    )
                    stone_y = random.randint(
                        0,
                        max(0, settings.HEIGHT - stone_h)
                    )

                else:
                    # Skrzyżowanie
                    stone_x = random.randint(
                        junction_left,
                        max(junction_left, junction_right - stone_w)
                    )
                    stone_y = random.randint(
                        junction_top,
                        max(junction_top, junction_bottom - stone_h)
                    )

                variant = random.randrange(5)

                road_stones.append(
                    (stone_x, stone_y, stone_w, stone_h, variant)
                )

            # Nieregularne kształty kamieni
            stone_shapes = [
                [
                    (0.08, 0.35), (0.27, 0.06), (0.68, 0.02),
                    (0.96, 0.30), (0.88, 0.72), (0.61, 0.96),
                    (0.20, 0.86), (0.02, 0.57)
                ],
                [
                    (0.04, 0.28), (0.38, 0.02), (0.79, 0.12),
                    (0.98, 0.48), (0.77, 0.91), (0.35, 0.98),
                    (0.06, 0.70)
                ],
                [
                    (0.15, 0.05), (0.75, 0.03), (0.99, 0.42),
                    (0.83, 0.81), (0.48, 0.98), (0.10, 0.76),
                    (0.01, 0.36)
                ],
            ]

            # Rysowanie kamieni
            for i, (stone_x, stone_y, stone_w, stone_h, variant) in enumerate(road_stones):

                if not (
                        -stone_w <= stone_x < settings.WIDTH
                        and -stone_h <= stone_y < settings.HEIGHT
                ):
                    continue

                shape = stone_shapes[i % len(stone_shapes)]

                points = [
                    (
                        int(stone_x + px * stone_w),
                        int(stone_y + py * stone_h)
                    )
                    for px, py in shape
                ]

                # Cień
                pygame.draw.polygon(
                    screen,
                    stone_shadow,
                    [(x + 2, y + 2) for x, y in points]
                )

                # Kontur
                pygame.draw.polygon(
                    screen,
                    stone_outline,
                    points
                )

                # Powierzchnia
                inset_points = [
                    (
                        int(stone_x + (x - stone_x) * 0.86),
                        int(stone_y + (y - stone_y) * 0.76 + stone_h * 0.10)
                    )
                    for x, y in points
                ]

                pygame.draw.polygon(
                    screen,
                    stone_colors[variant % len(stone_colors)],
                    inset_points
                )

                # Delikatny refleks
                highlight_points = [
                    (
                        int(stone_x + px * stone_w * 0.65 + stone_w * 0.10),
                        int(stone_y + py * stone_h * 0.40 + stone_h * 0.10)
                    )
                    for px, py in shape[:3]
                ]

                pygame.draw.polygon(
                    screen,
                    stone_highlights[variant % len(stone_highlights)],
                    highlight_points
                )

            # STALLS
            if npc_1_alive:
                textures.draw_npc(810, 370, (50, 140, 70))
            textures.draw_stall(800, 340, (170, 50, 50))
            if npc_2_alive:
                textures.draw_npc(310, 370, (180, 50, 50))
            textures.draw_stall(300, 340, (220, 170, 50))
            if npc_3_alive:
                textures.draw_npc(1810, 370, (220, 170, 50))
            textures.draw_stall(1800, 340, (50, 140, 70))
            if npc_4_alive:
                textures.draw_npc(2310, 370, (130, 60, 160))
            textures.draw_stall(2300, 340, (50, 90, 180))

            # LAKE
            pygame.draw.circle(
                screen,
                (50, 140, 220),
                ((2000), (1000)),
                (200)
            )

            pygame.draw.circle(
                screen,
                (50, 140, 220),
                ((2150), (1150)),
                (140)
            )

            # TREES AND ROCKS
            textures.draw_tree(365, 110)
            textures.draw_rock(900, 150)
            textures.draw_tree(2015, 125)
            textures.draw_rock(1650, 150)
            textures.draw_rock(2315, 125)
            textures.draw_rock(2315, 1000)
            textures.draw_rock(2165, 1300)
            textures.draw_tree(1700, 975)
            textures.draw_tree(300, 975)
            textures.draw_tree(800, 1025)
            textures.draw_tree(500, 1200)

            # Zwykły ruch gracza jest dostępny tylko podczas gry.
            # Ruch skryptowy Player.move_to() w cutscence pozostaje bez zmian.
            if game_game_state == "game":
                Player.move()
            else:
                Player.walking = False

            Player.draw(screen)

            game_ui.draw(screen, game_game_state)

            # =====================================================
            # ROZJAŚNIANIE PO UCIECZCE DEMONA
            # =====================================================

            if not game_fade_done:

                game_fade -= 0.5

                if game_fade <= 0:
                    game_fade = 0
                    game_fade_done = True

                fade_surface = pygame.Surface(
                    (
                        settings.WIDTH,
                        settings.HEIGHT
                    )
                )

                fade_surface.fill((0, 0, 0))

                fade_surface.set_alpha(
                    int(game_fade)
                )

                screen.blit(
                    fade_surface,
                    (0, 0)
                )

            # =====================================================
            # ROZJAŚNIANIE PO UCIECZCE DEMONA
            # =====================================================

            if not game_fade_done:

                game_fade -= 0.75

                if game_fade <= 0:
                    game_fade = 0
                    game_fade_done = True

                fade_surface = pygame.Surface(
                    (
                        settings.WIDTH,
                        settings.HEIGHT
                    )
                )

                fade_surface.fill((0, 0, 0))

                fade_surface.set_alpha(
                    int(game_fade)
                )

                screen.blit(
                    fade_surface,
                    (0, 0)
                )

        elif game_game_state == "pvp":
            pass

        else:
            last_save = data["variables"]["last_save"]
            if data["saves"][last_save]["cutsceene1_completed"] == False:
                data["saves"][last_save]["cutsceene1_completed"] = True
                save.save_game(data)

            data = save.load_game()
            npc_1_alive = data["saves"][last_save]["npc1_alive"]
            npc_2_alive = data["saves"][last_save]["npc2_alive"]
            npc_3_alive = data["saves"][last_save]["npc3_alive"]
            npc_4_alive = data["saves"][last_save]["npc4_alive"]

            screen.fill((80, 160, 60))

            # =====================================================
            # DROGA — FANTASY RPG
            # Naturalne krawędzie i gładka powierzchnia
            # =====================================================

            road_center_x = settings.WIDTH // 2
            road_center_y = settings.HEIGHT // 2

            # =====================================================
            # KOLORY
            # =====================================================

            road_shadow = (65, 48, 35)
            road_border = (91, 65, 44)
            road_border_mid = (119, 84, 54)
            road_border_light = (143, 103, 66)

            road_base = (153, 112, 73)
            road_surface = (174, 132, 88)
            road_surface_light = (179, 137, 92)

            # =====================================================
            # WYMIARY DROGI
            # =====================================================

            horizontal_top = road_center_y - 260
            horizontal_bottom = road_center_y + 10

            vertical_left = road_center_x - 145
            vertical_right = road_center_x + 125

            junction_left = road_center_x - 315
            junction_right = road_center_x + 315
            junction_top = road_center_y - 425
            junction_bottom = road_center_y + 210

            # =====================================================
            # 1. ZEWNĘTRZNY CIEŃ
            # =====================================================

            # Pozioma część drogi
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    -5,
                    horizontal_top - 5,
                    settings.WIDTH + 10,
                    horizontal_bottom - horizontal_top + 10
                )
            )

            # Pionowa część drogi
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    vertical_left - 5,
                    -5,
                    vertical_right - vertical_left + 10,
                    settings.HEIGHT + 10
                )
            )

            # Skrzyżowanie
            pygame.draw.rect(
                screen,
                road_shadow,
                (
                    junction_left - 5,
                    junction_top - 5,
                    junction_right - junction_left + 10,
                    junction_bottom - junction_top + 10
                ),
                border_radius=48
            )

            # =====================================================
            # 2. CIEMNE OBRZEŻE
            # =====================================================

            pygame.draw.rect(
                screen,
                road_border,
                (
                    0,
                    horizontal_top,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top
                )
            )

            pygame.draw.rect(
                screen,
                road_border,
                (
                    vertical_left,
                    0,
                    vertical_right - vertical_left,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_border,
                (
                    junction_left,
                    junction_top,
                    junction_right - junction_left,
                    junction_bottom - junction_top
                ),
                border_radius=44
            )

            # =====================================================
            # 3. WEWNĘTRZNA WARSTWA OBRZEŻA
            # =====================================================

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    0,
                    horizontal_top + 5,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 10
                )
            )

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    vertical_left + 5,
                    0,
                    vertical_right - vertical_left - 10,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_border_mid,
                (
                    junction_left + 5,
                    junction_top + 5,
                    junction_right - junction_left - 10,
                    junction_bottom - junction_top - 10
                ),
                border_radius=39
            )

            # =====================================================
            # 4. GŁÓWNA POWIERZCHNIA DROGI
            # =====================================================

            pygame.draw.rect(
                screen,
                road_base,
                (
                    0,
                    horizontal_top + 12,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 24
                )
            )

            pygame.draw.rect(
                screen,
                road_base,
                (
                    vertical_left + 12,
                    0,
                    vertical_right - vertical_left - 24,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_base,
                (
                    junction_left + 12,
                    junction_top + 12,
                    junction_right - junction_left - 24,
                    junction_bottom - junction_top - 24
                ),
                border_radius=32
            )

            # =====================================================
            # 5. GŁADKA WARSTWA ŚRODKOWA
            # =====================================================

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    0,
                    horizontal_top + 18,
                    settings.WIDTH,
                    horizontal_bottom - horizontal_top - 36
                )
            )

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    vertical_left + 18,
                    0,
                    vertical_right - vertical_left - 36,
                    settings.HEIGHT
                )
            )

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    junction_left + 18,
                    junction_top + 18,
                    junction_right - junction_left - 36,
                    junction_bottom - junction_top - 36
                ),
                border_radius=26
            )

            # =====================================================
            # 6. NATURALNE, ŁAGODNE KRAWĘDZIE
            # =====================================================

            # Delikatne rozjaśnienie górnej krawędzi poziomej drogi.
            # Nie tworzy linii przez środek drogi.

            pygame.draw.rect(
                screen,
                road_border_light,
                (
                    0,
                    horizontal_top + 5,
                    settings.WIDTH,
                    3
                )
            )

            # Delikatne rozjaśnienie lewej krawędzi pionowej drogi.

            pygame.draw.rect(
                screen,
                road_border_light,
                (
                    vertical_left + 5,
                    0,
                    3,
                    settings.HEIGHT
                )
            )

            # =====================================================
            # 7. WYGŁADZENIE POWIERZCHNI SKRZYŻOWANIA
            # =====================================================

            # Jednolita powierzchnia, bez plam i ozdobnych kształtów.

            pygame.draw.rect(
                screen,
                road_surface_light,
                (
                    junction_left + 25,
                    junction_top + 25,
                    junction_right - junction_left - 50,
                    junction_bottom - junction_top - 50
                ),
                border_radius=22
            )

            # Przywrócenie gładkiego koloru na całej powierzchni
            # skrzyżowania, aby nie powstała odrębna plama.

            pygame.draw.rect(
                screen,
                road_surface,
                (
                    junction_left + 29,
                    junction_top + 29,
                    junction_right - junction_left - 58,
                    junction_bottom - junction_top - 58
                ),
                border_radius=19
            )

            # =====================================================
            # 8. KAMIENIE — FANTASY RPG
            # =====================================================

            stone_shadow = (76, 53, 37)
            stone_outline = (101, 72, 49)

            stone_colors = [
                (145, 105, 70),
                (160, 117, 79),
                (173, 132, 91),
                (138, 101, 72),
                (181, 140, 99),
            ]

            stone_highlights = [
                (180, 139, 98),
                (190, 149, 108),
                (170, 130, 91),
            ]

            import random

            # =====================================================
            # 8. KAMIENIE — LOSOWO ROZMIESZCZONE NA DRODZE
            # =====================================================

            # Użyj stałego ziarna, żeby pozycje nie zmieniały się
            # przy każdym wywołaniu rysowania.
            random.seed(42)

            road_stones = []

            stone_count = 65
            stone_w_min, stone_w_max = 20, 30
            stone_h_min, stone_h_max = 10, 15

            for i in range(stone_count):
                stone_w = random.randint(stone_w_min, stone_w_max)
                stone_h = random.randint(stone_h_min, stone_h_max)

                # Wybór części drogi:
                # 0 = pozioma, 1 = pionowa, 2 = skrzyżowanie
                road_part = random.choices(
                    [0, 1, 2],
                    weights=[4, 3, 5],
                    k=1
                )[0]

                if road_part == 0:
                    # Pozioma droga
                    stone_x = random.randint(
                        0,
                        max(0, settings.WIDTH - stone_w)
                    )
                    stone_y = random.randint(
                        horizontal_top,
                        max(horizontal_top, horizontal_bottom - stone_h)
                    )

                elif road_part == 1:
                    # Pionowa droga
                    stone_x = random.randint(
                        vertical_left,
                        max(vertical_left, vertical_right - stone_w)
                    )
                    stone_y = random.randint(
                        0,
                        max(0, settings.HEIGHT - stone_h)
                    )

                else:
                    # Skrzyżowanie
                    stone_x = random.randint(
                        junction_left,
                        max(junction_left, junction_right - stone_w)
                    )
                    stone_y = random.randint(
                        junction_top,
                        max(junction_top, junction_bottom - stone_h)
                    )

                variant = random.randrange(5)

                road_stones.append(
                    (stone_x, stone_y, stone_w, stone_h, variant)
                )

            # Nieregularne kształty kamieni
            stone_shapes = [
                [
                    (0.08, 0.35), (0.27, 0.06), (0.68, 0.02),
                    (0.96, 0.30), (0.88, 0.72), (0.61, 0.96),
                    (0.20, 0.86), (0.02, 0.57)
                ],
                [
                    (0.04, 0.28), (0.38, 0.02), (0.79, 0.12),
                    (0.98, 0.48), (0.77, 0.91), (0.35, 0.98),
                    (0.06, 0.70)
                ],
                [
                    (0.15, 0.05), (0.75, 0.03), (0.99, 0.42),
                    (0.83, 0.81), (0.48, 0.98), (0.10, 0.76),
                    (0.01, 0.36)
                ],
            ]

            # Rysowanie kamieni
            for i, (stone_x, stone_y, stone_w, stone_h, variant) in enumerate(road_stones):

                if not (
                        -stone_w <= stone_x < settings.WIDTH
                        and -stone_h <= stone_y < settings.HEIGHT
                ):
                    continue

                shape = stone_shapes[i % len(stone_shapes)]

                points = [
                    (
                        int(stone_x + px * stone_w),
                        int(stone_y + py * stone_h)
                    )
                    for px, py in shape
                ]

                # Cień
                pygame.draw.polygon(
                    screen,
                    stone_shadow,
                    [(x + 2, y + 2) for x, y in points]
                )

                # Kontur
                pygame.draw.polygon(
                    screen,
                    stone_outline,
                    points
                )

                # Powierzchnia
                inset_points = [
                    (
                        int(stone_x + (x - stone_x) * 0.86),
                        int(stone_y + (y - stone_y) * 0.76 + stone_h * 0.10)
                    )
                    for x, y in points
                ]

                pygame.draw.polygon(
                    screen,
                    stone_colors[variant % len(stone_colors)],
                    inset_points
                )

                # Delikatny refleks
                highlight_points = [
                    (
                        int(stone_x + px * stone_w * 0.65 + stone_w * 0.10),
                        int(stone_y + py * stone_h * 0.40 + stone_h * 0.10)
                    )
                    for px, py in shape[:3]
                ]

                pygame.draw.polygon(
                    screen,
                    stone_highlights[variant % len(stone_highlights)],
                    highlight_points
                )

            # STALLS
            if npc_1_alive:
                textures.draw_npc(810, 370, (50, 140, 70))
            textures.draw_stall(800, 340, (170, 50, 50))
            if npc_2_alive:
                textures.draw_npc(310, 370, (180, 50, 50))
            textures.draw_stall(300, 340, (220, 170, 50))
            if npc_3_alive:
                textures.draw_npc(1810, 370, (220, 170, 50))
            textures.draw_stall(1800, 340, (50, 140, 70))
            if npc_4_alive:
                textures.draw_npc(2310, 370, (130, 60, 160))
            textures.draw_stall(2300, 340, (50, 90, 180))

            # LAKE
            pygame.draw.circle(
                screen,
                (50, 140, 220),
                ((2000), (1000)),
                (200)
            )

            pygame.draw.circle(
                screen,
                (50, 140, 220),
                ((2150), (1150)),
                (140)
            )

            # TREES AND ROCKS
            textures.draw_tree(365, 110)
            textures.draw_rock(900, 150)
            textures.draw_tree(2015, 125)
            textures.draw_rock(1650, 150)
            textures.draw_rock(2315, 125)
            textures.draw_rock(2315, 1000)
            textures.draw_rock(2165, 1300)
            textures.draw_tree(1700, 975)
            textures.draw_tree(300, 975)
            textures.draw_tree(800, 1025)
            textures.draw_tree(500, 1200)

            # Zwykły ruch gracza jest dostępny tylko podczas gry.
            # Ruch skryptowy Player.move_to() w cutscence pozostaje bez zmian.
            if game_game_state == "game":
                Player.move()
            else:
                Player.walking = False

            Player.draw(screen)

            game_ui.draw(screen, game_game_state)

            # =====================================================
            # ROZJAŚNIANIE PO UCIECZCE DEMONA
            # =====================================================

            if not game_fade_done:

                game_fade -= 0.5

                if game_fade <= 0:
                    game_fade = 0
                    game_fade_done = True

                fade_surface = pygame.Surface(
                    (
                        settings.WIDTH,
                        settings.HEIGHT
                    )
                )

                fade_surface.fill((0, 0, 0))

                fade_surface.set_alpha(
                    int(game_fade)
                )

                screen.blit(
                    fade_surface,
                    (0, 0)
                )

            # =====================================================
            # ROZJAŚNIANIE PO UCIECZCE DEMONA
            # =====================================================

            if not game_fade_done:

                game_fade -= 0.75

                if game_fade <= 0:
                    game_fade = 0
                    game_fade_done = True

                fade_surface = pygame.Surface(
                    (
                        settings.WIDTH,
                        settings.HEIGHT
                    )
                )

                fade_surface.fill((0, 0, 0))

                fade_surface.set_alpha(
                    int(game_fade)
                )

                screen.blit(
                    fade_surface,
                    (0, 0)
                )

    pygame.display.flip()

pygame.quit()
sys.exit()

#LOOP
