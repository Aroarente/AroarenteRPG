#IMPORTOWANIE
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import subprocess
import sys
import math

try:
    import pygame
except:
    install("pygame")
    import pygame

import settings
import swords
import fruits
import guns

#IMPORTOWANIE - KLASA

class player:

    def __init__(
        self,
        max_hp=100,
        max_energy=10,
        x=settings.WIDTH // 2,
        y=settings.HEIGHT // 2 - 100
    ):
        self.max_hp = max_hp
        self.hp = self.max_hp

        self.max_energy = max_energy
        self.energy = self.max_energy

        self.x = x
        self.y = y

        # =========================
        # RUCH
        # =========================

        self.speed = 5

        # =========================
        # ANIMACJA CHODZENIA
        # =========================

        self.walking = False
        self.walk_animation = 0
        self.walk_animation_speed = 0.20

        # =========================
        # CUTSCENKI
        # =========================

        self.moving_to_target = False
        self.target_x = self.x
        self.target_y = self.y
        self.cutscene_speed = 3

    # =========================================================
    # USTAWIENIE POZYCJI
    # =========================================================

    def set_position(self, x, y):

        self.x = x
        self.y = y

    # =========================================================
    # RUCH GRACZA
    # =========================================================

    def move(self):

        # Jeżeli gracz jest sterowany przez cutscenkę,
        # normalne WASD nie działa
        if self.moving_to_target:
            self.walking = True
            return

        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        # =========================
        # WASD
        # =========================

        if keys[pygame.K_a]:
            dx -= 1

        if keys[pygame.K_d]:
            dx += 1

        if keys[pygame.K_w]:
            dy -= 1

        if keys[pygame.K_s]:
            dy += 1

        # =========================
        # STRZAŁKI
        # =========================

        if keys[pygame.K_LEFT]:
            dx -= 1

        if keys[pygame.K_RIGHT]:
            dx += 1

        if keys[pygame.K_UP]:
            dy -= 1

        if keys[pygame.K_DOWN]:
            dy += 1

        # =========================
        # RUCH
        # =========================

        if dx != 0 or dy != 0:

            # Normalizacja
            # Dzięki temu po skosie nie chodzimy szybciej
            length = math.sqrt(dx * dx + dy * dy)

            dx /= length
            dy /= length

            self.x += dx * self.speed
            self.y += dy * self.speed

            self.walking = True

        else:

            self.walking = False

        # =========================
        # OGRANICZENIE DO EKRANU
        # =========================

        self.x = max(
            40,
            min(
                self.x,
                settings.WIDTH - 40
            )
        )

        self.y = max(
            80,
            min(
                self.y,
                settings.HEIGHT - 100
            )
        )

    # =========================================================
    # RUCH DO PUNKTU - CUTSCENKI
    # =========================================================

    def move_to(self, x, y, speed=None):

        # Jeżeli podano speed, ustawiamy go
        if speed is None:
            speed = self.cutscene_speed

        self.target_x = x
        self.target_y = y
        self.cutscene_speed = speed

        self.moving_to_target = True

        dx = self.target_x - self.x
        dy = self.target_y - self.y

        distance = math.sqrt(
            dx * dx + dy * dy
        )

        # =========================
        # DOTARŁ DO CELU
        # =========================

        if distance <= speed:

            self.x = self.target_x
            self.y = self.target_y

            self.moving_to_target = False
            self.walking = False

            return True

        # =========================
        # RUCH DO CELU
        # =========================

        dx /= distance
        dy /= distance

        self.x += dx * speed
        self.y += dy * speed

        self.walking = True

        return False

    # =========================================================
    # ZATRZYMANIE CUTSCENKI
    # =========================================================

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

            # Powrót do pozycji stojącej
            self.walk_animation = 0

    # =========================================================
    # RYSOWANIE
    # =========================================================

    def draw(self, screen, size=1.0):

        if size <= 0:
            return

        # =========================================================
        # AKTUALIZACJA ANIMACJI
        # =========================================================

        self.update_animation()

        # =========================================================
        # POWIERZCHNIA POSTACI
        # =========================================================

        base_width = 120
        base_height = 190

        character_surface = pygame.Surface(
            (base_width, base_height),
            pygame.SRCALPHA
        )

        center_x = base_width // 2
        center_y = 85

        # Zapamiętaj pozycję gracza
        old_x = self.x
        old_y = self.y

        # Tymczasowa pozycja na powierzchni
        self.x = center_x
        self.y = center_y

        # =========================================================
        # ANIMACJA CHODZENIA
        # =========================================================

        if self.walking:

            leg_offset = math.sin(
                self.walk_animation
            ) * 5

            arm_offset = math.sin(
                self.walk_animation
            ) * 4

        else:

            leg_offset = 0
            arm_offset = 0

        # =========================================================
        # NOGI
        # =========================================================

        pygame.draw.polygon(
            character_surface,
            (45, 50, 70),
            [
                (self.x - 23, self.y + 42 + leg_offset),
                (self.x - 2, self.y + 42 - leg_offset),
                (self.x - 5, self.y + 83 - leg_offset),
                (self.x - 27, self.y + 83 + leg_offset)
            ]
        )

        pygame.draw.polygon(
            character_surface,
            (45, 50, 70),
            [
                (self.x + 2, self.y + 42 - leg_offset),
                (self.x + 23, self.y + 42 + leg_offset),
                (self.x + 27, self.y + 83 + leg_offset),
                (self.x + 5, self.y + 83 - leg_offset)
            ]
        )

        # =========================================================
        # BUTY
        # =========================================================

        pygame.draw.ellipse(
            character_surface,
            (30, 28, 25),
            (
                self.x - 32,
                self.y + 77 + leg_offset,
                35,
                17
            )
        )

        pygame.draw.ellipse(
            character_surface,
            (30, 28, 25),
            (
                self.x - 2,
                self.y + 77 - leg_offset,
                35,
                17
            )
        )

        # =========================================================
        # PLECAK
        # =========================================================

        pygame.draw.rect(
            character_surface,
            (115, 70, 35),
            (
                self.x - 38,
                self.y - 2,
                76,
                52
            )
        )

        pygame.draw.ellipse(
            character_surface,
            (135, 85, 40),
            (
                self.x - 38,
                self.y - 12,
                76,
                28
            )
        )

        # =========================================================
        # TUŁÓW
        # =========================================================

        pygame.draw.polygon(
            character_surface,
            (55, 105, 200),
            [
                (self.x - 30, self.y - 5),
                (self.x + 30, self.y - 5),
                (self.x + 27, self.y + 48),
                (self.x + 18, self.y + 55),
                (self.x - 18, self.y + 55),
                (self.x - 27, self.y + 48)
            ]
        )

        pygame.draw.polygon(
            character_surface,
            (70, 120, 220),
            [
                (self.x - 14, self.y),
                (self.x + 14, self.y),
                (self.x + 13, self.y + 43),
                (self.x - 13, self.y + 43)
            ]
        )

        # =========================================================
        # PAS
        # =========================================================

        pygame.draw.rect(
            character_surface,
            (90, 55, 30),
            (
                self.x - 29,
                self.y + 38,
                58,
                10
            )
        )

        pygame.draw.rect(
            character_surface,
            (220, 175, 55),
            (
                self.x - 6,
                self.y + 37,
                12,
                12
            )
        )

        # =========================================================
        # RAMIONA
        # =========================================================

        pygame.draw.circle(
            character_surface,
            (55, 105, 200),
            (
                self.x - 30,
                self.y + 5 + arm_offset
            ),
            17
        )

        pygame.draw.circle(
            character_surface,
            (55, 105, 200),
            (
                self.x + 30,
                self.y + 5 - arm_offset
            ),
            17
        )

        pygame.draw.line(
            character_surface,
            (55, 105, 200),
            (
                self.x - 38,
                self.y + 10 + arm_offset
            ),
            (
                self.x - 43,
                self.y + 38 + arm_offset
            ),
            14
        )

        pygame.draw.line(
            character_surface,
            (55, 105, 200),
            (
                self.x + 38,
                self.y + 10 - arm_offset
            ),
            (
                self.x + 43,
                self.y + 38 - arm_offset
            ),
            14
        )

        # =========================================================
        # DŁONIE
        # =========================================================

        pygame.draw.circle(
            character_surface,
            (225, 175, 125),
            (
                self.x - 43,
                self.y + 46 + arm_offset
            ),
            10
        )

        pygame.draw.circle(
            character_surface,
            (225, 175, 125),
            (
                self.x + 43,
                self.y + 46 - arm_offset
            ),
            10
        )

        # =========================================================
        # SZYJA
        # =========================================================

        pygame.draw.rect(
            character_surface,
            (220, 170, 120),
            (
                self.x - 11,
                self.y - 20,
                22,
                20
            )
        )

        # =========================================================
        # USZY
        # =========================================================

        pygame.draw.circle(
            character_surface,
            (205, 150, 105),
            (
                self.x - 31,
                self.y - 42
            ),
            10
        )

        pygame.draw.circle(
            character_surface,
            (205, 150, 105),
            (
                self.x + 31,
                self.y - 42
            ),
            10
        )

        # =========================================================
        # GŁOWA
        # =========================================================

        pygame.draw.ellipse(
            character_surface,
            (225, 175, 125),
            (
                self.x - 32,
                self.y - 75,
                64,
                70
            )
        )

        # =========================================================
        # WŁOSY
        # =========================================================

        pygame.draw.ellipse(
            character_surface,
            (55, 32, 18),
            (
                self.x - 35,
                self.y - 82,
                70,
                43
            )
        )

        pygame.draw.circle(
            character_surface,
            (55, 32, 18),
            (
                self.x - 29,
                self.y - 52
            ),
            13
        )

        pygame.draw.circle(
            character_surface,
            (55, 32, 18),
            (
                self.x + 29,
                self.y - 52
            ),
            13
        )

        pygame.draw.polygon(
            character_surface,
            (55, 32, 18),
            [
                (self.x - 31, self.y - 56),
                (self.x - 20, self.y - 70),
                (self.x - 7, self.y - 54),
                (self.x + 5, self.y - 69),
                (self.x + 18, self.y - 55),
                (self.x + 31, self.y - 62),
                (self.x + 25, self.y - 42),
                (self.x - 27, self.y - 42)
            ]
        )

        # =========================================================
        # BRWI
        # =========================================================

        pygame.draw.line(
            character_surface,
            (75, 40, 22),
            (
                self.x - 22,
                self.y - 44
            ),
            (
                self.x - 7,
                self.y - 47
            ),
            4
        )

        pygame.draw.line(
            character_surface,
            (75, 40, 22),
            (
                self.x + 7,
                self.y - 47
            ),
            (
                self.x + 22,
                self.y - 44
            ),
            4
        )

        # =========================================================
        # OCZY
        # =========================================================

        pygame.draw.ellipse(
            character_surface,
            (245, 245, 235),
            (
                self.x - 22,
                self.y - 40,
                16,
                11
            )
        )

        pygame.draw.ellipse(
            character_surface,
            (245, 245, 235),
            (
                self.x + 6,
                self.y - 40,
                16,
                11
            )
        )

        pygame.draw.circle(
            character_surface,
            (35, 45, 55),
            (
                self.x - 14,
                self.y - 35
            ),
            5
        )

        pygame.draw.circle(
            character_surface,
            (35, 45, 55),
            (
                self.x + 14,
                self.y - 35
            ),
            5
        )

        pygame.draw.circle(
            character_surface,
            (255, 255, 255),
            (
                self.x - 12,
                self.y - 37
            ),
            2
        )

        pygame.draw.circle(
            character_surface,
            (255, 255, 255),
            (
                self.x + 16,
                self.y - 37
            ),
            2
        )

        # =========================================================
        # NOS
        # =========================================================

        pygame.draw.polygon(
            character_surface,
            (195, 140, 95),
            [
                (self.x, self.y - 37),
                (self.x - 6, self.y - 23),
                (self.x + 7, self.y - 23)
            ]
        )

        # =========================================================
        # USTA
        # =========================================================

        pygame.draw.arc(
            character_surface,
            (110, 55, 45),
            (
                self.x - 10,
                self.y - 25,
                20,
                12
            ),
            0,
            3.14,
            2
        )

        # =========================================================
        # KATANA
        # =========================================================

        katana = swords.Katana()

        if katana.eqquiped:
            katana.draw(
                character_surface,
                self.x + 43,
                self.y + 30 - arm_offset
            )

        # =========================================================
        # PRZYWRÓĆ POZYCJĘ GRACZA
        # =========================================================

        self.x = old_x
        self.y = old_y

        # =========================================================
        # SKALOWANIE CAŁEJ POSTACI
        # =========================================================

        scaled_width = max(
            1,
            int(base_width * size)
        )

        scaled_height = max(
            1,
            int(base_height * size)
        )

        scaled_character = pygame.transform.smoothscale(
            character_surface,
            (scaled_width, scaled_height)
        )

        # =========================================================
        # RYSOWANIE NA EKRANIE
        # =========================================================

        screen.blit(
            scaled_character,
            (
                int(old_x - scaled_width / 2),
                int(old_y - center_y * size)
            )
        )