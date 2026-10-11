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

class Elementals:
    def __init__(self, name, eqquiped, v1_energy_drain, v2_energy_drain, v3_energy_drain, v1_dmg, v2_dmg, v3_dmg, v1_name, v2_name, v3_name):
        self.name = name
        self.eqquiped = eqquiped

        self.v1_energy_drain = v1_energy_drain
        self.v2_energy_drain = v2_energy_drain
        self.v3_energy_drain = v3_energy_drain

        self.v1_name = v1_name
        self.v2_name = v2_name
        self.v3_name = v3_name

        self.v1_dmg = v1_dmg
        self.v2_dmg = v2_dmg
        self.v3_dmg = v3_dmg

class Fire(Elementals):
    def __init__(self):
        super().__init__(
            name="Fire",
            eqquiped=False,
            v1_energy_drain=10, #ZMIEŃ <
            v2_energy_drain=20,
            v3_energy_drain=30,
            v1_dmg=10,
            v2_dmg=15,
            v3_dmg=20,          #ZMIEŃ >
            v1_name="Fire Flames",
            v2_name="Flame Strike",
            v3_name="Fire Aspect"
        )

    def attack(self, target, player, v):
        if v == 1:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain
        elif v == 2:
            dmg = self.v2_dmg
            energy_drain = self.v2_energy_drain
        elif v == 3:
            dmg = self.v3_dmg
            energy_drain = self.v3_energy_drain
        else:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain

        # Zabierz energię
        player.energy -= energy_drain

        # Zadaj obrażenia
        target.hp -= dmg
        if target.hp < target.max_hp:
            target.hp = target.max_hp

    def draw_v1_icon(self, screen, center_x, center_y):
        # ==========================================
        # DUŻY, DOPRACOWANY PŁOMIEŃ — V1
        # ==========================================

        # Poświata za płomieniem
        glow_surface = pygame.Surface(
            (100, 100),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            glow_surface,
            (255, 75, 10, 25),
            (50, 50),
            35
        )

        pygame.draw.circle(
            glow_surface,
            (255, 110, 15, 35),
            (50, 50),
            25
        )

        screen.blit(
            glow_surface,
            (center_x - 50, center_y - 50)
        )

        # ==========================================
        # ZEWNĘTRZNY PŁOMIEŃ
        # ==========================================

        outer_flame = [
            (center_x, center_y - 32),
            (center_x + 5, center_y - 23),
            (center_x + 8, center_y - 15),
            (center_x + 17, center_y - 22),
            (center_x + 16, center_y - 9),
            (center_x + 24, center_y - 1),
            (center_x + 23, center_y + 10),
            (center_x + 17, center_y + 20),
            (center_x + 8, center_y + 26),
            (center_x, center_y + 29),
            (center_x - 10, center_y + 25),
            (center_x - 19, center_y + 18),
            (center_x - 24, center_y + 7),
            (center_x - 22, center_y - 4),
            (center_x - 15, center_y - 13),
            (center_x - 13, center_y - 23),
            (center_x - 5, center_y - 16),
        ]

        pygame.draw.polygon(
            screen,
            (125, 25, 12),
            outer_flame
        )

        # Główna warstwa ognia
        main_flame = [
            (center_x, center_y - 28),
            (center_x + 5, center_y - 17),
            (center_x + 7, center_y - 8),
            (center_x + 15, center_y - 14),
            (center_x + 13, center_y - 2),
            (center_x + 19, center_y + 7),
            (center_x + 13, center_y + 18),
            (center_x, center_y + 25),
            (center_x - 13, center_y + 17),
            (center_x - 18, center_y + 7),
            (center_x - 13, center_y - 3),
            (center_x - 8, center_y - 13),
            (center_x - 5, center_y - 5),
        ]

        pygame.draw.polygon(
            screen,
            (235, 55, 12),
            main_flame
        )

        # ==========================================
        # JASNY, POMARAŃCZOWY ŚRODEK
        # ==========================================

        orange_flame = [
            (center_x - 1, center_y + 20),
            (center_x - 9, center_y + 13),
            (center_x - 10, center_y + 5),
            (center_x - 5, center_y - 3),
            (center_x - 3, center_y + 3),
            (center_x + 3, center_y - 7),
            (center_x + 5, center_y + 1),
            (center_x + 11, center_y + 7),
            (center_x + 7, center_y + 15),
        ]

        pygame.draw.polygon(
            screen,
            (255, 125, 15),
            orange_flame
        )

        # ==========================================
        # ŻÓŁTY ŚRODEK
        # ==========================================

        yellow_flame = [
            (center_x, center_y + 19),
            (center_x - 5, center_y + 13),
            (center_x - 4, center_y + 7),
            (center_x, center_y + 1),
            (center_x + 2, center_y + 8),
            (center_x + 6, center_y + 12),
            (center_x + 4, center_y + 16),
        ]

        pygame.draw.polygon(
            screen,
            (255, 210, 65),
            yellow_flame
        )

        # Najjaśniejszy punkt ognia
        pygame.draw.polygon(
            screen,
            (255, 245, 175),
            [
                (center_x, center_y + 17),
                (center_x - 2, center_y + 12),
                (center_x, center_y + 7),
                (center_x + 3, center_y + 13),
            ]
        )

        # ==========================================
        # MAŁE PŁOMYKI WOKÓŁ GŁÓWNEGO OGNIA
        # ==========================================

        small_flames = [
            # Lewy górny płomyk
            (-27, -19, 7, 13, (255, 100, 15)),

            # Prawy górny płomyk
            (25, -20, 7, 14, (255, 135, 20)),

            # Lewy środkowy płomyk
            (-30, -3, 6, 11, (255, 75, 10)),

            # Prawy środkowy płomyk
            (29, 1, 6, 12, (255, 110, 15)),

            # Lewy dolny płomyk
            (-25, 16, 5, 9, (220, 55, 10)),

            # Prawy dolny płomyk
            (25, 17, 5, 9, (235, 75, 10)),
        ]

        for offset_x, offset_y, width, height, color in small_flames:
            flame_x = center_x + offset_x
            flame_y = center_y + offset_y

            points = [
                (flame_x, flame_y - height),
                (flame_x + width // 2, flame_y - height // 3),
                (flame_x + width // 2, flame_y + height // 3),
                (flame_x, flame_y + height // 2),
                (flame_x - width // 2, flame_y + height // 3),
                (flame_x - width // 2, flame_y - height // 3),
            ]

            pygame.draw.polygon(
                screen,
                color,
                points
            )

    def draw_v2_icon(self, screen, center_x, center_y):
        # ==========================================
        # FIREBALL — V2 ULTIMATE
        # ==========================================

        import math
        import pygame

        # Wszystkie pozycje są liczone względem środka ikony.
        # Dzięki temu można ją rysować w dowolnym miejscu.

        # ==========================================
        # 1. MIĘKKA POŚWIATA
        # ==========================================

        glow_size = 100
        glow = pygame.Surface(
            (glow_size, glow_size),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            glow,
            (255, 45, 0, 18),
            (50, 50),
            47
        )

        pygame.draw.circle(
            glow,
            (255, 85, 0, 28),
            (50, 50),
            36
        )

        pygame.draw.circle(
            glow,
            (255, 150, 15, 35),
            (50, 50),
            25
        )

        screen.blit(
            glow,
            (center_x - 50, center_y - 50)
        )

        # ==========================================
        # 2. OGON OGNIA
        # ==========================================

        # Ciemna warstwa zewnętrzna
        pygame.draw.polygon(
            screen,
            (105, 20, 12),
            [
                (center_x - 8, center_y + 8),
                (center_x - 23, center_y + 24),
                (center_x - 17, center_y + 8),
                (center_x - 32, center_y + 13),
                (center_x - 24, center_y - 2),
                (center_x - 36, center_y + 1),
                (center_x - 23, center_y - 13),
                (center_x - 13, center_y - 15),
            ]
        )

        # Główny ogon
        pygame.draw.polygon(
            screen,
            (225, 45, 8),
            [
                (center_x - 8, center_y + 7),
                (center_x - 25, center_y + 20),
                (center_x - 18, center_y + 7),
                (center_x - 28, center_y + 10),
                (center_x - 20, center_y - 2),
                (center_x - 30, center_y + 1),
                (center_x - 19, center_y - 11),
                (center_x - 8, center_y - 10),
            ]
        )

        # Jasny pas wewnątrz ogona
        pygame.draw.polygon(
            screen,
            (255, 105, 12),
            [
                (center_x - 10, center_y + 5),
                (center_x - 22, center_y + 13),
                (center_x - 15, center_y + 4),
                (center_x - 23, center_y + 3),
                (center_x - 13, center_y - 6),
                (center_x - 5, center_y - 6),
            ]
        )

        # ==========================================
        # 3. PŁOMIENIE WOKÓŁ KULI
        # ==========================================

        # Zewnętrzna sylwetka płomieni
        pygame.draw.polygon(
            screen,
            (120, 22, 8),
            [
                (center_x - 14, center_y - 8),
                (center_x - 22, center_y - 24),
                (center_x - 10, center_y - 19),
                (center_x - 7, center_y - 32),
                (center_x + 2, center_y - 23),
                (center_x + 10, center_y - 29),
                (center_x + 12, center_y - 17),
                (center_x + 27, center_y - 19),
                (center_x + 20, center_y - 5),
                (center_x + 29, center_y + 2),
                (center_x + 20, center_y + 9),
                (center_x + 17, center_y + 20),
                (center_x + 3, center_y + 24),
                (center_x - 12, center_y + 20),
                (center_x - 25, center_y + 10),
                (center_x - 28, center_y - 1),
            ]
        )

        # Właściwy ogień
        pygame.draw.polygon(
            screen,
            (245, 55, 8),
            [
                (center_x - 12, center_y - 7),
                (center_x - 19, center_y - 20),
                (center_x - 9, center_y - 15),
                (center_x - 5, center_y - 27),
                (center_x + 3, center_y - 17),
                (center_x + 11, center_y - 24),
                (center_x + 12, center_y - 12),
                (center_x + 22, center_y - 15),
                (center_x + 17, center_y - 3),
                (center_x + 24, center_y + 3),
                (center_x + 17, center_y + 11),
                (center_x + 13, center_y + 18),
                (center_x, center_y + 22),
                (center_x - 12, center_y + 16),
                (center_x - 21, center_y + 8),
                (center_x - 23, center_y),
            ]
        )

        # Dodatkowy płomień z lewej
        pygame.draw.polygon(
            screen,
            (255, 105, 10),
            [
                (center_x - 12, center_y - 4),
                (center_x - 20, center_y - 16),
                (center_x - 17, center_y - 4),
                (center_x - 21, center_y + 2),
                (center_x - 12, center_y + 4),
            ]
        )

        # Dodatkowy płomień z prawej
        pygame.draw.polygon(
            screen,
            (255, 125, 12),
            [
                (center_x + 13, center_y - 7),
                (center_x + 23, center_y - 13),
                (center_x + 19, center_y - 3),
                (center_x + 24, center_y + 1),
                (center_x + 15, center_y + 5),
            ]
        )

        # ==========================================
        # 4. CIEMNY KONTUR KULI
        # ==========================================

        pygame.draw.circle(
            screen,
            (105, 22, 8),
            (center_x, center_y),
            18
        )

        # Zewnętrzna pomarańczowa warstwa
        pygame.draw.circle(
            screen,
            (240, 65, 8),
            (center_x, center_y),
            16
        )

        # ==========================================
        # 5. ROZŻARZONA POWŁOKA
        # ==========================================

        pygame.draw.circle(
            screen,
            (255, 115, 10),
            (center_x - 1, center_y - 1),
            13
        )

        pygame.draw.circle(
            screen,
            (255, 165, 25),
            (center_x - 2, center_y - 3),
            10
        )

        # Asymetryczne rozżarzone obszary
        pygame.draw.ellipse(
            screen,
            (255, 205, 55),
            (
                center_x - 9,
                center_y - 10,
                13,
                15
            )
        )

        pygame.draw.ellipse(
            screen,
            (255, 225, 100),
            (
                center_x - 5,
                center_y - 8,
                9,
                12
            )
        )

        # ==========================================
        # 6. BIAŁO-ŻÓŁTY GORĄCY RDZEŃ
        # ==========================================

        pygame.draw.polygon(
            screen,
            (255, 240, 160),
            [
                (center_x - 4, center_y - 8),
                (center_x + 2, center_y - 5),
                (center_x + 4, center_y),
                (center_x + 1, center_y + 5),
                (center_x - 4, center_y + 3),
                (center_x - 6, center_y - 2),
            ]
        )

        pygame.draw.circle(
            screen,
            (255, 255, 220),
            (center_x - 4, center_y - 6),
            2
        )

        # ==========================================
        # 7. ISKRY WOKÓŁ FIREBALLA
        # ==========================================

        sparks = [
            (-29, -20, 2, (255, 190, 45)),
            (28, -24, 2, (255, 225, 100)),
            (30, 12, 2, (255, 115, 20)),
            (-26, 19, 2, (255, 145, 25)),
            (4, -35, 2, (255, 210, 75)),
            (-35, -5, 1, (255, 225, 130)),
            (23, 25, 1, (255, 180, 40)),
        ]

        for offset_x, offset_y, radius, color in sparks:
            pygame.draw.circle(
                screen,
                color,
                (
                    center_x + offset_x,
                    center_y + offset_y
                ),
                radius
            )

    def draw_v1(self, screen):
        pass

    def draw_v2(self, screen):
        pass

    def draw_v3(self, screen):
        pass

class Water(Elementals):
    def __init__(self):
        super().__init__(
            name="Water",
            eqquiped=False,
            v1_energy_drain=10, #ZMIEŃ <
            v2_energy_drain=20,
            v3_energy_drain=30,
            v1_dmg=10,
            v2_dmg=15,
            v3_dmg=20,          #ZMIEŃ >
            v1_name="Aqua Barrage",
            v2_name="Tsunami",
            v3_name="Drowning Orbs"
        )

    def attack(self, target, player, v):
        if v == 1:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain
        elif v == 2:
            dmg = self.v2_dmg
            energy_drain = self.v2_energy_drain
        elif v == 3:
            dmg = self.v3_dmg
            energy_drain = self.v3_energy_drain
        else:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain

        # Zabierz energię
        player.energy -= energy_drain

        # Zadaj obrażenia
        target.hp -= dmg
        if target.hp < target.max_hp:
            target.hp = target.max_hp

    def draw_v1_icon(self, screen, center_x, center_y):
        # ==========================================
        # KILKA ATAKUJĄCYCH KROPLI WODY — V1
        # ==========================================

        glow_surface = pygame.Surface((100, 100), pygame.SRCALPHA)

        pygame.draw.circle(
            glow_surface,
            (20, 140, 255, 30),
            (50, 50),
            35
        )

        pygame.draw.circle(
            glow_surface,
            (60, 210, 255, 40),
            (50, 50),
            25
        )

        screen.blit(
            glow_surface,
            (center_x - 50, center_y - 50)
        )

        # ==========================================
        # POZYCJE KROPLI WODY
        # ==========================================

        droplets = [
            (-19, -19, 9, 15),
            (2, -25, 10, 17),
            (22, -14, 9, 15),
            (-25, 3, 10, 16),
            (-7, 0, 11, 18),
            (15, 5, 10, 17),
            (-15, 23, 8, 13),
            (8, 24, 9, 14),
            (29, 21, 7, 12),
        ]

        # ==========================================
        # RYSOWANIE KROPLI
        # ==========================================

        for offset_x, offset_y, width, height in droplets:
            x = center_x + offset_x
            y = center_y + offset_y

            # Ciemna obwódka / cień
            pygame.draw.ellipse(
                screen,
                (10, 65, 145),
                (
                    x - width // 2 - 2,
                    y - height // 2 - 2,
                    width + 4,
                    height + 4
                )
            )

            # Główna kropla
            pygame.draw.ellipse(
                screen,
                (20, 145, 235),
                (
                    x - width // 2,
                    y - height // 2,
                    width,
                    height
                )
            )

            # Jasny turkusowy środek
            pygame.draw.ellipse(
                screen,
                (55, 210, 255),
                (
                    x - width // 3,
                    y - height // 3,
                    max(3, width * 2 // 3),
                    max(4, height * 2 // 3)
                )
            )

            # Biały refleks światła
            pygame.draw.circle(
                screen,
                (225, 250, 255),
                (
                    x - 1,
                    y - height // 6
                ),
                2
            )

            # Mały błękitny refleks
            pygame.draw.circle(
                screen,
                (145, 230, 255),
                (
                    x + 2,
                    y + height // 5
                ),
                1
            )

    def draw_v2_icon(self, screen, center_x, center_y):
        # =====================================================
        # TSUNAMI V12 — SMALLER + LOWER WAVE TIP
        # =====================================================

        import pygame
        import math

        icon_size = 92
        wave_offset_y = 8

        # =====================================================
        # 1. POŚWIATA
        # =====================================================

        glow = pygame.Surface((110, 110), pygame.SRCALPHA)

        pygame.draw.circle(
            glow,
            (0, 100, 255, 22),
            (55, 55),
            44
        )

        pygame.draw.circle(
            glow,
            (0, 160, 255, 28),
            (55, 55),
            34
        )

        pygame.draw.circle(
            glow,
            (60, 220, 255, 35),
            (55, 55),
            24
        )

        screen.blit(
            glow,
            (center_x - 55, center_y - 55 + wave_offset_y)
        )

        # =====================================================
        # 2. GŁÓWNA POWIERZCHNIA FALI
        # =====================================================

        water = pygame.Surface((150, 150), pygame.SRCALPHA)

        wave_points = [
            (4, 119),
            (15, 112),
            (27, 101),
            (38, 86),
            (46, 67),
            (52, 47),
            (61, 29),
            (73, 17),
            (85, 13),
            (97, 17),
            (108, 25),
            (119, 37),
            (130, 47),
            (139, 51),

            # Zawinięty szczyt
            (136, 57),
            (127, 57),
            (119, 51),
            (111, 44),
            (103, 37),
            (95, 33),
            (87, 34),
            (81, 41),
            (76, 53),
            (72, 69),
            (70, 84),

            # Końcówka fali opadająca niżej
            (78, 96),
            (91, 106),
            (107, 115),
            (125, 122),
            (143, 126),
            (137, 130),
            (116, 132),
            (90, 132),
            (62, 130),
            (37, 127),
            (17, 123),
            (4, 119)
        ]

        shadow_points = [
            (x + 3, y + 3)
            for x, y in wave_points
        ]

        pygame.draw.polygon(
            water,
            (0, 8, 40, 210),
            shadow_points
        )

        pygame.draw.polygon(
            water,
            (0, 28, 100, 255),
            wave_points
        )

        pygame.draw.lines(
            water,
            (0, 100, 220, 255),
            False,
            wave_points,
            3
        )

        # =====================================================
        # 3. WEWNĘTRZNA WARSTWA WODY
        # =====================================================

        inner_wave = [
            (10, 116),
            (25, 103),
            (37, 86),
            (45, 66),
            (53, 47),
            (64, 30),
            (76, 21),
            (87, 20),
            (98, 25),
            (109, 35),
            (120, 46),
            (112, 45),
            (104, 37),
            (96, 31),
            (87, 29),
            (80, 36),
            (75, 50),
            (70, 69),
            (68, 85),

            # Wewnętrzna woda również opada niżej
            (78, 97),
            (96, 108),
            (116, 117),
            (136, 123),
            (113, 126),
            (86, 126),
            (57, 124),
            (32, 120),
            (10, 116)
        ]

        pygame.draw.polygon(
            water,
            (0, 75, 180, 255),
            inner_wave
        )

        # =====================================================
        # 4. TURKUSOWY REFLEKS
        # =====================================================

        highlight_points = [
            (14, 113),
            (29, 100),
            (40, 83),
            (48, 64),
            (57, 45),
            (67, 30),
            (77, 24),
            (87, 24),
            (98, 30),
            (108, 40),
            (117, 49),
            (108, 43),
            (99, 36),
            (91, 32),
            (84, 34),
            (78, 44),
            (73, 61),
            (70, 79),

            # Refleks dopasowany do opadającej końcówki
            (76, 94),
            (91, 105),
            (108, 114),
            (89, 117),
            (67, 117),
            (44, 115),
            (27, 113),
            (14, 113)
        ]

        pygame.draw.polygon(
            water,
            (0, 145, 230, 255),
            highlight_points
        )

        pygame.draw.lines(
            water,
            (35, 205, 255, 255),
            False,
            [
                (16, 111),
                (30, 98),
                (41, 81),
                (50, 61),
                (60, 42),
                (71, 28),
                (81, 25),
                (92, 29),
                (104, 39),
                (116, 49)
            ],
            2
        )

        # =====================================================
        # 5. PIANA NA SZCZYCIE
        # =====================================================

        foam_points = [
            (51, 51),
            (59, 37),
            (69, 25),
            (78, 19),
            (87, 18),
            (97, 23),
            (107, 31),
            (117, 41),
            (128, 50),
            (119, 48),
            (109, 39),
            (100, 31),
            (92, 27),
            (84, 27),
            (77, 33),
            (71, 45),
            (66, 59),
            (61, 66),
            (56, 62)
        ]

        pygame.draw.polygon(
            water,
            (160, 240, 255, 255),
            foam_points
        )

        pygame.draw.lines(
            water,
            (245, 255, 255, 255),
            False,
            [
                (51, 51),
                (59, 37),
                (69, 25),
                (78, 19),
                (87, 18),
                (97, 23),
                (107, 31),
                (117, 41),
                (128, 50)
            ],
            3
        )

        pygame.draw.lines(
            water,
            (255, 255, 255, 255),
            False,
            [
                (75, 23),
                (83, 20),
                (91, 22),
                (99, 27)
            ],
            2
        )

        # =====================================================
        # 6. KROPLE WODY I PIANY
        # =====================================================

        foam_drops = [
            (45, 65, 2),
            (53, 49, 2),
            (61, 36, 2),
            (69, 27, 2),
            (79, 19, 2),
            (91, 22, 2),
            (102, 29, 2),
            (113, 39, 2),
            (124, 48, 2),
            (37, 82, 1),
            (28, 96, 2),
            (19, 108, 1),
            (118, 103, 2),
            (133, 108, 1)
        ]

        for x, y, radius in foam_drops:
            pygame.draw.circle(
                water,
                (180, 245, 255, 245),
                (x, y),
                radius
            )

        # =====================================================
        # 7. SMUGI I REFLEKSY WODNE
        # =====================================================

        pygame.draw.arc(
            water,
            (90, 225, 255, 255),
            (22, 65, 46, 43),
            math.radians(190),
            math.radians(280),
            2
        )

        pygame.draw.arc(
            water,
            (20, 180, 255, 255),
            (30, 78, 52, 30),
            math.radians(190),
            math.radians(280),
            2
        )

        pygame.draw.arc(
            water,
            (130, 240, 255, 255),
            (72, 93, 49, 20),
            math.radians(195),
            math.radians(320),
            2
        )

        pygame.draw.arc(
            water,
            (0, 100, 220, 255),
            (38, 87, 38, 17),
            math.radians(195),
            math.radians(290),
            2
        )

        # =====================================================
        # 8. ROZPRYSKI PRZY PODSTAWIE
        # =====================================================

        splash_lines = [
            ((15, 115), (5, 108)),
            ((25, 120), (15, 128)),
            ((39, 122), (34, 131)),
            ((54, 124), (51, 130)),
            ((107, 127), (115, 136)),
            ((125, 124), (136, 130)),
            ((137, 119), (147, 114)),
            ((31, 109), (25, 103)),
            ((46, 88), (40, 82))
        ]

        for start, end in splash_lines:
            pygame.draw.line(
                water,
                (90, 220, 255, 235),
                start,
                end,
                2
            )

        # =====================================================
        # 9. BĄBELKI
        # =====================================================

        bubbles = [
            (12, 103, 2),
            (21, 94, 1),
            (33, 87, 2),
            (42, 73, 1),
            (132, 100, 2),
            (140, 104, 1)
        ]

        for x, y, radius in bubbles:
            pygame.draw.circle(
                water,
                (100, 220, 255, 220),
                (x, y),
                radius,
                1
            )

        # =====================================================
        # 10. ZMNIEJSZENIE I RYSOWANIE
        # =====================================================

        water = pygame.transform.smoothscale(
            water,
            (icon_size, icon_size)
        )

        screen.blit(
            water,
            (
                center_x - icon_size // 2,
                center_y - icon_size // 2 + wave_offset_y
            )
        )

    def draw_v1(self, screen):
        pass

    def draw_v2(self, screen):
        pass

    def draw_v3(self, screen):
        pass

class Wind(Elementals):
    def __init__(self):
        super().__init__(
            name="Wind",
            eqquiped=False,
            v1_energy_drain=10, #ZMIEŃ <
            v2_energy_drain=20,
            v3_energy_drain=30,
            v1_dmg=10,
            v2_dmg=15,
            v3_dmg=20,          #ZMIEŃ >
            v1_name="Slowing Gale",
            v2_name="Hurricane",
            v3_name="Reflecting spin"
        )

    def attack(self, target, player, v):
        if v == 1:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain
        elif v == 2:
            dmg = self.v2_dmg
            energy_drain = self.v2_energy_drain
        elif v == 3:
            dmg = self.v3_dmg
            energy_drain = self.v3_energy_drain
        else:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain

        # Zabierz energię
        player.energy -= energy_drain

        # Zadaj obrażenia
        target.hp -= dmg
        if target.hp < target.max_hp:
            target.hp = target.max_hp

    def draw_v1_icon(self, screen, center_x, center_y):
        # ==========================================
        # WIND V1 — SZARY WIATR + BRĄZOWE LIŚCIE
        # ==========================================

        import pygame
        import math

        # ==========================================
        # 1. SUBTELNA SZARA POŚWIATA
        # ==========================================

        glow_surface = pygame.Surface(
            (100, 100),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            glow_surface,
            (180, 190, 200, 18),
            (50, 50),
            35
        )

        pygame.draw.circle(
            glow_surface,
            (210, 215, 220, 24),
            (50, 50),
            24
        )

        screen.blit(
            glow_surface,
            (center_x - 50, center_y - 50)
        )

        # ==========================================
        # 2. FALOWANY WIATR — CIEMNY CIEŃ
        # ==========================================

        wind_shadow = [
            (center_x - 35, center_y - 12),
            (center_x - 25, center_y - 18),
            (center_x - 15, center_y - 16),
            (center_x - 7, center_y - 9),
            (center_x + 2, center_y - 5),
            (center_x + 11, center_y - 7),
            (center_x + 20, center_y - 14),
            (center_x + 31, center_y - 15),
        ]

        pygame.draw.lines(
            screen,
            (75, 80, 87),
            False,
            wind_shadow,
            7
        )

        # ==========================================
        # 3. GŁÓWNA FALA WIATRU
        # ==========================================

        wind_main = [
            (center_x - 36, center_y - 13),
            (center_x - 27, center_y - 19),
            (center_x - 18, center_y - 18),
            (center_x - 10, center_y - 11),
            (center_x - 2, center_y - 7),
            (center_x + 7, center_y - 8),
            (center_x + 16, center_y - 14),
            (center_x + 25, center_y - 16),
            (center_x + 35, center_y - 12),
        ]

        pygame.draw.lines(
            screen,
            (155, 160, 168),
            False,
            wind_main,
            4
        )

        # ==========================================
        # 4. ŚRODKOWA FALOWANA SMUGA
        # ==========================================

        wind_middle = [
            (center_x - 38, center_y),
            (center_x - 29, center_y - 5),
            (center_x - 20, center_y - 4),
            (center_x - 11, center_y + 2),
            (center_x - 2, center_y + 5),
            (center_x + 7, center_y + 3),
            (center_x + 16, center_y - 2),
            (center_x + 25, center_y - 3),
            (center_x + 37, center_y + 1),
        ]

        pygame.draw.lines(
            screen,
            (185, 190, 198),
            False,
            wind_middle,
            5
        )

        # Jasny refleks na środku wiatru
        pygame.draw.lines(
            screen,
            (225, 228, 232),
            False,
            [
                (center_x - 32, center_y - 1),
                (center_x - 23, center_y - 2),
                (center_x - 15, center_y + 3),
                (center_x - 7, center_y + 6),
                (center_x + 1, center_y + 6),
                (center_x + 10, center_y + 2),
                (center_x + 19, center_y + 1),
            ],
            2
        )

        # ==========================================
        # 5. DOLNA FALOWANA SMUGA
        # ==========================================

        wind_bottom = [
            (center_x - 31, center_y + 13),
            (center_x - 22, center_y + 8),
            (center_x - 13, center_y + 9),
            (center_x - 4, center_y + 15),
            (center_x + 5, center_y + 17),
            (center_x + 14, center_y + 13),
            (center_x + 22, center_y + 8),
            (center_x + 31, center_y + 9),
        ]

        pygame.draw.lines(
            screen,
            (125, 131, 140),
            False,
            wind_bottom,
            4
        )

        pygame.draw.lines(
            screen,
            (205, 209, 215),
            False,
            [
                (center_x - 25, center_y + 10),
                (center_x - 17, center_y + 11),
                (center_x - 9, center_y + 16),
                (center_x - 1, center_y + 18),
                (center_x + 7, center_y + 16),
            ],
            2
        )

        # ==========================================
        # 6. KRÓTKIE SMUGI POWIETRZA
        # ==========================================

        small_wind_lines = [
            [
                (center_x - 36, center_y + 22),
                (center_x - 28, center_y + 19),
                (center_x - 21, center_y + 20),
            ],
            [
                (center_x + 17, center_y - 24),
                (center_x + 25, center_y - 22),
                (center_x + 33, center_y - 25),
            ],
            [
                (center_x - 34, center_y - 25),
                (center_x - 27, center_y - 27),
                (center_x - 21, center_y - 25),
            ],
        ]

        for points in small_wind_lines:
            pygame.draw.lines(
                screen,
                (190, 195, 202),
                False,
                points,
                2
            )

        # ==========================================
        # 7. FUNKCJA RYSOWANIA BRĄZOWYCH LIŚCI
        # ==========================================

        def draw_leaf(x, y, size, angle, color):
            leaf_surface = pygame.Surface(
                (size * 4, size * 4),
                pygame.SRCALPHA
            )

            leaf_center = size * 2

            # Liść o lekko wydłużonym, jesiennym kształcie
            leaf_points = [
                (leaf_center - size, leaf_center),
                (leaf_center - size // 2, leaf_center - size),
                (leaf_center + size // 2, leaf_center - size * 2),
                (leaf_center + size, leaf_center - size),
                (leaf_center + size, leaf_center),
                (leaf_center + size // 2, leaf_center + size),
                (leaf_center - size // 2, leaf_center + size),
            ]

            # Ciemna krawędź
            pygame.draw.polygon(
                leaf_surface,
                (75, 42, 22),
                leaf_points
            )

            # Główna powierzchnia liścia
            inner_points = [
                (leaf_center - size + 1, leaf_center),
                (leaf_center - size // 2, leaf_center - size + 1),
                (leaf_center + size // 2, leaf_center - size * 2 + 1),
                (leaf_center + size - 1, leaf_center - size),
                (leaf_center + size - 1, leaf_center),
                (leaf_center + size // 2, leaf_center + size - 1),
                (leaf_center - size // 2, leaf_center + size - 1),
            ]

            pygame.draw.polygon(
                leaf_surface,
                color,
                inner_points
            )

            # Główna żyłka
            pygame.draw.line(
                leaf_surface,
                (225, 175, 105),
                (leaf_center - size + 1, leaf_center),
                (leaf_center + size - 1, leaf_center),
                1
            )

            # Boczne żyłki
            pygame.draw.line(
                leaf_surface,
                (195, 135, 75),
                (leaf_center - size // 3, leaf_center),
                (leaf_center - size // 2, leaf_center - size // 2),
                1
            )

            pygame.draw.line(
                leaf_surface,
                (195, 135, 75),
                (leaf_center, leaf_center),
                (leaf_center + size // 3, leaf_center - size),
                1
            )

            pygame.draw.line(
                leaf_surface,
                (195, 135, 75),
                (leaf_center - size // 3, leaf_center),
                (leaf_center - size // 2, leaf_center + size // 2),
                1
            )

            # Obrót liścia zgodnie z kierunkiem podmuchu
            rotated_leaf = pygame.transform.rotate(
                leaf_surface,
                angle
            )

            leaf_rect = rotated_leaf.get_rect(
                center=(int(x), int(y))
            )

            screen.blit(
                rotated_leaf,
                leaf_rect
            )

        # ==========================================
        # 8. LIŚCIE NIESIONE OD LEWEJ DO PRAWEJ
        # ==========================================

        leaves = [
            # x, y, rozmiar, kąt, kolor

            (-25, -20, 5, -35, (145, 82, 38)),
            (-8, -27, 4, 25, (175, 105, 48)),
            (12, -21, 5, -20, (120, 65, 30)),
            (29, -16, 4, 40, (165, 95, 40)),

            (-29, 3, 5, 20, (130, 72, 32)),
            (-7, -2, 4, -45, (185, 120, 55)),
            (17, 5, 5, 35, (140, 75, 35)),
            (32, 13, 4, -25, (170, 95, 40)),

            (-19, 23, 4, 35, (165, 95, 45)),
            (3, 26, 5, -20, (125, 65, 28)),
            (22, 23, 4, 30, (190, 125, 60)),
        ]

        for offset_x, offset_y, size, angle, color in leaves:
            draw_leaf(
                center_x + offset_x,
                center_y + offset_y,
                size,
                angle,
                color
            )

        # ==========================================
        # 9. MAŁE JESIENNE CZĄSTECZKI
        # ==========================================

        particles = [
            (-35, -6, 2, (180, 145, 115)),
            (-33, 17, 1, (210, 180, 145)),
            (-14, -32, 1, (185, 150, 115)),
            (5, -30, 2, (205, 165, 115)),
            (25, -28, 1, (180, 140, 100)),
            (37, -6, 2, (205, 180, 150)),
            (30, 21, 1, (180, 140, 105)),
            (-4, 32, 1, (205, 170, 130)),
        ]

        for offset_x, offset_y, radius, color in particles:
            pygame.draw.circle(
                screen,
                color,
                (
                    center_x + offset_x,
                    center_y + offset_y
                ),
                radius
            )

    def draw_v2_icon(self, screen, center_x, center_y):
        # ==========================================
        # TORNADO — V2 ULTIMATE
        # ==========================================

        import math
        import pygame

        # ==========================================
        # 1. MIĘKKA SZARA POŚWIATA
        # ==========================================

        glow_size = 110
        glow = pygame.Surface(
            (glow_size, glow_size),
            pygame.SRCALPHA
        )

        pygame.draw.ellipse(
            glow,
            (170, 180, 190, 15),
            (7, 20, 96, 75)
        )

        pygame.draw.ellipse(
            glow,
            (195, 202, 210, 22),
            (17, 24, 76, 62)
        )

        pygame.draw.ellipse(
            glow,
            (220, 225, 230, 18),
            (27, 30, 56, 48)
        )

        screen.blit(
            glow,
            (center_x - 55, center_y - 55)
        )

        # ==========================================
        # 2. ZEWNĘTRZNA SYLWETKA TORNADA
        # ==========================================

        pygame.draw.polygon(
            screen,
            (65, 72, 82),
            [
                (center_x - 4, center_y - 34),
                (center_x + 10, center_y - 32),
                (center_x + 27, center_y - 25),
                (center_x + 34, center_y - 15),
                (center_x + 29, center_y - 7),
                (center_x + 20, center_y - 2),
                (center_x + 22, center_y + 7),
                (center_x + 12, center_y + 13),
                (center_x + 9, center_y + 21),
                (center_x + 1, center_y + 29),
                (center_x - 5, center_y + 18),
                (center_x - 13, center_y + 13),
                (center_x - 20, center_y + 8),
                (center_x - 15, center_y + 1),
                (center_x - 27, center_y - 5),
                (center_x - 31, center_y - 14),
                (center_x - 22, center_y - 23),
                (center_x - 12, center_y - 29),
            ]
        )

        # ==========================================
        # 3. GŁÓWNY WIR WIATRU
        # ==========================================

        pygame.draw.polygon(
            screen,
            (112, 122, 133),
            [
                (center_x - 5, center_y - 31),
                (center_x + 9, center_y - 29),
                (center_x + 23, center_y - 23),
                (center_x + 28, center_y - 16),
                (center_x + 20, center_y - 10),
                (center_x + 10, center_y - 7),
                (center_x + 17, center_y - 1),
                (center_x + 11, center_y + 6),
                (center_x + 5, center_y + 12),
                (center_x + 3, center_y + 22),
                (center_x - 3, center_y + 15),
                (center_x - 8, center_y + 10),
                (center_x - 16, center_y + 6),
                (center_x - 10, center_y),
                (center_x - 22, center_y - 6),
                (center_x - 25, center_y - 13),
                (center_x - 17, center_y - 20),
                (center_x - 9, center_y - 25),
            ]
        )

        # ==========================================
        # 4. JASNE PASMA WIRUJĄCEGO POWIETRZA
        # ==========================================

        pygame.draw.lines(
            screen,
            (205, 212, 220),
            False,
            [
                (center_x - 20, center_y - 20),
                (center_x - 7, center_y - 27),
                (center_x + 8, center_y - 26),
                (center_x + 19, center_y - 20),
                (center_x + 16, center_y - 15),
                (center_x + 4, center_y - 12),
            ],
            3
        )

        pygame.draw.lines(
            screen,
            (183, 193, 204),
            False,
            [
                (center_x - 24, center_y - 7),
                (center_x - 11, center_y - 12),
                (center_x + 5, center_y - 11),
                (center_x + 19, center_y - 6),
                (center_x + 12, center_y + 1),
                (center_x + 2, center_y + 3),
            ],
            3
        )

        pygame.draw.lines(
            screen,
            (220, 225, 232),
            False,
            [
                (center_x - 15, center_y + 5),
                (center_x - 5, center_y + 1),
                (center_x + 7, center_y + 2),
                (center_x + 12, center_y + 6),
                (center_x + 4, center_y + 12),
                (center_x - 2, center_y + 17),
            ],
            2
        )

        # ==========================================
        # 5. POZIOME SMUGI WIATRU
        # ==========================================

        pygame.draw.lines(
            screen,
            (150, 160, 171),
            False,
            [
                (center_x - 39, center_y - 13),
                (center_x - 30, center_y - 17),
                (center_x - 22, center_y - 16),
                (center_x - 17, center_y - 12),
            ],
            3
        )

        pygame.draw.lines(
            screen,
            (190, 198, 207),
            False,
            [
                (center_x + 17, center_y - 22),
                (center_x + 26, center_y - 26),
                (center_x + 36, center_y - 23),
                (center_x + 40, center_y - 19),
            ],
            2
        )

        pygame.draw.lines(
            screen,
            (135, 146, 158),
            False,
            [
                (center_x - 35, center_y + 4),
                (center_x - 27, center_y + 1),
                (center_x - 20, center_y + 3),
            ],
            2
        )

        pygame.draw.lines(
            screen,
            (205, 212, 220),
            False,
            [
                (center_x + 11, center_y + 14),
                (center_x + 22, center_y + 10),
                (center_x + 32, center_y + 13),
            ],
            2
        )

        # ==========================================
        # 6. ZAWINIĘTE PASMO U PODSTAWY
        # ==========================================

        pygame.draw.polygon(
            screen,
            (75, 83, 94),
            [
                (center_x - 8, center_y + 14),
                (center_x + 3, center_y + 18),
                (center_x + 9, center_y + 23),
                (center_x + 2, center_y + 29),
                (center_x - 5, center_y + 22),
                (center_x - 13, center_y + 19),
            ]
        )

        pygame.draw.lines(
            screen,
            (192, 201, 211),
            False,
            [
                (center_x - 9, center_y + 16),
                (center_x - 2, center_y + 20),
                (center_x + 3, center_y + 24),
            ],
            2
        )

        # ==========================================
        # 7. BRĄZOWE LIŚCIE
        # ==========================================

        def draw_leaf(x, y, size, angle, color):
            leaf_surface = pygame.Surface(
                (size * 4, size * 4),
                pygame.SRCALPHA
            )

            c = size * 2

            # Liść z wyraźnym czubkiem
            points = [
                (c, c - size * 2),
                (c + size, c - size),
                (c + size * 2, c - size // 2),
                (c + size, c),
                (c + size * 2, c + size),
                (c, c + size * 2),
                (c - size, c + size),
                (c - size * 2, c),
                (c - size, c - size),
            ]

            pygame.draw.polygon(
                leaf_surface,
                color,
                points
            )

            pygame.draw.polygon(
                leaf_surface,
                (80, 49, 27),
                points,
                1
            )

            # Żyłka liścia
            pygame.draw.line(
                leaf_surface,
                (220, 170, 100),
                (c, c + size),
                (c, c - size * 2),
                1
            )

            # Boczne żyłki
            pygame.draw.line(
                leaf_surface,
                (205, 145, 83),
                (c, c),
                (c + size, c - size),
                1
            )

            pygame.draw.line(
                leaf_surface,
                (205, 145, 83),
                (c, c - size // 2),
                (c - size, c - size),
                1
            )

            rotated = pygame.transform.rotate(
                leaf_surface,
                angle
            )

            screen.blit(
                rotated,
                rotated.get_rect(
                    center=(int(x), int(y))
                )
            )

        # Liść po lewej stronie
        draw_leaf(
            center_x - 32,
            center_y - 25,
            3,
            -35,
            (126, 76, 39)
        )

        # Liść wirujący w górnej części
        draw_leaf(
            center_x + 29,
            center_y - 30,
            4,
            25,
            (153, 91, 43)
        )

        # Liść z prawej strony
        draw_leaf(
            center_x + 36,
            center_y + 1,
            3,
            55,
            (111, 66, 35)
        )

        # Liść w dolnej części tornada
        draw_leaf(
            center_x - 19,
            center_y + 22,
            3,
            -20,
            (168, 103, 47)
        )

        # Mały liść przy górnym wirze
        draw_leaf(
            center_x + 4,
            center_y - 37,
            2,
            40,
            (135, 79, 38)
        )

        # ==========================================
        # 8. DROBINKI PYŁU
        # ==========================================

        particles = [
            (-35, -25, 2, (176, 184, 194)),
            (35, -12, 2, (202, 208, 216)),
            (-29, 12, 2, (143, 153, 165)),
            (25, 23, 2, (171, 180, 190)),
            (12, -36, 1, (225, 230, 235)),
            (-38, 1, 1, (192, 200, 208)),
            (32, 19, 1, (215, 220, 226)),
        ]

        for offset_x, offset_y, radius, color in particles:
            pygame.draw.circle(
                screen,
                color,
                (
                    center_x + offset_x,
                    center_y + offset_y
                ),
                radius
            )

        # ==========================================
        # 9. DROBNE SMUGI RUCHU
        # ==========================================

        pygame.draw.line(
            screen,
            (185, 194, 204),
            (center_x - 37, center_y - 3),
            (center_x - 30, center_y - 5),
            2
        )

        pygame.draw.line(
            screen,
            (215, 221, 228),
            (center_x + 28, center_y - 8),
            (center_x + 36, center_y - 10),
            2
        )

        pygame.draw.line(
            screen,
            (155, 165, 176),
            (center_x - 31, center_y + 17),
            (center_x - 23, center_y + 15),
            2
        )

    def draw_v1(self, screen):
        pass

    def draw_v2(self, screen):
        pass

    def draw_v3(self, screen):
        pass

class Nature(Elementals):
    def __init__(self):
        super().__init__(
            name="Nature",
            eqquiped=False,
            v1_energy_drain=10, #ZMIEŃ <
            v2_energy_drain=20,
            v3_energy_drain=30,
            v1_dmg=10,
            v2_dmg=15,
            v3_dmg=20,          #ZMIEŃ >
            v1_name="Dirt Burst",
            v2_name="Vines Eruption",
            v3_name="Stone Guard"
        )

    def attack(self, target, player, v):
        if v == 1:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain
        elif v == 2:
            dmg = self.v2_dmg
            energy_drain = self.v2_energy_drain
        elif v == 3:
            dmg = self.v3_dmg
            energy_drain = self.v3_energy_drain
        else:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain

        # Zabierz energię
        player.energy -= energy_drain

        # Zadaj obrażenia
        target.hp -= dmg
        if target.hp < target.max_hp:
            target.hp = target.max_hp

    def draw_v1_icon(self, screen, center_x, center_y):
        # ==========================================
        # DIRT V1 — KULKI ZIEMI LECĄCE W PRAWO
        # ==========================================

        import pygame
        import math

        # ==========================================
        # 1. PYŁ I POŚWIATA
        # ==========================================

        glow_surface = pygame.Surface(
            (110, 100),
            pygame.SRCALPHA
        )

        pygame.draw.ellipse(
            glow_surface,
            (145, 100, 55, 18),
            (5, 20, 100, 60)
        )

        pygame.draw.ellipse(
            glow_surface,
            (180, 130, 75, 22),
            (15, 28, 80, 42)
        )

        screen.blit(
            glow_surface,
            (center_x - 55, center_y - 50)
        )

        # ==========================================
        # 2. FUNKCJA RYSUJĄCA KULKĘ ZIEMI
        # ==========================================

        def draw_dirt_ball(x, y, radius, rotation=0):
            # Cień i ciemny kontur
            pygame.draw.circle(
                screen,
                (65, 42, 25),
                (int(x), int(y)),
                radius + 1
            )

            # Główna bryła ziemi
            pygame.draw.circle(
                screen,
                (125, 78, 39),
                (int(x), int(y)),
                radius
            )

            # Jaśniejsza powierzchnia
            pygame.draw.ellipse(
                screen,
                (166, 111, 58),
                (
                    int(x - radius * 0.65),
                    int(y - radius * 0.65),
                    int(radius * 1.35),
                    int(radius * 1.15)
                )
            )

            # Ciemna grudka na dole
            pygame.draw.ellipse(
                screen,
                (91, 55, 29),
                (
                    int(x - radius * 0.55),
                    int(y + radius * 0.15),
                    int(radius * 1.1),
                    max(2, int(radius * 0.5))
                )
            )

            # Drobne kamyczki na powierzchni
            if radius >= 5:
                pygame.draw.circle(
                    screen,
                    (204, 151, 87),
                    (
                        int(x - radius * 0.25),
                        int(y - radius * 0.25)
                    ),
                    max(1, radius // 5)
                )

                pygame.draw.circle(
                    screen,
                    (83, 52, 29),
                    (
                        int(x + radius * 0.4),
                        int(y + radius * 0.1)
                    ),
                    max(1, radius // 6)
                )

        # ==========================================
        # 3. SMUGI RUCHU — LEWO -> PRAWO
        # ==========================================

        motion_lines = [
            (-38, -17, -20, -17, 3, (115, 82, 48)),
            (-42, -9, -24, -9, 2, (170, 126, 75)),
            (-36, 5, -22, 5, 3, (105, 72, 42)),
            (-40, 17, -25, 17, 2, (157, 111, 62)),
            (-20, -28, -9, -28, 2, (190, 143, 85)),
        ]

        for x1, y1, x2, y2, thickness, color in motion_lines:
            pygame.draw.line(
                screen,
                color,
                (center_x + x1, center_y + y1),
                (center_x + x2, center_y + y2),
                thickness
            )

        # ==========================================
        # 4. GŁÓWNE KULKI ZIEMI
        # ==========================================

        dirt_balls = [
            # Duża kulka z przodu
            (22, -2, 10, 0),

            # Kulka z tyłu
            (-9, -15, 7, 1),

            # Dolna kulka
            (-8, 15, 6, 2),

            # Górna kulka
            (7, -25, 5, 0),

            # Mniejsza kulka z prawej
            (38, 10, 5, 1),

            # Mała kulka z lewej
            (-28, 1, 4, 0),

            # Drobna kulka na dole
            (17, 24, 4, 2),
        ]

        for offset_x, offset_y, radius, rotation in dirt_balls:
            draw_dirt_ball(
                center_x + offset_x,
                center_y + offset_y,
                radius,
                rotation
            )

        # ==========================================
        # 5. MAŁE OKRUCHY LECĄCE DO PRZODU
        # ==========================================

        debris = [
            (-31, -24, 2, (151, 103, 55)),
            (-19, 23, 2, (120, 78, 41)),
            (0, -34, 2, (180, 129, 72)),
            (30, -19, 2, (173, 118, 61)),
            (43, -5, 2, (130, 85, 44)),
            (31, 24, 2, (154, 100, 50)),
            (-38, 10, 1, (190, 143, 85)),
            (44, 17, 1, (205, 158, 97)),
            (1, 31, 2, (115, 73, 38)),
        ]

        for offset_x, offset_y, radius, color in debris:
            pygame.draw.circle(
                screen,
                color,
                (
                    center_x + offset_x,
                    center_y + offset_y
                ),
                radius
            )

        # ==========================================
        # 6. SZYBKIE SMUGI ZA KULKAMI
        # ==========================================

        pygame.draw.lines(
            screen,
            (190, 143, 85),
            False,
            [
                (center_x - 25, center_y - 17),
                (center_x - 17, center_y - 19),
                (center_x - 12, center_y - 17),
            ],
            2
        )

        pygame.draw.lines(
            screen,
            (125, 83, 43),
            False,
            [
                (center_x - 25, center_y + 13),
                (center_x - 17, center_y + 11),
                (center_x - 12, center_y + 13),
            ],
            2
        )

        pygame.draw.lines(
            screen,
            (174, 121, 64),
            False,
            [
                (center_x + 23, center_y - 13),
                (center_x + 31, center_y - 15),
                (center_x + 36, center_y - 13),
            ],
            2
        )

    def draw_v2_icon(self, screen, center_x, center_y):
        # ==========================================
        # VINES — V2 ULTIMATE
        # PNĄCZA WYCHODZĄCE Z ZIEMI
        # ==========================================

        import math
        import pygame

        # ==========================================
        # 1. ZIELONA POŚWIATA
        # ==========================================

        glow = pygame.Surface((110, 110), pygame.SRCALPHA)

        pygame.draw.ellipse(
            glow,
            (35, 150, 55, 18),
            (8, 25, 94, 75)
        )

        pygame.draw.ellipse(
            glow,
            (65, 190, 75, 24),
            (20, 32, 70, 60)
        )

        screen.blit(
            glow,
            (center_x - 55, center_y - 55)
        )

        # ==========================================
        # 2. ZIEMIA
        # ==========================================

        ground_y = center_y + 27

        pygame.draw.ellipse(
            screen,
            (65, 43, 28),
            (
                center_x - 39,
                ground_y - 3,
                78,
                17
            )
        )

        pygame.draw.ellipse(
            screen,
            (105, 70, 39),
            (
                center_x - 33,
                ground_y - 3,
                66,
                10
            )
        )

        # Pęknięcia ziemi
        pygame.draw.lines(
            screen,
            (45, 35, 25),
            False,
            [
                (center_x - 7, ground_y + 1),
                (center_x - 13, ground_y + 5),
                (center_x - 19, ground_y + 4)
            ],
            2
        )

        pygame.draw.lines(
            screen,
            (45, 35, 25),
            False,
            [
                (center_x + 5, ground_y + 1),
                (center_x + 12, ground_y + 5),
                (center_x + 18, ground_y + 3)
            ],
            2
        )

        # ==========================================
        # 3. FUNKCJA RYSUJĄCA PNĄCZE
        # ==========================================

        def draw_vine(points, width):
            # Ciemny kontur
            pygame.draw.lines(
                screen,
                (32, 65, 30),
                False,
                points,
                width + 4
            )

            # Główna łodyga
            pygame.draw.lines(
                screen,
                (55, 125, 43),
                False,
                points,
                width
            )

            # Jasny pasek na łodydze
            highlight_points = []

            for x, y in points:
                highlight_points.append(
                    (x - max(1, width // 4), y)
                )

            pygame.draw.lines(
                screen,
                (105, 175, 65),
                False,
                highlight_points,
                max(1, width // 3)
            )

        # ==========================================
        # 4. GŁÓWNE PNĄCZE — LEWA STRONA
        # ==========================================

        left_vine = [
            (center_x - 12, ground_y),
            (center_x - 19, center_y + 17),
            (center_x - 24, center_y + 7),
            (center_x - 21, center_y - 3),
            (center_x - 12, center_y - 11),
            (center_x - 10, center_y - 21),
            (center_x - 17, center_y - 30)
        ]

        draw_vine(left_vine, 7)

        # ==========================================
        # 5. GŁÓWNE PNĄCZE — PRAWA STRONA
        # ==========================================

        right_vine = [
            (center_x + 12, ground_y),
            (center_x + 20, center_y + 17),
            (center_x + 25, center_y + 7),
            (center_x + 19, center_y - 1),
            (center_x + 12, center_y - 7),
            (center_x + 14, center_y - 18),
            (center_x + 24, center_y - 25)
        ]

        draw_vine(right_vine, 7)

        # ==========================================
        # 6. ŚRODKOWE PNĄCZE — NAJWYŻSZE
        # ==========================================

        center_vine = [
            (center_x, ground_y),
            (center_x - 5, center_y + 17),
            (center_x + 2, center_y + 8),
            (center_x + 5, center_y - 2),
            (center_x - 2, center_y - 11),
            (center_x + 1, center_y - 21),
            (center_x + 8, center_y - 34)
        ]

        draw_vine(center_vine, 8)

        # ==========================================
        # 7. BOCZNE ODROSTY
        # ==========================================

        side_vines = [
            [
                (center_x - 20, center_y + 7),
                (center_x - 30, center_y + 2),
                (center_x - 34, center_y - 5)
            ],
            [
                (center_x + 20, center_y + 7),
                (center_x + 30, center_y + 1),
                (center_x + 34, center_y - 7)
            ],
            [
                (center_x - 12, center_y - 11),
                (center_x - 4, center_y - 17),
                (center_x + 2, center_y - 16)
            ],
            [
                (center_x + 13, center_y - 8),
                (center_x + 21, center_y - 13),
                (center_x + 29, center_y - 12)
            ]
        ]

        for branch in side_vines:
            draw_vine(branch, 3)

        # ==========================================
        # 8. KOLCE NA PNĄCZACH
        # ==========================================

        thorns = [
            (center_x - 22, center_y + 3, -1),
            (center_x - 15, center_y - 12, 1),
            (center_x + 20, center_y + 3, 1),
            (center_x + 14, center_y - 15, -1),
            (center_x + 3, center_y + 9, 1),
            (center_x - 2, center_y - 20, -1)
        ]

        for x, y, direction in thorns:
            pygame.draw.polygon(
                screen,
                (35, 75, 31),
                [
                    (x, y),
                    (x + direction * 7, y - 5),
                    (x + direction * 2, y + 3)
                ]
            )

            pygame.draw.polygon(
                screen,
                (105, 150, 53),
                [
                    (x, y),
                    (x + direction * 5, y - 4),
                    (x + direction, y + 2)
                ]
            )

        # ==========================================
        # 9. FUNKCJA RYSUJĄCA LIŚĆ
        # ==========================================

        def draw_leaf(x, y, size, angle, color):
            leaf_surface = pygame.Surface(
                (size * 4, size * 4),
                pygame.SRCALPHA
            )

            c = size * 2

            points = [
                (c, c - size * 2),
                (c + size, c - size),
                (c + size * 2, c - size // 2),
                (c + size, c + size),
                (c, c + size * 2),
                (c - size, c + size),
                (c - size * 2, c - size // 2),
                (c - size, c - size)
            ]

            pygame.draw.polygon(
                leaf_surface,
                color,
                points
            )

            pygame.draw.polygon(
                leaf_surface,
                (30, 75, 30),
                points,
                1
            )

            pygame.draw.line(
                leaf_surface,
                (155, 205, 90),
                (c, c + size),
                (c, c - size * 2),
                1
            )

            rotated_leaf = pygame.transform.rotate(
                leaf_surface,
                angle
            )

            screen.blit(
                rotated_leaf,
                rotated_leaf.get_rect(
                    center=(int(x), int(y))
                )
            )

        # ==========================================
        # 10. LIŚCIE NA PNĄCZACH
        # ==========================================

        leaves = [
            (-29, -5, 4, -35, (65, 145, 45)),
            (-16, -22, 4, 30, (85, 165, 55)),
            (-29, 12, 3, -20, (105, 175, 65)),
            (-3, -16, 4, 40, (75, 155, 45)),
            (20, -7, 4, -35, (65, 135, 40)),
            (30, -14, 3, 25, (110, 180, 65)),
            (22, 13, 4, 35, (80, 150, 45)),
            (4, 9, 3, -25, (115, 185, 70)),
            (-13, 15, 3, 30, (85, 155, 50))
        ]

        for offset_x, offset_y, size, angle, color in leaves:
            draw_leaf(
                center_x + offset_x,
                center_y + offset_y,
                size,
                angle,
                color
            )

        # ==========================================
        # 11. DROBNE CZĄSTECZKI NATURY
        # ==========================================

        particles = [
            (-35, -20, 2, (115, 175, 65)),
            (35, -25, 2, (145, 195, 85)),
            (-31, 20, 2, (90, 145, 50)),
            (32, 16, 2, (125, 180, 65)),
            (0, -39, 2, (155, 205, 95)),
            (12, -32, 1, (190, 220, 125)),
            (-24, -29, 1, (175, 210, 105))
        ]

        for offset_x, offset_y, radius, color in particles:
            pygame.draw.circle(
                screen,
                color,
                (
                    center_x + offset_x,
                    center_y + offset_y
                ),
                radius
            )

    def draw_v1(self, screen):
        pass

    def draw_v2(self, screen):
        pass

    def draw_v3(self, screen):
        pass

class Bloodborn(Elementals):
    def __init__(self):
        super().__init__(
            name="Bloodborn",
            eqquiped=False,
            v1_energy_drain=10, #ZMIEŃ <
            v2_energy_drain=20,
            v3_energy_drain=30,
            v1_dmg=10,
            v2_dmg=15,
            v3_dmg=20,          #ZMIEŃ >
            v1_name="Vampire Swarm",
            v2_name="Blood Leech",
            v3_name="Eternal Recharge"
        )

    def attack(self, target, player, v):
        if v == 1:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain
        elif v == 2:
            dmg = self.v2_dmg
            energy_drain = self.v2_energy_drain
        elif v == 3:
            dmg = self.v3_dmg
            energy_drain = self.v3_energy_drain
        else:
            dmg = self.v1_dmg
            energy_drain = self.v1_energy_drain

        # Zabierz energię
        player.energy -= energy_drain

        # Zadaj obrażenia
        target.hp -= dmg
        if target.hp < target.max_hp:
            target.hp = target.max_hp

    def draw_v1_icon(self, screen, center_x, center_y):
        # ==========================================
        # FLYING BATS V2 — DARK MAGIC
        # ==========================================

        import pygame
        import math

        # ==========================================
        # 1. FIOLETOWA POŚWIATA
        # ==========================================

        glow_surface = pygame.Surface((120, 110), pygame.SRCALPHA)

        pygame.draw.ellipse(
            glow_surface,
            (100, 35, 160, 18),
            (5, 15, 110, 85)
        )

        pygame.draw.ellipse(
            glow_surface,
            (140, 55, 200, 25),
            (20, 25, 80, 65)
        )

        pygame.draw.ellipse(
            glow_surface,
            (180, 90, 240, 12),
            (32, 32, 56, 48)
        )

        screen.blit(
            glow_surface,
            (center_x - 60, center_y - 55)
        )

        # ==========================================
        # 2. FUNKCJA RYSUJĄCA NIETOPERZA
        # ==========================================

        def draw_bat(x, y, size, wing_angle, color):
            shadow_color = (17, 12, 27)
            outline_color = (30, 19, 43)

            wing_spread = max(
                0.4,
                math.cos(math.radians(wing_angle))
            )

            half_width = int(size * 1.9 * wing_spread)
            wing_height = int(size * 0.9)

            # ------------------------------
            # LEWE SKRZYDŁO
            # ------------------------------

            left_wing = [
                (x - size // 4, y),
                (x - half_width // 3, y - wing_height),
                (x - half_width, y - wing_height // 2),
                (x - half_width + size // 4, y + size // 8),
                (x - half_width // 2, y + size // 2),
                (x - size // 3, y + size // 3),
                (x, y + size // 4),
            ]

            # ------------------------------
            # PRAWE SKRZYDŁO
            # ------------------------------

            right_wing = [
                (x + size // 4, y),
                (x + half_width // 3, y - wing_height),
                (x + half_width, y - wing_height // 2),
                (x + half_width - size // 4, y + size // 8),
                (x + half_width // 2, y + size // 2),
                (x + size // 3, y + size // 3),
                (x, y + size // 4),
            ]

            # Kontury skrzydeł
            pygame.draw.polygon(
                screen, outline_color, left_wing
            )

            pygame.draw.polygon(
                screen, outline_color, right_wing
            )

            # Właściwe skrzydła
            pygame.draw.polygon(
                screen, color, left_wing
            )

            pygame.draw.polygon(
                screen, color, right_wing
            )

            # Delikatne żyłki skrzydeł
            wing_detail = (
                max(0, color[0] - 8),
                max(0, color[1] - 3),
                min(255, color[2] + 15)
            )

            pygame.draw.line(
                screen,
                wing_detail,
                (x - size // 4, y),
                (x - half_width + size // 4, y + size // 8),
                1
            )

            pygame.draw.line(
                screen,
                wing_detail,
                (x + size // 4, y),
                (x + half_width - size // 4, y + size // 8),
                1
            )

            # ------------------------------
            # KORPUS
            # ------------------------------

            body = [
                (x - size // 4, y - size // 3),
                (x + size // 4, y - size // 3),
                (x + size // 3, y + size // 4),
                (x, y + size * 3 // 4),
                (x - size // 3, y + size // 4),
            ]

            pygame.draw.polygon(
                screen, shadow_color, body
            )

            inner_body = [
                (x - size // 5, y - size // 3),
                (x + size // 5, y - size // 3),
                (x + size // 4, y + size // 5),
                (x, y + size // 2),
                (x - size // 4, y + size // 5),
            ]

            pygame.draw.polygon(
                screen, color, inner_body
            )

            # ------------------------------
            # GŁOWA I USZY
            # ------------------------------

            head_y = y - size // 3
            head_radius = max(2, size // 4)

            pygame.draw.circle(
                screen,
                outline_color,
                (x, head_y),
                head_radius + 1
            )

            pygame.draw.circle(
                screen,
                color,
                (x, head_y),
                head_radius
            )

            # Lewe ucho
            pygame.draw.polygon(
                screen,
                outline_color,
                [
                    (x - size // 6, head_y),
                    (x - size // 3, y - size * 2 // 3),
                    (x - size // 12, y - size // 5),
                ]
            )

            pygame.draw.polygon(
                screen,
                color,
                [
                    (x - size // 6, head_y),
                    (x - size // 3, y - size * 2 // 3),
                    (x - size // 12, y - size // 5),
                ]
            )

            # Prawe ucho
            pygame.draw.polygon(
                screen,
                outline_color,
                [
                    (x + size // 6, head_y),
                    (x + size // 3, y - size * 2 // 3),
                    (x + size // 12, y - size // 5),
                ]
            )

            pygame.draw.polygon(
                screen,
                color,
                [
                    (x + size // 6, head_y),
                    (x + size // 3, y - size * 2 // 3),
                    (x + size // 12, y - size // 5),
                ]
            )

            # ------------------------------
            # CZERWONE OCZY
            # ------------------------------

            eye_radius = max(1, size // 12)
            eye_y = head_y

            pygame.draw.circle(
                screen,
                (120, 20, 45),
                (x - max(1, size // 8), eye_y),
                eye_radius + 1
            )

            pygame.draw.circle(
                screen,
                (255, 55, 90),
                (x - max(1, size // 8), eye_y),
                eye_radius
            )

            pygame.draw.circle(
                screen,
                (120, 20, 45),
                (x + max(1, size // 8), eye_y),
                eye_radius + 1
            )

            pygame.draw.circle(
                screen,
                (255, 55, 90),
                (x + max(1, size // 8), eye_y),
                eye_radius
            )

        # ==========================================
        # 3. GŁÓWNY NIETOPERZ
        # ==========================================

        draw_bat(
            center_x,
            center_y - 2,
            15,
            0,
            (48, 31, 65)
        )

        # ==========================================
        # 4. NIETOPERZ PO LEWEJ
        # ==========================================

        draw_bat(
            center_x - 29,
            center_y - 14,
            9,
            20,
            (68, 43, 91)
        )

        # ==========================================
        # 5. NIETOPERZ PO PRAWEJ
        # ==========================================

        draw_bat(
            center_x + 29,
            center_y - 10,
            10,
            -15,
            (53, 35, 75)
        )

        # ==========================================
        # 6. MAŁY NIETOPERZ U GÓRY
        # ==========================================

        draw_bat(
            center_x + 5,
            center_y - 32,
            7,
            25,
            (83, 51, 110)
        )

        # ==========================================
        # 7. MAŁY NIETOPERZ NA DOLE
        # ==========================================

        draw_bat(
            center_x - 19,
            center_y + 23,
            6,
            -20,
            (59, 39, 81)
        )

        # ==========================================
        # 8. CZĄSTECZKI MROCZNEJ MAGII
        # ==========================================

        particles = [
            (-38, -23, 2, (165, 90, 225)),
            (37, -26, 2, (185, 115, 245)),
            (-40, 6, 2, (125, 65, 185)),
            (40, 13, 2, (155, 85, 210)),
            (1, 35, 2, (180, 105, 230)),
            (-14, -39, 1, (220, 165, 255)),
            (26, 29, 1, (200, 135, 235)),
            (-32, 24, 1, (150, 90, 200)),
            (15, -20, 1, (205, 130, 250)),
            (-23, -7, 1, (175, 100, 220)),
        ]

        for offset_x, offset_y, radius, color in particles:
            pygame.draw.circle(
                screen,
                color,
                (
                    int(center_x + offset_x),
                    int(center_y + offset_y)
                ),
                radius
            )

        # ==========================================
        # 9. SMUGI MROCZNEJ ENERGII
        # ==========================================

        pygame.draw.lines(
            screen,
            (100, 55, 145),
            False,
            [
                (center_x - 40, center_y - 5),
                (center_x - 35, center_y - 9),
                (center_x - 30, center_y - 6),
            ],
            2
        )

        pygame.draw.lines(
            screen,
            (130, 75, 175),
            False,
            [
                (center_x + 28, center_y + 17),
                (center_x + 34, center_y + 13),
                (center_x + 40, center_y + 16),
            ],
            2
        )

        # ==========================================
        # 10. MAŁE FIOLETOWE BŁYSKI
        # ==========================================

        pygame.draw.line(
            screen,
            (185, 115, 235),
            (center_x - 24, center_y - 31),
            (center_x - 21, center_y - 27),
            1
        )

        pygame.draw.line(
            screen,
            (185, 115, 235),
            (center_x - 21, center_y - 31),
            (center_x - 24, center_y - 27),
            1
        )

        pygame.draw.line(
            screen,
            (200, 135, 250),
            (center_x + 34, center_y - 2),
            (center_x + 38, center_y + 2),
            1
        )

        pygame.draw.line(
            screen,
            (200, 135, 250),
            (center_x + 38, center_y - 2),
            (center_x + 34, center_y + 2),
            1
        )

    def draw_v2_icon(self, screen, center_x, center_y):
        # ==========================================
        # BLOOD LEECH V2 — HEART OF BLOOD
        # MROCZNE SERCE WYSYSAJĄCE ŻYCIE
        # ==========================================

        import math
        import pygame

        # ==========================================
        # 1. KRWISTA POŚWIATA
        # ==========================================

        glow_size = 110

        glow = pygame.Surface(
            (glow_size, glow_size),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            glow,
            (180, 0, 20, 18),
            (55, 55),
            48
        )

        pygame.draw.circle(
            glow,
            (220, 0, 25, 25),
            (55, 55),
            35
        )

        pygame.draw.circle(
            glow,
            (255, 25, 45, 20),
            (55, 55),
            23
        )

        screen.blit(
            glow,
            (center_x - 55, center_y - 55)
        )

        # ==========================================
        # 2. FUNKCJA POMOCNICZA — PUNKT SERCA
        # ==========================================

        def heart_points(cx, cy, scale):
            return [
                (
                    int(cx),
                    int(cy + scale * 0.85)
                ),
                (
                    int(cx - scale * 0.75),
                    int(cy + scale * 0.15)
                ),
                (
                    int(cx - scale * 1.0),
                    int(cy - scale * 0.35)
                ),
                (
                    int(cx - scale * 0.9),
                    int(cy - scale * 0.8)
                ),
                (
                    int(cx - scale * 0.45),
                    int(cy - scale * 0.95)
                ),
                (
                    int(cx),
                    int(cy - scale * 0.55)
                ),
                (
                    int(cx + scale * 0.45),
                    int(cy - scale * 0.95)
                ),
                (
                    int(cx + scale * 0.9),
                    int(cy - scale * 0.8)
                ),
                (
                    int(cx + scale * 1.0),
                    int(cy - scale * 0.35)
                ),
                (
                    int(cx + scale * 0.75),
                    int(cy + scale * 0.15)
                ),
            ]

        # ==========================================
        # 3. CIENIE ZA SERCEM
        # ==========================================

        pygame.draw.polygon(
            screen,
            (35, 0, 10),
            heart_points(
                center_x + 2,
                center_y + 3,
                22
            )
        )

        # ==========================================
        # 4. CIEMNY KONTUR SERCA
        # ==========================================

        pygame.draw.polygon(
            screen,
            (65, 0, 13),
            heart_points(
                center_x,
                center_y,
                22
            )
        )

        # ==========================================
        # 5. GŁÓWNA POWŁOKA SERCA
        # ==========================================

        pygame.draw.polygon(
            screen,
            (145, 0, 24),
            heart_points(
                center_x,
                center_y - 1,
                19
            )
        )

        # ==========================================
        # 6. JAŚNIEJSZA LEWA STRONA SERCA
        # ==========================================

        pygame.draw.polygon(
            screen,
            (205, 12, 35),
            [
                (center_x, center_y - 10),
                (center_x - 7, center_y - 18),
                (center_x - 14, center_y - 15),
                (center_x - 17, center_y - 8),
                (center_x - 13, center_y + 1),
                (center_x - 5, center_y + 10),
                (center_x, center_y + 15),
            ]
        )

        # ==========================================
        # 7. CIEMNA PRAWA STRONA SERCA
        # ==========================================

        pygame.draw.polygon(
            screen,
            (105, 0, 20),
            [
                (center_x, center_y - 10),
                (center_x + 7, center_y - 18),
                (center_x + 14, center_y - 15),
                (center_x + 17, center_y - 8),
                (center_x + 13, center_y + 1),
                (center_x + 5, center_y + 10),
                (center_x, center_y + 15),
            ]
        )

        # ==========================================
        # 8. KRWISTE ODBICIE ŚWIATŁA
        # ==========================================

        pygame.draw.arc(
            screen,
            (255, 65, 75),
            (
                center_x - 17,
                center_y - 20,
                16,
                17
            ),
            math.radians(175),
            math.radians(285),
            2
        )

        pygame.draw.arc(
            screen,
            (190, 10, 35),
            (
                center_x + 1,
                center_y - 20,
                16,
                17
            ),
            math.radians(250),
            math.radians(350),
            2
        )

        # ==========================================
        # 9. ŻYŁY WYPEŁNIONE KRWIĄ
        # ==========================================

        vein_dark = (75, 0, 15)
        vein_light = (245, 25, 50)

        pygame.draw.lines(
            screen,
            vein_dark,
            False,
            [
                (center_x, center_y - 9),
                (center_x - 4, center_y - 3),
                (center_x - 9, center_y),
                (center_x - 11, center_y + 6),
            ],
            3
        )

        pygame.draw.lines(
            screen,
            vein_light,
            False,
            [
                (center_x, center_y - 9),
                (center_x - 4, center_y - 3),
                (center_x - 9, center_y),
                (center_x - 11, center_y + 6),
            ],
            1
        )

        pygame.draw.lines(
            screen,
            vein_dark,
            False,
            [
                (center_x, center_y - 5),
                (center_x + 5, center_y),
                (center_x + 9, center_y - 2),
                (center_x + 12, center_y + 3),
            ],
            3
        )

        pygame.draw.lines(
            screen,
            vein_light,
            False,
            [
                (center_x, center_y - 5),
                (center_x + 5, center_y),
                (center_x + 9, center_y - 2),
                (center_x + 12, center_y + 3),
            ],
            1
        )

        # ==========================================
        # 10. KRWISTY RDZEŃ
        # ==========================================

        pygame.draw.circle(
            screen,
            (90, 0, 15),
            (center_x, center_y - 2),
            6
        )

        pygame.draw.circle(
            screen,
            (200, 0, 30),
            (center_x, center_y - 2),
            4
        )

        pygame.draw.circle(
            screen,
            (255, 45, 55),
            (center_x - 1, center_y - 3),
            2
        )

        # ==========================================
        # 11. KROPLE KRWI POD SERCEM
        # ==========================================

        pygame.draw.polygon(
            screen,
            (85, 0, 12),
            [
                (center_x - 11, center_y + 11),
                (center_x - 14, center_y + 18),
                (center_x - 10, center_y + 22),
                (center_x - 7, center_y + 18),
            ]
        )

        pygame.draw.polygon(
            screen,
            (200, 0, 30),
            [
                (center_x - 11, center_y + 11),
                (center_x - 13, center_y + 17),
                (center_x - 10, center_y + 20),
                (center_x - 8, center_y + 17),
            ]
        )

        pygame.draw.polygon(
            screen,
            (85, 0, 12),
            [
                (center_x + 12, center_y + 10),
                (center_x + 9, center_y + 16),
                (center_x + 12, center_y + 19),
                (center_x + 15, center_y + 15),
            ]
        )

        pygame.draw.polygon(
            screen,
            (220, 8, 35),
            [
                (center_x + 12, center_y + 10),
                (center_x + 10, center_y + 15),
                (center_x + 12, center_y + 17),
                (center_x + 14, center_y + 15),
            ]
        )

        # ==========================================
        # 12. CZĄSTECZKI KRWI
        # ==========================================

        particles = [
            (-29, -17, 2, (255, 35, 55)),
            (28, -19, 2, (220, 10, 35)),
            (-31, 4, 2, (180, 0, 25)),
            (30, 8, 2, (255, 45, 60)),
            (3, -34, 2, (255, 70, 80)),
            (-22, 25, 1, (255, 30, 45)),
            (23, 27, 1, (220, 15, 40)),
            (0, 31, 2, (170, 0, 25)),
        ]

        for offset_x, offset_y, radius, color in particles:
            pygame.draw.circle(
                screen,
                color,
                (
                    int(center_x + offset_x),
                    int(center_y + offset_y)
                ),
                radius
            )

        # ==========================================
        # 13. MROCZNE SMUGI ENERGII
        # ==========================================

        pygame.draw.lines(
            screen,
            (125, 0, 25),
            False,
            [
                (center_x - 29, center_y - 5),
                (center_x - 35, center_y - 9),
                (center_x - 39, center_y - 5),
            ],
            2
        )

        pygame.draw.lines(
            screen,
            (160, 0, 30),
            False,
            [
                (center_x + 27, center_y - 4),
                (center_x + 34, center_y - 8),
                (center_x + 39, center_y - 3),
            ],
            2
        )

        # ==========================================
        # 14. MAŁE BŁYSKI KRWISTEJ ENERGII
        # ==========================================

        pygame.draw.line(
            screen,
            (255, 75, 85),
            (center_x - 30, center_y - 27),
            (center_x - 25, center_y - 27),
            2
        )

        pygame.draw.line(
            screen,
            (255, 75, 85),
            (center_x - 27, center_y - 30),
            (center_x - 27, center_y - 24),
            2
        )

        pygame.draw.line(
            screen,
            (255, 50, 65),
            (center_x + 29, center_y + 20),
            (center_x + 35, center_y + 20),
            2
        )

        pygame.draw.line(
            screen,
            (255, 50, 65),
            (center_x + 32, center_y + 17),
            (center_x + 32, center_y + 23),
            2
        )

    def draw_v1(self, screen):
        pass

    def draw_v2(self, screen):
        pass

    def draw_v3(self, screen):
        pass