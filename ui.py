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
import swords
import guns
import utilities
import player
import fruits
import elementals

katana = swords.Katana()
Player = player.player()


def format_number(n):
    if n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
        if n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} TQC"
        elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} BQC"
        elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} MQC"
        elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} KQC"
        else:
            return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} QC"

    elif n >= 1_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} C"

    elif n >= 1_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} QD"

    elif n >= 1_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} D"

    elif n >= 1_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} QN"

    elif n >= 1_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} N"

    elif n >= 1_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} O"

    elif n >= 1_000_000_000_000_000_000_000_000_000_000_000_000:
        return f"{n/1_000_000_000_000_000_000_000_000_000_000_000_000_000_000:.1f} QS"

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


pygame.font.init()

data = save.load_game()

last_save = data["variables"]["last_save"]

if last_save not in data["saves"]:
    last_save = "save1"

save_data = data["saves"][last_save]

font = pygame.font.Font(None, (75))
font2 = pygame.font.Font(None, (50))
font3 = pygame.font.Font(None, (35))

font_1 = pygame.font.SysFont(
    "Segoe UI Emoji",
    (75)
)

font_2 = pygame.font.SysFont(
    "Segoe UI Emoji",
    (50)
)

font_3 = pygame.font.SysFont(
    "Segoe UI Emoji",
    (35)
)

font_4 = pygame.font.SysFont(
    "Cambria Math",
    (35)
)

def draw_multiline_text_with_frame(
    screen,
    lines,
    font,
    center,
    animation=False,
    color=(60, 120, 200)
):

    if animation:

        if not hasattr(
            draw_multiline_text_with_frame,
            "animation_start"
        ):
            draw_multiline_text_with_frame.animation_start = (
                pygame.time.get_ticks()
            )

        elapsed = (
            pygame.time.get_ticks()
            - draw_multiline_text_with_frame.animation_start
        )

        animation_duration = 300

        progress = min(
            elapsed / animation_duration,
            1.0
        )

        progress = 1 - (1 - progress) ** 3

    else:
        progress = 1.0

    rendered_lines = []

    for line in lines:

        rendered_lines.append(
            font.render(
                line,
                True,
                (255, 255, 255)
            )
        )

    spacing = (10)

    max_width = max(
        text.get_width()
        for text in rendered_lines
    )

    total_height = (
        sum(
            text.get_height()
            for text in rendered_lines
        )
        +
        spacing * (len(rendered_lines) - 1)
    )

    padding_x = (25)
    padding_y = (20)

    full_width = max_width + padding_x * 2
    full_height = total_height + padding_y * 2

    frame_width = int(
        full_width * progress
    )

    frame_height = int(
        full_height * progress
    )

    frame_rect = pygame.Rect(
        center[0] - frame_width // 2,
        center[1] - frame_height // 2,
        frame_width,
        frame_height
    )

    shadow_rect = frame_rect.copy()
    shadow_rect.y += (7)

    pygame.draw.rect(
        screen,
        (5, 5, 10),
        shadow_rect,
        border_radius=(12)
    )

    pygame.draw.rect(
        screen,
        (10, 20, 70),
        frame_rect,
        border_radius=(12)
    )

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

    y = center[1] - total_height // 2

    for text_surface in rendered_lines:

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

        text_rect = animated_text.get_rect(
            center=(
                center[0],
                y + text_surface.get_height() // 2
            )
        )

        screen.blit(
            animated_text,
            text_rect
        )

        y += (
            text_surface.get_height()
            + spacing
        )


class SquareButton:

    def __init__(
        self,
        x,
        y,
        size,
        icon,
        key
    ):

        self.x = x
        self.y = y
        self.size = size
        self.icon = icon
        self.key = key

        self.font = pygame.font.SysFont(
            "Segoe UI Emoji",
            (60)
        )

    def is_hovered(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()

        x = (self.x)
        y = (self.y)
        size = (self.size)

        return (
            x <= mouse_x <= x + size
            and
            y <= mouse_y <= y + size
        )

    def clicked(self):

        return self.is_hovered()

    def draw(self, screen):

        x = (self.x)
        y = (self.y)
        size = (self.size)

        if self.is_hovered():
            color = (80, 150, 220)
        else:
            color = (55, 105, 160)

        pygame.draw.rect(
            screen,
            (30, 30, 30),
            (
                int(x),
                int(y + (6)),
                int(size),
                int(size)
            ),
            border_radius=(12)
        )

        pygame.draw.rect(
            screen,
            (30, 65, 100),
            (
                int(x),
                int(y),
                int(size),
                int(size)
            ),
            border_radius=(12)
        )

        pygame.draw.rect(
            screen,
            color,
            (
                int(x + (4)),
                int(y + (4)),
                int(size - (8)),
                int(size - (8))
            ),
            border_radius=(9)
        )

        icon_surface = self.font.render(
            self.icon,
            True,
            (255, 255, 255)
        )

        icon_rect = icon_surface.get_rect(
            center=(
                int(x + size / 2),
                int(y + size / 2)
            )
        )

        screen.blit(
            icon_surface,
            icon_rect
        )

        key_name = pygame.key.name(
            self.key
        ).upper()

        key_surface = pygame.font.Font(
            None,
            (28)
        ).render(
            key_name,
            True,
            (255, 255, 255)
        )

        key_rect = key_surface.get_rect(
            bottomright=(
                int(
                    x
                    + size
                    - (8)
                ),
                int(
                    y
                    + size
                    - (8)
                )
            )
        )

        screen.blit(
            key_surface,
            key_rect
        )


def draw_custom_frame(
    screen,
    x,
    y,
    width,
    height,
    blocked=False,
    energy=100,
    max_energy=100,
    health=100,
    max_health=100,
    v3_enabled=False,
    bow_enabled=False
):
    import pygame
    import math

    # ==========================================
    # USTAWIENIA
    # ==========================================

    cut = 35
    shadow_x = 16
    shadow_y = 19
    radius = 18
    end_length = 140

    # ==========================================
    # ZAOKRĄGLENIE ROGU
    # ==========================================

    def rounded_corner(p1, corner, p2, radius, steps=10):
        cx, cy = corner

        dx1 = p1[0] - cx
        dy1 = p1[1] - cy
        length1 = math.sqrt(dx1 ** 2 + dy1 ** 2)

        if length1 == 0:
            return [corner]

        dx1 /= length1
        dy1 /= length1

        dx2 = p2[0] - cx
        dy2 = p2[1] - cy
        length2 = math.sqrt(dx2 ** 2 + dy2 ** 2)

        if length2 == 0:
            return [corner]

        dx2 /= length2
        dy2 /= length2

        start = (
            cx + dx1 * radius,
            cy + dy1 * radius
        )

        end = (
            cx + dx2 * radius,
            cy + dy2 * radius
        )

        result = [start]

        for i in range(1, steps + 1):
            t = i / steps

            a = (1 - t) ** 2
            b = 2 * (1 - t) * t
            c = t ** 2

            px = (
                a * start[0]
                + b * cx
                + c * end[0]
            )

            py = (
                a * start[1]
                + b * cy
                + c * end[1]
            )

            result.append((px, py))

        return result

    # ==========================================
    # GŁÓWNY KSZTAŁT RAMKI
    # ==========================================

    points = [
        (x, y + cut),
        (x + width * 0.20 + end_length, y + cut),
        (x + width * 0.20 + cut + end_length, y),
        (x + width * 0.80 - cut - end_length, y),
        (x + width * 0.80 - end_length, y + cut),
        (x + width, y + cut),
        (x + width, y + height - cut),
        (x + width * 0.80 - end_length, y + height - cut),
        (x + width * 0.80 - cut - end_length, y + height),
        (x + width * 0.20 + cut + end_length, y + height),
        (x + width * 0.20 + end_length, y + height - cut),
        (x, y + height - cut)
    ]

    # ==========================================
    # ZAOKRĄGLONA GŁÓWNA RAMKA
    # ==========================================

    rounded_points = []

    rounded_points.extend(
        rounded_corner(points[11], points[0], points[1], radius)
    )

    rounded_points.extend([
        points[1],
        points[2],
        points[3],
        points[4]
    ])

    rounded_points.extend(
        rounded_corner(points[4], points[5], points[6], radius)
    )

    rounded_points.extend(
        rounded_corner(points[5], points[6], points[7], radius)
    )

    rounded_points.extend([
        points[7],
        points[8],
        points[9],
        points[10]
    ])

    rounded_points.extend(
        rounded_corner(points[10], points[11], points[0], radius)
    )

    # ==========================================
    # CIEŃ RAMKI
    # ==========================================

    shadow_size = 8

    shadow_points = [
        (
            px + shadow_x - shadow_size,
            py + shadow_y - shadow_size
        )
        for px, py in rounded_points
    ]

    pygame.draw.polygon(
        screen,
        (5, 10, 15),
        shadow_points
    )

    # ==========================================
    # GŁÓWNA RAMKA
    # ==========================================

    pygame.draw.polygon(
        screen,
        (15, 25, 40),
        rounded_points
    )

    # ==========================================
    # WEWNĘTRZNA CZĘŚĆ RAMKI
    # ==========================================

    border = 4
    inner_cut = 31

    inner_points = [
        (x + border, y + inner_cut),
        (x + width * 0.20 + end_length, y + inner_cut),
        (x + width * 0.20 + inner_cut + end_length, y + border),
        (x + width * 0.80 - inner_cut - end_length, y + border),
        (x + width * 0.80 - end_length, y + inner_cut),
        (x + width - border, y + inner_cut),
        (x + width - border, y + height - inner_cut),
        (x + width * 0.80 - end_length, y + height - inner_cut),
        (x + width * 0.80 - inner_cut - end_length, y + height - border),
        (x + width * 0.20 + inner_cut + end_length, y + height - border),
        (x + width * 0.20 + end_length, y + height - inner_cut),
        (x + border, y + height - inner_cut)
    ]

    inner_radius = 14
    rounded_inner = []

    rounded_inner.extend(
        rounded_corner(
            inner_points[11],
            inner_points[0],
            inner_points[1],
            inner_radius
        )
    )

    rounded_inner.extend([
        inner_points[1],
        inner_points[2],
        inner_points[3],
        inner_points[4]
    ])

    rounded_inner.extend(
        rounded_corner(
            inner_points[4],
            inner_points[5],
            inner_points[6],
            inner_radius
        )
    )

    rounded_inner.extend(
        rounded_corner(
            inner_points[5],
            inner_points[6],
            inner_points[7],
            inner_radius
        )
    )

    rounded_inner.extend([
        inner_points[7],
        inner_points[8],
        inner_points[9],
        inner_points[10]
    ])

    rounded_inner.extend(
        rounded_corner(
            inner_points[10],
            inner_points[11],
            inner_points[0],
            inner_radius
        )
    )

    pygame.draw.polygon(
        screen,
        (30, 55, 85),
        rounded_inner
    )

    # ==========================================
    # USTAWIENIA PRZYCISKÓW FRUIT I ELEMENTAL
    # ==========================================

    small_button_width = 80
    small_button_height = 80
    small_button_gap = 35

    small_button_color = (18, 32, 48)
    small_button_border = (55, 85, 115)

    buttons_y = y + cut + 65

    # ==========================================
    # NAZWY SKILLI WYPOSAŻONEGO OWOCU
    # ==========================================

    fruit_top_texts = [
        "Skill 1",
        "Skill 2",
        "Skill 3"
    ]

    for fruit in vars(fruits).values():
        if (
            isinstance(fruit, type)
            and issubclass(fruit, fruits.Fruits)
            and fruit is not fruits.Fruits
        ):
            fruit_obj = fruit()

            if getattr(fruit_obj, "eqquiped", False):
                fruit_top_texts = [
                    fruit_obj.s1_name,
                    fruit_obj.s2_name,
                    fruit_obj.s3_name
                ]
                break

    fruit_bottom_texts = [
        "G",
        "C",
        "Z"
    ]

    # ==========================================
    # TEKSTY ELEMENTALU
    # ==========================================

    elemental_top_texts = [
        "V1",
        "V2",
        "Utility"
    ]

    elemental_bottom_texts = [
        "X",
        "V",
        "F"
    ]

    # ==========================================
    # KOLORY I CZCIONKA
    # ==========================================

    text_color = (230, 240, 255)
    text_font = pygame.font.Font(None, 28)

    # ==========================================
    # SPRAWDZANIE WYPOSAŻONEGO FRUIT
    # ==========================================

    fruit_equipped = False

    for fruit_class in vars(fruits).values():
        if (
            isinstance(fruit_class, type)
            and issubclass(fruit_class, fruits.Fruits)
            and fruit_class is not fruits.Fruits
        ):
            if getattr(fruit_class(), "eqquiped", False):
                fruit_equipped = True
                break

    # ==========================================
    # SPRAWDZANIE WYPOSAŻONEGO UTILITY
    # ==========================================

    utility_equipped = False

    for utility_class in vars(utilities).values():
        if (
            isinstance(utility_class, type)
            and issubclass(utility_class, utilities.Utilities)
            and utility_class is not utilities.Utilities
        ):
            if getattr(utility_class(), "eqquiped", False):
                utility_equipped = True
                break

    # ==========================================
    # ODCZYT AKTYWNEGO SAVE
    # ==========================================

    elemental_data = save.load_game() or {}

    elemental_last_save = (
        elemental_data
        .get("variables", {})
        .get("last_save", "save1")
    )

    elemental_save = (
        elemental_data
        .get("saves", {})
        .get(elemental_last_save, {})
    )

    equipped_elemental_name = str(
        elemental_save.get("elemental", "")
    ).strip().casefold()

    # ==========================================
    # POZIOM ELEMENTALU
    # elemental_lvl == 1 -> V2 ZABLOKOWANE
    # elemental_lvl >= 2 -> V2 ODBLOKOWANE
    # ==========================================

    try:
        elemental_lvl = int(
            elemental_save.get("elemental_lvl", 1)
        )
    except (TypeError, ValueError):
        elemental_lvl = 1

    # ==========================================
    # WYSZUKIWANIE ELEMENTALU Z SAVE
    # ==========================================

    equipped_elemental = None

    if equipped_elemental_name not in (
        "",
        "none",
        "no elemental",
        "null"
    ):
        for elemental_class in vars(elementals).values():
            if (
                isinstance(elemental_class, type)
                and issubclass(elemental_class, elementals.Elementals)
                and elemental_class is not elementals.Elementals
            ):
                elemental_obj = elemental_class()

                class_name = (
                    elemental_class.__name__
                    .strip()
                    .casefold()
                )

                object_name = str(
                    getattr(elemental_obj, "name", "")
                ).strip().casefold()

                if equipped_elemental_name in (
                    class_name,
                    object_name
                ):
                    equipped_elemental = elemental_obj
                    break

    # ==========================================
    # KONFIGURACJA OBU GRUP PRZYCISKÓW
    # ==========================================

    button_groups = [
        (
            x + width * 0.18,
            fruit_top_texts,
            fruit_bottom_texts
        ),
        (
            x + width * 0.82,
            elemental_top_texts,
            elemental_bottom_texts
        )
    ]

    # ==========================================
    # RYSOWANIE PRZYCISKÓW FRUIT I ELEMENTAL
    # ==========================================

    for group_index, (
        group_center_x,
        top_texts,
        bottom_texts
    ) in enumerate(button_groups):

        total_width = (
            small_button_width * 3
            + small_button_gap * 2
        )

        start_x = group_center_x - total_width // 2

        for i in range(3):
            button_x = start_x + i * (
                small_button_width + small_button_gap
            )

            button_center_x = (
                button_x + small_button_width // 2
            )

            button_center_y = (
                buttons_y + small_button_height // 2
            )

            # ==========================================
            # CIEŃ PRZYCISKU
            # ==========================================

            pygame.draw.rect(
                screen,
                (5, 10, 18),
                (
                    button_x + 3,
                    buttons_y + 4,
                    small_button_width,
                    small_button_height
                ),
                border_radius=7
            )

            # ==========================================
            # TŁO PRZYCISKU
            # ==========================================

            pygame.draw.rect(
                screen,
                small_button_color,
                (
                    button_x,
                    buttons_y,
                    small_button_width,
                    small_button_height
                ),
                border_radius=7
            )

            # ==========================================
            # OBRAMOWANIE PRZYCISKU
            # ==========================================

            pygame.draw.rect(
                screen,
                small_button_border,
                (
                    button_x,
                    buttons_y,
                    small_button_width,
                    small_button_height
                ),
                width=2,
                border_radius=7
            )

            # ==========================================
            # IKONY ELEMENTALU
            # PRZYCISK 1 = V1
            # PRZYCISK 2 = V2
            # ==========================================

            if (
                group_index == 1
                and equipped_elemental is not None
            ):
                if i == 0 and hasattr(
                    equipped_elemental,
                    "draw_v1_icon"
                ):
                    equipped_elemental.draw_v1_icon(
                        screen,
                        button_center_x,
                        button_center_y
                    )

                elif i == 1 and hasattr(
                    equipped_elemental,
                    "draw_v2_icon"
                ):
                    equipped_elemental.draw_v2_icon(
                        screen,
                        button_center_x,
                        button_center_y
                    )

            # ==========================================
            # SPRAWDZANIE, CZY PRZYCISK MA BYĆ ZABLOKOWANY
            # ==========================================

            locked = False

            # Pierwsze trzy przyciski: brak wyposażonego owocu
            if group_index == 0 and not fruit_equipped:
                locked = True

            # Ostatni przycisk grupy elemental: brak utility
            if (
                group_index == 1
                and i == 2
                and not utility_equipped
            ):
                locked = True

            # Drugi przycisk elemental (V2):
            # blokada na poziomie 1, odblokowanie od poziomu 2
            if (
                group_index == 1
                and i == 1
                and elemental_lvl <= 1
            ):
                locked = True

            # ==========================================
            # RYSOWANIE KŁÓDKI
            # ==========================================

            if locked:
                lock_center_x = button_center_x
                lock_center_y = button_center_y

                # Pałąk kłódki
                pygame.draw.arc(
                    screen,
                    (255, 195, 65),
                    (
                        lock_center_x - 9,
                        lock_center_y - 16,
                        18,
                        20
                    ),
                    0,
                    math.pi,
                    3
                )

                # Korpus kłódki
                pygame.draw.rect(
                    screen,
                    (255, 195, 65),
                    (
                        lock_center_x - 12,
                        lock_center_y - 5,
                        24,
                        20
                    ),
                    border_radius=4
                )

                # Obramowanie
                pygame.draw.rect(
                    screen,
                    (255, 230, 160),
                    (
                        lock_center_x - 12,
                        lock_center_y - 5,
                        24,
                        20
                    ),
                    width=2,
                    border_radius=4
                )

                # Dziurka zamka
                pygame.draw.circle(
                    screen,
                    (30, 45, 60),
                    (
                        lock_center_x,
                        lock_center_y + 2
                    ),
                    3
                )

                pygame.draw.line(
                    screen,
                    (30, 45, 60),
                    (
                        lock_center_x,
                        lock_center_y + 4
                    ),
                    (
                        lock_center_x,
                        lock_center_y + 8
                    ),
                    2
                )

            # ==========================================
            # TEKST NAD PRZYCISKIEM
            # ==========================================

            top_text = text_font.render(
                str(top_texts[i]),
                True,
                text_color
            )

            screen.blit(
                top_text,
                top_text.get_rect(
                    center=(
                        button_center_x,
                        buttons_y - 18
                    )
                )
            )

            # ==========================================
            # TEKST POD PRZYCISKIEM
            # ==========================================

            bottom_text = text_font.render(
                str(bottom_texts[i]),
                True,
                text_color
            )

            screen.blit(
                bottom_text,
                bottom_text.get_rect(
                    center=(
                        button_center_x,
                        buttons_y + small_button_height + 18
                    )
                )
            )

    # ==========================================
    # NAPISY NA GÓRZE RAMKI
    # ==========================================

    data = save.load_game() or {}

    last_save = (
        data.get("variables", {})
        .get("last_save", "save1")
    )

    save_data = (
        data.get("saves", {})
        .get(last_save, {})
    )

    current_fruit = str(
        save_data.get("current_fruit", "")
    )

    if current_fruit == "":
        left_title = "No fruit"
    else:
        left_title = current_fruit

    right_title = str(
        save_data.get("elemental", "None")
    ).capitalize()

    title_font = pygame.font.Font(None, 38)
    title_color = (230, 240, 255)

    # Lewy napis
    left_text = title_font.render(
        left_title,
        True,
        title_color
    )

    screen.blit(
        left_text,
        left_text.get_rect(
            center=(
                x + width * 0.18,
                y + cut // 2 + 35
            )
        )
    )

    # Prawy napis
    right_text = title_font.render(
        right_title,
        True,
        title_color
    )

    screen.blit(
        right_text,
        right_text.get_rect(
            center=(
                x + width * 0.82,
                y + cut // 2 + 35
            )
        )
    )

    # ==========================================
    # ENERGY
    # ==========================================

    bar_width = 220
    bar_height = 14

    bar_x = x + (width - bar_width) // 2
    energy_y = y + 8

    energy_icon = font_3.render(
        "⚡",
        True,
        (255, 220, 60)
    )

    screen.blit(
        energy_icon,
        (bar_x - 40, energy_y - 12)
    )

    pygame.draw.rect(
        screen,
        (10, 20, 30),
        (bar_x, energy_y, bar_width, bar_height),
        border_radius=7
    )

    energy_ratio = 0

    if max_energy > 0:
        energy_ratio = max(
            0,
            min(energy / max_energy, 1)
        )

    energy_width = int(bar_width * energy_ratio)

    if energy_width > 0:
        pygame.draw.rect(
            screen,
            (255, 210, 50),
            (
                bar_x,
                energy_y,
                energy_width,
                bar_height
            ),
            border_radius=7
        )

    energy_text = font3.render(
        f"{int(energy)}/{int(max_energy)}",
        True,
        (255, 255, 255)
    )

    screen.blit(
        energy_text,
        energy_text.get_rect(
            center=(
                bar_x + bar_width // 2,
                energy_y + bar_height // 2
            )
        )
    )

    # ==========================================
    # HEALTH
    # ==========================================

    health_y = y + height - 22

    health_icon = font_3.render(
        "❤️",
        True,
        (255, 80, 80)
    )

    screen.blit(
        health_icon,
        (bar_x - 40, health_y - 12)
    )

    pygame.draw.rect(
        screen,
        (10, 20, 30),
        (bar_x, health_y, bar_width, bar_height),
        border_radius=7
    )

    health_ratio = 0

    if max_health > 0:
        health_ratio = max(
            0,
            min(health / max_health, 1)
        )

    health_width = int(bar_width * health_ratio)

    if health_width > 0:
        pygame.draw.rect(
            screen,
            (80, 220, 100),
            (
                bar_x,
                health_y,
                health_width,
                bar_height
            ),
            border_radius=7
        )

    health_text = font3.render(
        f"{int(health)}/{int(max_health)}",
        True,
        (255, 255, 255)
    )

    screen.blit(
        health_text,
        health_text.get_rect(
            center=(
                bar_x + bar_width // 2,
                health_y + bar_height // 2
            )
        )
    )

    # ==========================================
    # PRZYCISKI UMIEJĘTNOŚCI
    # ==========================================

    button_size = 54
    group_width = 125
    buttons_per_row = 3

    total_width = group_width * buttons_per_row
    row_height = 75
    total_height = row_height * 2

    buttons_start_x = (
        x + (width - total_width) // 2 + 15
    )

    buttons_start_y = (
        y + (height - total_height) // 2 + 10
    )

    button_color = (20, 38, 58)
    button_border = (100, 155, 195)
    icon_color = (235, 240, 250)
    key_color = (255, 220, 100)

    skill_buttons = [
        ("sword", "W", True),
        ("v3", "E", v3_enabled),
        ("bow", "S", bow_enabled),
        ("left", "A", True),
        ("shield", "Q", True),
        ("right", "D", True)
    ]

    key_font = pygame.font.Font(None, 30)

    for i, (skill, key, enabled) in enumerate(skill_buttons):
        row = i // 3
        col = i % 3

        button_x = buttons_start_x + col * group_width
        skill_button_y = buttons_start_y + row * row_height

        # Cień przycisku
        pygame.draw.rect(
            screen,
            (5, 10, 18),
            (
                button_x + 4,
                skill_button_y + 5,
                button_size,
                button_size
            ),
            border_radius=10
        )

        # Tło przycisku
        pygame.draw.rect(
            screen,
            button_color,
            (
                button_x,
                skill_button_y,
                button_size,
                button_size
            ),
            border_radius=10
        )

        # Obramowanie
        pygame.draw.rect(
            screen,
            button_border,
            (
                button_x,
                skill_button_y,
                button_size,
                button_size
            ),
            width=2,
            border_radius=10
        )

        skill_center_x = button_x + button_size // 2
        skill_center_y = skill_button_y + button_size // 2

        # ==========================================
        # MIECZ - W
        # ==========================================

        if skill == "sword":
            sword_icon = font_3.render(
                "⚔",
                True,
                icon_color
            )

            screen.blit(
                sword_icon,
                sword_icon.get_rect(
                    center=(skill_center_x, skill_center_y)
                )
            )

        # ==========================================
        # V3 - E
        # ==========================================

        elif skill == "v3":
            v3_text = font3.render(
                "V3",
                True,
                (100, 220, 255)
            )

            screen.blit(
                v3_text,
                v3_text.get_rect(
                    center=(skill_center_x, skill_center_y)
                )
            )

        # ==========================================
        # ŁUK - S
        # ==========================================

        elif skill == "bow":
            pygame.draw.line(
                screen,
                (225, 225, 225),
                (
                    skill_center_x + 5,
                    skill_center_y - 20
                ),
                (
                    skill_center_x + 5,
                    skill_center_y + 20
                ),
                2
            )

            pygame.draw.arc(
                screen,
                (190, 145, 85),
                (
                    skill_center_x - 17,
                    skill_center_y - 20,
                    34,
                    40
                ),
                -math.pi / 2,
                math.pi / 2,
                4
            )

            pygame.draw.line(
                screen,
                icon_color,
                (
                    skill_center_x - 17,
                    skill_center_y
                ),
                (
                    skill_center_x + 20,
                    skill_center_y
                ),
                3
            )

            pygame.draw.polygon(
                screen,
                icon_color,
                [
                    (skill_center_x + 20, skill_center_y),
                    (skill_center_x + 11, skill_center_y - 6),
                    (skill_center_x + 11, skill_center_y + 6)
                ]
            )

        # ==========================================
        # STRZAŁKA W LEWO - A
        # ==========================================

        elif skill == "left":
            pygame.draw.polygon(
                screen,
                icon_color,
                [
                    (skill_center_x - 17, skill_center_y),
                    (skill_center_x + 7, skill_center_y - 17),
                    (skill_center_x + 7, skill_center_y - 7),
                    (skill_center_x + 19, skill_center_y - 7),
                    (skill_center_x + 19, skill_center_y + 7),
                    (skill_center_x + 7, skill_center_y + 7),
                    (skill_center_x + 7, skill_center_y + 17)
                ]
            )

        # ==========================================
        # TARCZA - Q
        # ==========================================

        elif skill == "shield":
            pygame.draw.polygon(
                screen,
                (90, 160, 220),
                [
                    (skill_center_x, skill_center_y - 21),
                    (skill_center_x + 17, skill_center_y - 14),
                    (skill_center_x + 14, skill_center_y + 7),
                    (skill_center_x, skill_center_y + 21),
                    (skill_center_x - 14, skill_center_y + 7),
                    (skill_center_x - 17, skill_center_y - 14)
                ]
            )

            pygame.draw.polygon(
                screen,
                icon_color,
                [
                    (skill_center_x, skill_center_y - 14),
                    (skill_center_x + 10, skill_center_y - 10),
                    (skill_center_x + 8, skill_center_y + 5),
                    (skill_center_x, skill_center_y + 14),
                    (skill_center_x - 8, skill_center_y + 5),
                    (skill_center_x - 10, skill_center_y - 10)
                ],
                width=2
            )

        # ==========================================
        # STRZAŁKA W PRAWO - D
        # ==========================================

        elif skill == "right":
            pygame.draw.polygon(
                screen,
                icon_color,
                [
                    (skill_center_x + 17, skill_center_y),
                    (skill_center_x - 7, skill_center_y - 17),
                    (skill_center_x - 7, skill_center_y - 7),
                    (skill_center_x - 19, skill_center_y - 7),
                    (skill_center_x - 19, skill_center_y + 7),
                    (skill_center_x - 7, skill_center_y + 7),
                    (skill_center_x - 7, skill_center_y + 17)
                ]
            )

        # ==========================================
        # KŁÓDKA UMIEJĘTNOŚCI
        # ==========================================

        if not enabled:
            lock_x = button_x + button_size - 13
            lock_y = skill_button_y + button_size - 13

            pygame.draw.arc(
                screen,
                (255, 195, 65),
                (
                    lock_x - 6,
                    lock_y - 13,
                    12,
                    14
                ),
                0,
                math.pi,
                3
            )

            pygame.draw.rect(
                screen,
                (255, 195, 65),
                (
                    lock_x - 9,
                    lock_y - 5,
                    18,
                    15
                ),
                border_radius=4
            )

            pygame.draw.rect(
                screen,
                (255, 230, 160),
                (
                    lock_x - 9,
                    lock_y - 5,
                    18,
                    15
                ),
                width=1,
                border_radius=4
            )

            pygame.draw.circle(
                screen,
                (30, 45, 60),
                (lock_x, lock_y + 1),
                2
            )

            pygame.draw.line(
                screen,
                (30, 45, 60),
                (lock_x, lock_y + 2),
                (lock_x, lock_y + 5),
                2
            )

        # ==========================================
        # KLAWISZ OBOK PRZYCISKU
        # ==========================================

        key_text = key_font.render(
            key,
            True,
            key_color
        )

        key_rect = key_text.get_rect(
            midleft=(
                button_x + button_size + 5,
                skill_button_y + button_size // 2
            )
        )

        screen.blit(key_text, key_rect)

    # ==========================================
    # KŁÓDKA - CAŁA RAMKA ZABLOKOWANA
    # ==========================================

    if blocked:
        lock_x = x + 27
        lock_y = y + 45

        lock_width = 32
        lock_height = 38

        pygame.draw.rect(
            screen,
            (210, 180, 70),
            (
                lock_x,
                lock_y + 15,
                lock_width,
                lock_height - 15
            ),
            border_radius=6
        )

        pygame.draw.rect(
            screen,
            (255, 225, 150),
            (
                lock_x,
                lock_y + 15,
                lock_width,
                lock_height - 15
            ),
            width=2,
            border_radius=6
        )

        pygame.draw.arc(
            screen,
            (210, 180, 70),
            (
                lock_x + 6,
                lock_y,
                lock_width - 12,
                25
            ),
            0,
            math.pi,
            6
        )

        pygame.draw.circle(
            screen,
            (30, 55, 85),
            (
                lock_x + lock_width // 2,
                lock_y + 28
            ),
            4
        )


class UI:

    def __init__(self):

        self.money = save_data["money"]
        self.fragments = save_data["fragments"]

        self.exp = save_data["exp"]
        self.max_exp = save_data["max_exp"]
        self.lvl = save_data["lvl"]
        self.prestige_lvl = save_data["prestige_lvl"]
        self.to_add_points = 0

        self.level_up_active = False
        self.level_up_start = 0
        self.level_up_level = 0
        self.level_up_particles = []

        self.health = save_data["health"]
        self.max_health = save_data["max_health"]

        self.energy = save_data["energy"]
        self.max_energy = save_data["max_energy"]

        self.stats_points_to_give = save_data["stats_points_to_give"]
        self.health_and_def_stats = save_data["health_and_def_stats"]
        self.dmg_and_forget_resistance_stats = save_data["dmg_and_forget_resistance_stats"]
        self.energy_stats = save_data["energy_stats"]
        self.combo_stats = save_data["combo_stats"]

        self.elemental = save_data["elemental"]
        self.name = save_data["character_name"]
        self.difficulty = save_data["difficulty"]

        self.current_place = save_data["current_world"]
        self.places_unlocked = save_data["worlds_unlocked"]

        self.place_position_x = save_data["current_map_on_x"]
        self.place_position_y = save_data["current_map_on_y"]

        self.map_position_x = save_data["current_location_x"]
        self.map_position_y = save_data["current_location_y"]

        self.fruit = save_data["current_fruit"]
        self.fighting_style = save_data["current_fighting_style"]
        self.gun = save_data["current_gun"]
        self.sword = save_data["current_sword"]


        # ==========================================
        # USTAWIENIA PRZYCISKÓW
        # ==========================================

        BUTTON_SIZE = 140
        MARGIN = 50


        # ==========================================
        # SETTINGS
        # ==========================================

        self.settings_button = SquareButton(
            settings.WIDTH - BUTTON_SIZE - MARGIN,
            MARGIN,
            BUTTON_SIZE,
            "⚙",
            pygame.K_c
        )


        # ==========================================
        # INVENTORY
        # ==========================================

        self.inventory_button = SquareButton(
            settings.WIDTH - BUTTON_SIZE * 2 - MARGIN * 2,
            MARGIN,
            BUTTON_SIZE,
            "🎒",
            pygame.K_e
        )


        # ==========================================
        # MAP
        # ==========================================

        self.map_button = SquareButton(
            settings.WIDTH - BUTTON_SIZE - MARGIN,
            BUTTON_SIZE + MARGIN * 2,
            BUTTON_SIZE,
            "🗺",
            pygame.K_m
        )


        # ==========================================
        # ▲ / ▼
        # ==========================================

        # Stan GUI. None oznacza, że stan gry nie został jeszcze ustawiony.
        self.game_active = None
        self.buttons_visible = False

        # Przycisk TAB jest widoczny również podczas cutscenki.
        self.buttons_toggle = SquareButton(
            settings.WIDTH - BUTTON_SIZE - MARGIN,
            MARGIN,
            BUTTON_SIZE,
            "🔒",
            pygame.K_TAB
        )

        self.open_panel = None

    def reset_game_ui_self(self):
        data = save.load_game()
        last_save = data["variables"]["last_save"]
        if last_save not in data["saves"]:
            last_save = "save1"
        save_data = data["saves"][last_save]

        self.money = save_data["money"]
        self.fragments = save_data["fragments"]

        self.exp = save_data["exp"]
        self.max_exp = save_data["max_exp"]
        self.lvl = save_data["lvl"]
        self.prestige_lvl = save_data["prestige_lvl"]
        self.to_add_points = 0

        self.level_up_active = False
        self.level_up_start = 0
        self.level_up_level = 0
        self.level_up_particles = []

        self.health = save_data["health"]
        self.max_health = save_data["max_health"]

        self.energy = save_data["energy"]
        self.max_energy = save_data["max_energy"]

        self.stats_points_to_give = save_data["stats_points_to_give"]
        self.health_and_def_stats = save_data["health_and_def_stats"]
        self.dmg_and_forget_resistance_stats = save_data["dmg_and_forget_resistance_stats"]
        self.energy_stats = save_data["energy_stats"]
        self.combo_stats = save_data["combo_stats"]

        self.elemental = save_data["elemental"]
        self.name = save_data["character_name"]
        self.difficulty = save_data["difficulty"]

        self.current_place = save_data["current_world"]
        self.places_unlocked = save_data["worlds_unlocked"]

        self.place_position_x = save_data["current_map_on_x"]
        self.place_position_y = save_data["current_map_on_y"]

        self.map_position_x = save_data["current_location_x"]
        self.map_position_y = save_data["current_location_y"]

        self.fruit = save_data["current_fruit"]
        self.fighting_style = save_data["current_fighting_style"]
        self.gun = save_data["current_gun"]
        self.sword = save_data["current_sword"]

        # ==========================================
        # USTAWIENIA PRZYCISKÓW
        # ==========================================

        BUTTON_SIZE = 140
        MARGIN = 50

        # ==========================================
        # SETTINGS
        # ==========================================

        self.settings_button = SquareButton(
            settings.WIDTH - BUTTON_SIZE - MARGIN,
            MARGIN,
            BUTTON_SIZE,
            "⚙",
            pygame.K_c
        )

        # ==========================================
        # INVENTORY
        # ==========================================

        self.inventory_button = SquareButton(
            settings.WIDTH - BUTTON_SIZE * 2 - MARGIN * 2,
            MARGIN,
            BUTTON_SIZE,
            "🎒",
            pygame.K_e
        )

        # ==========================================
        # MAP
        # ==========================================

        self.map_button = SquareButton(
            settings.WIDTH - BUTTON_SIZE - MARGIN,
            BUTTON_SIZE + MARGIN * 2,
            BUTTON_SIZE,
            "🗺",
            pygame.K_m
        )

        # ==========================================
        # ▲ / ▼
        # ==========================================

        # Stan GUI. None oznacza, że stan gry nie został jeszcze ustawiony.
        self.game_active = None
        self.buttons_visible = False

        # Przycisk TAB jest widoczny również podczas cutscenki.
        self.buttons_toggle = SquareButton(
            settings.WIDTH - BUTTON_SIZE - MARGIN,
            MARGIN,
            BUTTON_SIZE,
            "🔒",
            pygame.K_TAB
        )

        self.open_panel = None

    def set_game_active(self, active):
        """Włącza lub blokuje sterowanie GUI zależnie od stanu gry."""

        # Nie resetujemy widoczności przycisków co klatkę.
        if self.game_active == active:
            return

        self.game_active = active

        if not active:
            # Podczas cutscenki chowamy E, C i M.
            self.buttons_visible = False
            self.open_panel = None

            # TAB z kłódką w prawym górnym rogu.
            self.buttons_toggle.icon = "🔒"
            self.buttons_toggle.x = (
                settings.WIDTH - self.buttons_toggle.size - 50
            )
            self.buttons_toggle.y = 50

        else:
            # Po rozpoczęciu gry pokazujemy przyciski.
            self.buttons_visible = True
            self.update_toggle_position()


    def draw_locked_toggle(self, screen, game_game_state):
        """Rysuje sam przycisk TAB z kłódką poza właściwą grą."""

        if not self.game_active:
            self.buttons_toggle.icon = "🔒"
            self.buttons_toggle.x = (
                settings.WIDTH - self.buttons_toggle.size - 50
            )
            self.buttons_toggle.y = 50
            if game_game_state != "cutsceene1":
                self.buttons_toggle.draw(screen)


    def update_toggle_position(self):

        BUTTON_SIZE = 140
        MARGIN = 50


        if self.buttons_visible:

            # ==========================================
            # PRZYCISKI WIDOCZNE
            # ▲ OBOK PLECAKA
            # ==========================================

            self.buttons_toggle.x = (
                settings.WIDTH
                - BUTTON_SIZE * 3
                - MARGIN * 3
            )

            self.buttons_toggle.y = MARGIN

            self.buttons_toggle.icon = "▲"


        else:

            # ==========================================
            # PRZYCISKI UKRYTE
            # ▼ W PRAWYM GÓRNYM ROGU
            # ==========================================

            self.buttons_toggle.x = (
                settings.WIDTH
                - BUTTON_SIZE
                - MARGIN
            )

            self.buttons_toggle.y = MARGIN

            self.buttons_toggle.icon = "▼"

    def give_exp_for_quest(self):
        self.exp += self.max_exp

    def update_lvl(self):
        data = save.load_game()

        last_save = data["variables"]["last_save"]

        if last_save not in data["saves"]:
            last_save = "save1"

        save_data = data["saves"][last_save]

        if self.exp >= self.max_exp:
            if self.lvl < 100:
                self.lvl += 1
                self.to_add_points += 2
                if self.lvl <= 5:
                    data["saves"][last_save]["money"] += 500
                elif self.lvl <= 10:
                    data["saves"][last_save]["money"] += 1000
                elif self.lvl <= 25:
                    data["saves"][last_save]["money"] += 2500
                elif self.lvl <= 50:
                    data["saves"][last_save]["money"] += 5000
                elif self.lvl <= 75:
                    data["saves"][last_save]["money"] += 7500
                elif self.lvl <= 80:
                    data["saves"][last_save]["money"] += 8000
                elif self.lvl <= 99:
                    data["saves"][last_save]["money"] += 10000
                elif self.lvl >= 100:
                    data["saves"][last_save]["money"] += 20000
                save.save_game(data)

                self.exp -= self.max_exp
                if self.lvl < 10:
                    self.max_exp += 25
                else:
                    self.max_exp += 50

                if self.exp >= self.max_exp:
                    self.update_lvl()

                else:
                    data["saves"][last_save]["lvl"] = self.lvl
                    data["saves"][last_save]["exp"] = self.exp
                    data["saves"][last_save]["max_exp"] = self.max_exp
                    data["saves"][last_save]["stats_points_to_give"] += self.to_add_points
                    self.to_add_points = 0
                    save.save_game(data)

                self.start_level_up_effect()

            else:
                self.prestige_lvl += 1

                self.exp -= self.max_exp
                if self.lvl < 10:
                    self.max_exp += 25
                else:
                    self.max_exp += 50

                if self.exp >= self.max_exp:
                    self.update_lvl()

                else:
                    data["saves"][last_save]["prestige_lvl"] = self.prestige_lvl
                    data["saves"][last_save]["exp"] = self.exp
                    data["saves"][last_save]["max_exp"] = self.max_exp
                    self.to_add_points = 0
                    save.save_game(data)

                self.start_level_up_effect()

    def recover_afk_hande(self):
        data = save.load_game()

        last_save = data["variables"]["last_save"]

        if last_save not in data["saves"]:
            last_save = "save1"

        if not hasattr(self, "afk_start_time"):
            self.afk_start_time = pygame.time.get_ticks()

        current_time = pygame.time.get_ticks()

        if current_time - self.afk_start_time >= 5000: #5000 - 5 sec

            # ==========================================
            # CO MA SIĘ STAĆ PO 5 SEKUNDACH
            # ==========================================

            self.energy += 1
            self.health += 1

            if self.energy > self.max_energy:
                self.energy = self.max_energy
            if self.health > self.max_health:
                self.health = self.max_health

            data["saves"][last_save]["health"] = self.health
            data["saves"][last_save]["energy"] = self.energy
            save.save_game(data)

            # ==========================================
            # RESET CZASU
            # ==========================================

            self.afk_start_time = current_time

    def start_level_up_effect(self):
        self.level_up_active = True
        self.level_up_start = pygame.time.get_ticks()
        data = save.load_game()

        last_save = data["variables"]["last_save"]

        if last_save not in data["saves"]:
            last_save = "save1"

        save_data = data["saves"][last_save]
        self.lvl = save_data["lvl"]
        self.level_up_level = self.lvl

        self.level_up_particles = []

        center_x = settings.WIDTH // 2
        center_y = settings.HEIGHT // 2

        # Tworzenie cząsteczek
        import random
        import math

        for i in range(35):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(2.5, 6.5)

            self.level_up_particles.append({
                "x": center_x,
                "y": center_y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "life": random.randint(500, 1000),
                "max_life": 1000,
                "size": random.randint(4, 9)
            })

    def draw_level_up_effect(self, screen):

        if not self.level_up_active:
            return

        now = pygame.time.get_ticks()
        elapsed = now - self.level_up_start

        duration = 2500

        if elapsed >= duration:
            self.level_up_active = False
            self.level_up_particles.clear()
            return

        progress = elapsed / duration

        # ==========================================
        # CZĄSTECZKI
        # ==========================================

        for particle in self.level_up_particles:

            particle["x"] += particle["vx"]
            particle["y"] += particle["vy"]

            particle["vy"] += 0.025

            particle["life"] -= 16

            life_progress = max(
                0,
                particle["life"] / particle["max_life"]
            )

            alpha = int(255 * life_progress)

            if alpha <= 0:
                continue

            size = max(
                1,
                int(particle["size"] * life_progress)
            )

            particle_surface = pygame.Surface(
                (size * 2, size * 2),
                pygame.SRCALPHA
            )

            pygame.draw.circle(
                particle_surface,
                (255, 220, 70, alpha),
                (size, size),
                size
            )

            screen.blit(
                particle_surface,
                (
                    int(particle["x"] - size),
                    int(particle["y"] - size)
                )
            )

        # ==========================================
        # NAPIS
        # ==========================================

        # Najpierw lekko powiększa się,
        # potem przesuwa do góry.
        if progress < 0.18:

            appear_progress = progress / 0.18

            scale = 0.7 + appear_progress * 0.3

        else:

            scale = 1.0

        # Ruch do góry
        move_progress = min(
            1.0,
            max(0.0, (progress - 0.05) / 0.95)
        )

        move_progress = 1 - (1 - move_progress) ** 3

        start_y = settings.HEIGHT // 2
        end_y = start_y - (300)

        y = start_y + (end_y - start_y) * move_progress

        # Zanikanie pod koniec
        if progress > 0.75:

            fade_progress = (
                                    progress - 0.75
                            ) / 0.25

            alpha = int(
                255 * (1 - fade_progress)
            )

        else:

            alpha = 255

        if self.level_up_level >= 100:
            level_up_text = f"< Max Lvl reached! (Lvl: {self.level_up_level}) >"
        else:
            level_up_text = f"< You leveled up! (Lvl: {self.level_up_level}) >"

        text = font.render(
            level_up_text,
            True,
            (255, 225, 80)
        )

        # Powiększenie przy pojawieniu
        new_width = max(
            1,
            int(text.get_width() * scale)
        )

        new_height = max(
            1,
            int(text.get_height() * scale)
        )

        text = pygame.transform.smoothscale(
            text,
            (new_width, new_height)
        )

        # Cień
        shadow = pygame.Surface(
            text.get_size(),
            pygame.SRCALPHA
        )

        shadow.blit(text, (0, 0))
        shadow.fill(
            (20, 20, 20, alpha),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        shadow_rect = shadow.get_rect(
            center=(
                settings.WIDTH // 2 + (6),
                int(y + (6))
            )
        )

        screen.blit(
            shadow,
            shadow_rect
        )

        # Główny napis
        text_surface = pygame.Surface(
            text.get_size(),
            pygame.SRCALPHA
        )

        text_surface.blit(text, (0, 0))
        text_surface.fill(
            (255, 255, 255, alpha),
            special_flags=pygame.BLEND_RGBA_MULT
        )

        text_rect = text_surface.get_rect(
            center=(
                settings.WIDTH // 2,
                int(y)
            )
        )

        screen.blit(
            text_surface,
            text_rect
        )

    def handle_event(self, event):

        # Poza właściwą grą ignorujemy sterowanie GUI.
        if not self.game_active:
            return

        # ==========================================
        # KLAWIATURA
        # ==========================================

        if event.type == pygame.KEYDOWN:

            if event.key == self.buttons_toggle.key:

                self.buttons_visible = not self.buttons_visible

                self.update_toggle_position()

                return


            # ==========================================
            # SETTINGS
            # ==========================================

            if event.key == self.settings_button.key:

                self.open_panel = (
                    None
                    if self.open_panel == "settings"
                    else "settings"
                )


            # ==========================================
            # INVENTORY
            # ==========================================

            elif event.key == self.inventory_button.key:

                self.open_panel = (
                    None
                    if self.open_panel == "inventory"
                    else "inventory"
                )


            # ==========================================
            # MAP
            # ==========================================

            elif event.key == self.map_button.key:

                self.open_panel = (
                    None
                    if self.open_panel == "map"
                    else "map"
                )


        # ==========================================
        # MYSZ
        # ==========================================

        # Kółko myszy przewija dokładnie tę sekcję ekwipunku,
        # nad którą znajduje się kursor.
        if event.type == pygame.MOUSEWHEEL and self.open_panel == "inventory":
            mouse_pos = pygame.mouse.get_pos()
            section_viewports = getattr(self, "inventory_section_viewports", {})
            section_max_scroll = getattr(self, "inventory_section_max_scroll", {})

            for section_index, viewport in section_viewports.items():
                if viewport.collidepoint(mouse_pos):
                    if not hasattr(self, "inventory_scroll_offsets"):
                        self.inventory_scroll_offsets = {}
                    max_scroll = section_max_scroll.get(section_index, 0)
                    current_scroll = self.inventory_scroll_offsets.get(section_index, 0)
                    self.inventory_scroll_offsets[section_index] = max(
                        0,
                        min(max_scroll, current_scroll - event.y * 150)
                    )
                    return

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                # ==========================================
                # ▲ / ▼
                # ==========================================

                if self.buttons_toggle.clicked():

                    self.buttons_visible = not self.buttons_visible

                    self.update_toggle_position()

                    return


                # ==========================================
                # SETTINGS
                # ==========================================

                if (
                    self.buttons_visible
                    and self.settings_button.clicked()
                ):

                    self.open_panel = (
                        None
                        if self.open_panel == "settings"
                        else "settings"
                    )


                # ==========================================
                # INVENTORY
                # ==========================================

                elif (
                    self.buttons_visible
                    and self.inventory_button.clicked()
                ):

                    self.open_panel = (
                        None
                        if self.open_panel == "inventory"
                        else "inventory"
                    )


                # ==========================================
                # MAP
                # ==========================================

                elif (
                    self.buttons_visible
                    and self.map_button.clicked()
                ):

                    self.open_panel = (
                        None
                        if self.open_panel == "map"
                        else "map"
                    )

                mouse_x, mouse_y = event.pos

                if self.open_panel == "inventory":
                    for section_index, viewport in self.inventory_section_viewports.items():
                        if viewport.collidepoint(mouse_x, mouse_y):
                            # Kliknięto obszar tej sekcji ekwipunku
                            print(f"Kliknięto sekcję: {section_index}")

                            # Tutaj sprawdzimy, który konkretnie przedmiot
                            # został kliknięty.
                            break

    def draw(self, screen, game_game_state):

        data = save.load_game()

        last_save = data["variables"]["last_save"]

        if last_save not in data["saves"]:
            last_save = "save1"

        save_data = data["saves"][last_save]

        quest_doing_rn_number = save_data["quest_doing_rn"]
        data["saves"][last_save]["quest_doing_rn_name"] = data["variables"]["quests_names"][quest_doing_rn_number]
        save.save_game(data)

        if self.game_active:
        # ==========================================
        # QUEST + FRAGMENTY + PIENIĄDZE
        # ==========================================

            panel_x = (40)
            panel_y = (40)

            panel_width = (460)
            panel_height = (250)

            radius = (18)

            # ------------------------------------------
            # DANE
            # ------------------------------------------

            quest = save_data["quest_doing_rn_name"]

            fragments = save_data["fragments"]
            money = save_data["money"]

            # ------------------------------------------
            # CIEŃ
            # ------------------------------------------

            shadow_rect = pygame.Rect(
                panel_x + (7),
                panel_y + (7),
                panel_width,
                panel_height
            )

            pygame.draw.rect(
                screen,
                (25, 25, 25),
                shadow_rect,
                border_radius=radius
            )

            # ------------------------------------------
            # GŁÓWNY PANEL
            # ------------------------------------------

            panel_rect = pygame.Rect(
                panel_x,
                panel_y,
                panel_width,
                panel_height
            )

            pygame.draw.rect(
                screen,
                (15, 25, 40),
                panel_rect,
                border_radius=radius
            )

            # ------------------------------------------
            # GÓRNA CZĘŚĆ - QUEST
            # ------------------------------------------

            quest_height = (155)

            quest_rect = pygame.Rect(
                panel_x,
                panel_y,
                panel_width,
                quest_height
            )

            pygame.draw.rect(
                screen,
                (30, 55, 85),
                quest_rect,
                border_top_left_radius=radius,
                border_top_right_radius=radius
            )

            # ------------------------------------------
            # NAPIS QUEST
            # ------------------------------------------

            quest_title = font2.render(
                "Quest:",
                True,
                (255, 220, 80)
            )

            quest_title_rect = quest_title.get_rect(
                midleft=(
                    panel_x + (25),
                    panel_y + (35)
                )
            )

            screen.blit(
                quest_title,
                quest_title_rect
            )

            # ------------------------------------------
            # NAZWA QUESTU
            # ------------------------------------------

            quest_max_width = panel_width - (50)

            # ------------------------------------------
            # ZAWIJANIE TEKSTU
            # ------------------------------------------

            words = quest.split(" ")
            quest_lines = []
            current_line = ""

            for word in words:

                test_line = (
                    word
                    if current_line == ""
                    else current_line + " " + word
                )

                test_surface = font3.render(
                    test_line,
                    True,
                    (255, 255, 255)
                )

                if test_surface.get_width() <= quest_max_width:

                    current_line = test_line

                else:

                    if current_line != "":
                        quest_lines.append(current_line)

                    current_line = word

            if current_line != "":
                quest_lines.append(current_line)

            # ------------------------------------------
            # MAKSYMALNIE 2 LINIE
            # ------------------------------------------

            if len(quest_lines) > 2:

                quest_lines = quest_lines[:2]

                last_line = quest_lines[1]

                while True:

                    test_line = last_line + "..."

                    test_surface = font3.render(
                        test_line,
                        True,
                        (255, 255, 255)
                    )

                    if test_surface.get_width() <= quest_max_width:
                        break

                    if len(last_line) <= 1:
                        break

                    last_line = last_line[:-1]

                quest_lines[1] = last_line + "..."

            # ------------------------------------------
            # RYSOWANIE QUESTU
            # ------------------------------------------

            if len(quest_lines) == 1:

                quest_text = font3.render(
                    quest_lines[0],
                    True,
                    (255, 255, 255)
                )

                quest_text_rect = quest_text.get_rect(
                    midleft=(
                        panel_x + (25),
                        panel_y + (85)
                    )
                )

                screen.blit(
                    quest_text,
                    quest_text_rect
                )

            else:

                line_spacing = (5)

                total_height = (
                        sum(
                            font3.render(
                                line,
                                True,
                                (255, 255, 255)
                            ).get_height()
                            for line in quest_lines
                        )
                        +
                        line_spacing
                )

                start_y = (
                        panel_y
                        + (85)
                        - total_height // 2
                )

                for line in quest_lines:
                    quest_text = font3.render(
                        line,
                        True,
                        (255, 255, 255)
                    )

                    quest_text_rect = quest_text.get_rect(
                        midleft=(
                            panel_x + (25),
                            start_y + quest_text.get_height() // 2
                        )
                    )

                    screen.blit(
                        quest_text,
                        quest_text_rect
                    )

                    start_y += (
                            quest_text.get_height()
                            + line_spacing
                    )

            # ------------------------------------------
            # DOLNA CZĘŚĆ
            # ------------------------------------------

            bottom_y = panel_y + quest_height
            bottom_height = panel_height - quest_height

            bottom_rect = pygame.Rect(
                panel_x,
                bottom_y,
                panel_width,
                bottom_height
            )

            pygame.draw.rect(
                screen,
                (20, 35, 55),
                bottom_rect,
                border_bottom_left_radius=radius,
                border_bottom_right_radius=radius
            )

            # ------------------------------------------
            # FRAGMENTY
            # ------------------------------------------

            fragments_text = font_4.render(
                f"𝓕 {format_number(fragments)}",
                True,
                (190, 100, 255)
            )

            fragments_rect = fragments_text.get_rect(
                midleft=(
                    panel_x + (25),
                    bottom_y + bottom_height // 2
                )
            )

            screen.blit(
                fragments_text,
                fragments_rect
            )

            # ------------------------------------------
            # PIENIĄDZE
            # ------------------------------------------

            money_text = font_4.render(
                f"$ {format_number(money)}",
                True,
                (100, 255, 130)
            )

            money_rect = money_text.get_rect(
                midright=(
                    panel_x + panel_width - (25),
                    bottom_y + bottom_height // 2
                )
            )

            screen.blit(
                money_text,
                money_rect
            )

            # ==========================================
            # CURRENT PLACE
            # ==========================================

            self.current_place = save_data["current_world"]

            text = font.render(
                f"< {self.current_place} >",
                True,
                (255, 255, 255)
            )


            text_rect = text.get_rect(
                center=(
                    settings.WIDTH // 2,
                    (75)
                )
            )


            shadow_text_rect = text.get_rect(
                center=(
                    settings.WIDTH // 2 + (5),
                    (75) + (5)
                )
            )


            screen.blit(
                font.render(
                    f"< {self.current_place} >",
                    True,
                    (35, 35, 35)
                ),
                shadow_text_rect
            )


            screen.blit(
                text,
                text_rect
            )

        # ==========================================
        # CUSTOM FRAME
        # ==========================================

        elemental_v = save_data["elemental_lvl"]
        if_elemental_v = False
        if elemental_v == 3:
            if_elemental_v = True
        else:
            if_elemental_v = False

        current_gun = save_data["current_gun"]
        if_gun_eq = False
        if current_gun == "":
            if_gun_eq = False
        else:
            if_gun_eq = True

        is_blocked = True
        if game_game_state == "game":
            is_blocked = True
        else:
            is_blocked = False

        draw_custom_frame(
            screen,
            ((settings.WIDTH // 2) - 600),
            (1100),
            (1200),
            (250),
            is_blocked,
            energy=self.energy,
            max_energy=self.max_energy,
            health=self.health,
            max_health=self.max_health,
            v3_enabled=if_elemental_v,
            bow_enabled=if_gun_eq
        )

        # ==========================================
        # GÓRNE PRZYCISKI
        # ==========================================

        if self.buttons_visible:

            self.settings_button.draw(screen)

            self.inventory_button.draw(screen)

            self.map_button.draw(screen)


        # ==========================================
        # ▲ / ▼
        # ZAWSZE WIDOCZNY
        # ==========================================

        self.buttons_toggle.draw(screen)


        # ==========================================
        # PANELE
        # ==========================================

        if self.open_panel == "settings":

            self.draw_settings(screen)

        elif self.open_panel == "inventory":

            self.draw_inventory(screen)

        elif self.open_panel == "map":

            self.draw_map(screen)

        # ==========================================
        # LEVEL UP EFFECT
        # ==========================================

        self.draw_level_up_effect(screen)
        self.update_lvl()

        self.recover_afk_hande()

    def draw_settings(self, screen):

        data = save.load_game()

        last_save = data["variables"]["last_save"]

        if last_save not in data["saves"]:
            last_save = "save1"

        save_data = data["saves"][last_save]

        # ==========================================
        # PANEL
        # ==========================================

        shadow = pygame.Surface(
            (
                (600),
                settings.HEIGHT
            ),
            pygame.SRCALPHA
        )


        shadow.fill(
            (40, 40, 40, 180)
        )


        screen.blit(
            shadow,
            (0, 0)
        )


        # ==========================================
        # TYTUŁ
        # ==========================================

        text = font.render(
            "Aroarente RPG :",
            True,
            (255, 255, 255)
        )


        text_rect = text.get_rect(
            center=(
                (300),
                (100)
            )
        )


        screen.blit(
            text,
            text_rect
        )


        # ==========================================
        # PODTYTUŁ
        # ==========================================

        text2 = font.render(
            "Explore the world",
            True,
            (255, 255, 255)
        )


        text2_rect = text2.get_rect(
            center=(
                (300),
                (200)
            )
        )


        screen.blit(
            text2,
            text2_rect
        )


        # ==========================================
        # SETTINGS
        # ==========================================

        draw_multiline_text_with_frame(
            screen,
            [
                "No settings",
                "for now.",
                "Wait for",
                "update (:"
            ],
            font,
            (
                (300),
                (675)
            )
        )

    def draw_inventory(self, screen):
        data = save.load_game()

        last_save = data["variables"]["last_save"]

        if last_save not in data["saves"]:
            last_save = "save1"

        save_data = data["saves"][last_save]

        if save_data["quest_doing_rn"] == 1:
            data["saves"][last_save]["quest_doing_rn"] += 1
            data["saves"][last_save]["quests_done"] += 1
            self.give_exp_for_quest()
            save.save_game(data)

        # =====================================================
        # INWENTARZ — BRĄZOWA SKÓRA PLECAKA FANTASY RPG
        # =====================================================

        import pygame
        import random
        import math

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        # =====================================================
        # 1. GŁÓWNE TŁO — BRĄZOWA SKÓRA
        # =====================================================

        screen.fill((91, 53, 30))

        # Delikatny gradient skóry
        leather_surface = pygame.Surface(
            (screen_width, screen_height)
        )

        for i in range(screen_height):
            progress = i / max(1, screen_height)

            red = int(125 - progress * 35)
            green = int(76 - progress * 28)
            blue = int(43 - progress * 15)

            pygame.draw.line(
                leather_surface,
                (red, green, blue),
                (0, i),
                (screen_width, i)
            )

        screen.blit(leather_surface, (0, 0))

        # =====================================================
        # 2. DELIKATNA FAKTURA SKÓRY
        # =====================================================

        texture_surface = pygame.Surface(
            (screen_width, screen_height),
            pygame.SRCALPHA
        )

        random.seed(42)

        for _ in range(max(100, screen_width * screen_height // 1800)):
            px = random.randint(0, screen_width - 1)
            py = random.randint(0, screen_height - 1)

            length = random.randint(2, 9)

            if random.random() < 0.5:
                color = (35, 18, 10, 35)
            else:
                color = (230, 165, 100, 22)

            pygame.draw.line(
                texture_surface,
                color,
                (px, py),
                (min(screen_width - 1, px + length), py + 1),
                1
            )

        screen.blit(texture_surface, (0, 0))

        # =====================================================
        # 3. CIEMNE KRAWĘDZIE PLECAKA
        # =====================================================

        edge_size = max(12, int(min(screen_width, screen_height) * 0.025))

        # Górna krawędź
        pygame.draw.rect(
            screen,
            (48, 27, 17),
            (0, 0, screen_width, edge_size)
        )

        # Dolna krawędź
        pygame.draw.rect(
            screen,
            (48, 27, 17),
            (
                0,
                screen_height - edge_size,
                screen_width,
                edge_size
            )
        )

        # Lewa krawędź
        pygame.draw.rect(
            screen,
            (48, 27, 17),
            (0, 0, edge_size, screen_height)
        )

        # Prawa krawędź
        pygame.draw.rect(
            screen,
            (48, 27, 17),
            (
                screen_width - edge_size,
                0,
                edge_size,
                screen_height
            )
        )

        # =====================================================
        # 4. PODWÓJNE OBRAMOWANIE
        # =====================================================

        margin = edge_size // 2

        pygame.draw.rect(
            screen,
            (183, 125, 68),
            (
                margin,
                margin,
                screen_width - margin * 2,
                screen_height - margin * 2
            ),
            width=4,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            (65, 36, 22),
            (
                margin + 7,
                margin + 7,
                screen_width - (margin + 7) * 2,
                screen_height - (margin + 7) * 2
            ),
            width=2,
            border_radius=9
        )

        # =====================================================
        # 5. PRZESZYCIA WZDŁUŻ KRAWĘDZI
        # =====================================================

        stitch_color = (220, 166, 104)
        stitch_shadow = (45, 24, 14)

        stitch_offset = edge_size + 10
        stitch_spacing = 22

        # Góra i dół
        for px in range(stitch_offset, screen_width - stitch_offset, stitch_spacing):
            for py in (stitch_offset, screen_height - stitch_offset):
                pygame.draw.line(
                    screen,
                    stitch_shadow,
                    (px, py + 1),
                    (px + 9, py + 1),
                    3
                )

                pygame.draw.line(
                    screen,
                    stitch_color,
                    (px, py),
                    (px + 9, py),
                    2
                )

        # Lewa i prawa strona
        for py in range(stitch_offset, screen_height - stitch_offset, stitch_spacing):
            for px in (stitch_offset, screen_width - stitch_offset):
                pygame.draw.line(
                    screen,
                    stitch_shadow,
                    (px + 1, py),
                    (px + 1, py + 9),
                    3
                )

                pygame.draw.line(
                    screen,
                    stitch_color,
                    (px, py),
                    (px, py + 9),
                    2
                )

        # =====================================================
        # 6. METALOWE NAROŻNIKI
        # =====================================================

        corner_size = max(28, int(min(screen_width, screen_height) * 0.055))

        corners = [
            (edge_size, edge_size),
            (screen_width - edge_size, edge_size),
            (edge_size, screen_height - edge_size),
            (screen_width - edge_size, screen_height - edge_size)
        ]

        for cx, cy in corners:
            pygame.draw.circle(
                screen,
                (39, 25, 17),
                (cx, cy),
                corner_size // 2 + 3
            )

            pygame.draw.circle(
                screen,
                (117, 76, 39),
                (cx, cy),
                corner_size // 2
            )

            pygame.draw.circle(
                screen,
                (207, 157, 87),
                (cx, cy),
                corner_size // 2,
                3
            )

            pygame.draw.circle(
                screen,
                (238, 199, 128),
                (cx, cy),
                4
            )

        # =====================================================
        # 7. DELIKATNE CIENIOWANIE BRZEGÓW
        # =====================================================

        vignette = pygame.Surface(
            (screen_width, screen_height),
            pygame.SRCALPHA
        )

        vignette_width = max(
            20,
            int(min(screen_width, screen_height) * 0.12)
        )

        for i in range(vignette_width):
            alpha = int(1 + 65 * (1 - i / vignette_width))

            pygame.draw.rect(
                vignette,
                (25, 10, 4, alpha),
                (
                    i,
                    i,
                    screen_width - i * 2,
                    screen_height - i * 2
                ),
                width=2
            )

        # =====================================================
        # 8. PIONOWE PODZIAŁY EKWIPUNKU — STYL SKÓRZANY
        # =====================================================

        section_width = screen_width / 3

        line_top = edge_size + 8
        line_bottom = screen_height - edge_size - 8

        for i in (1, 2):
            line_x = int(section_width * i)

            # Ciemny cień linii
            pygame.draw.line(
                screen,
                (40, 22, 13),
                (line_x + 2, line_top),
                (line_x + 2, line_bottom),
                6
            )

            # Główna linia — ciemny brąz
            pygame.draw.line(
                screen,
                (75, 43, 25),
                (line_x, line_top),
                (line_x, line_bottom),
                4
            )

            # Delikatny złotobrązowy brzeg
            pygame.draw.line(
                screen,
                (183, 125, 68),
                (line_x - 2, line_top),
                (line_x - 2, line_bottom),
                1
            )

            # Przeszycia wzdłuż podziału
            for py in range(line_top + 12, line_bottom - 8, 22):
                pygame.draw.line(
                    screen,
                    (220, 166, 104),
                    (line_x - 5, py),
                    (line_x + 5, py + 6),
                    2
                )

        # =====================================================
        # 9. POZIOME PODZIAŁY LEWEJ I PRAWEJ KOLUMNY
        # =====================================================

        section_height = screen_height / 3

        left_start = 0
        left_end = int(screen_width / 3)

        right_start = int(screen_width * 2 / 3)
        right_end = screen_width

        for i in (1, 2):
            line_y = int(section_height * i)

            # Lewa kolumna
            for start_x, end_x in (
                (left_start + edge_size + 8, left_end - 8),
                (right_start + 8, right_end - edge_size - 8)
            ):
                # Ciemny cień
                pygame.draw.line(
                    screen,
                    (40, 22, 13),
                    (start_x, line_y + 2),
                    (end_x, line_y + 2),
                    6
                )

                # Główna linia — ciemny brąz
                pygame.draw.line(
                    screen,
                    (75, 43, 25),
                    (start_x, line_y),
                    (end_x, line_y),
                    4
                )

                # Złotobrązowy brzeg
                pygame.draw.line(
                    screen,
                    (183, 125, 68),
                    (start_x, line_y - 2),
                    (end_x, line_y - 2),
                    1
                )

                # Przeszycia
                for px in range(start_x + 12, end_x - 8, 22):
                    pygame.draw.line(
                        screen,
                        (220, 166, 104),
                        (px, line_y - 5),
                        (px + 6, line_y + 5),
                        2
                    )

        # =====================================================
        # 10. PODZIAŁ ŚRODKOWEJ KOLUMNY: 20% / 60% / 20%
        # =====================================================

        center_start = int(screen_width / 3)
        center_end = int(screen_width * 2 / 3)

        center_top = edge_size + 8
        center_bottom = screen_height - edge_size - 8
        center_height = center_bottom - center_top

        center_line_1 = int(center_top + center_height * 0.20)
        center_line_2 = int(center_top + center_height * 0.80)

        for line_y in (center_line_1, center_line_2):

            pygame.draw.line(
                screen,
                (40, 22, 13),
                (center_start + 8, line_y + 2),
                (center_end - 8, line_y + 2),
                6
            )

            pygame.draw.line(
                screen,
                (75, 43, 25),
                (center_start + 8, line_y),
                (center_end - 8, line_y),
                4
            )

            pygame.draw.line(
                screen,
                (183, 125, 68),
                (center_start + 8, line_y - 2),
                (center_end - 8, line_y - 2),
                1
            )

            for px in range(center_start + 20, center_end - 15, 22):
                pygame.draw.line(
                    screen,
                    (220, 166, 104),
                    (px, line_y - 5),
                    (px + 6, line_y + 5),
                    2
                )

        # =====================================================
        # 11. TYTUŁY SEKCJI — FANTASY RPG
        # =====================================================

        title_font = pygame.font.Font(None, 44)

        title_color = (255, 220, 155)
        shadow_color = (35, 18, 10)
        gold_color = (195, 139, 67)
        light_gold = (255, 235, 185)

        section_height = screen_height / 3
        column_width = screen_width / 3

        title_padding_y = 22

        # =====================================================
        # FUNKCJA RYSOWANIA OZDOBNEGO TYTUŁU
        # =====================================================

        def draw_inventory_title(title, center_x, top_y, max_width):
            text = title_font.render(
                title,
                True,
                title_color
            )

            # Dopasowanie napisu do szerokości sekcji
            if text.get_width() > max_width:
                scale = max_width / text.get_width()

                text = pygame.transform.smoothscale(
                    text,
                    (
                        int(text.get_width() * scale),
                        int(text.get_height() * scale)
                    )
                )

            text_rect = text.get_rect(
                midtop=(int(center_x), int(top_y))
            )

            # Cień napisu
            shadow = text.copy()
            shadow.fill(
                shadow_color,
                special_flags=pygame.BLEND_RGB_MULT
            )

            screen.blit(
                shadow,
                (text_rect.x + 3, text_rect.y + 4)
            )

            # Główny napis
            screen.blit(text, text_rect)

            # Delikatne złote podkreślenie
            line_y = text_rect.bottom + 8
            line_width = min(
                text_rect.width + 50,
                int(max_width * 0.72)
            )

            line_left = int(center_x - line_width / 2)
            line_right = int(center_x + line_width / 2)

            pygame.draw.line(
                screen,
                gold_color,
                (line_left, line_y),
                (line_right, line_y),
                2
            )

            # Jasny środek podkreślenia
            pygame.draw.line(
                screen,
                light_gold,
                (int(center_x - 18), line_y),
                (int(center_x + 18), line_y),
                2
            )

            # Ozdobne końcówki
            for ornament_x in (line_left, line_right):
                pygame.draw.circle(
                    screen,
                    light_gold,
                    (ornament_x, line_y),
                    3
                )

        # =====================================================
        # LEWA KOLUMNA — ARMOR / UTILITY / FRUITS
        # =====================================================

        left_titles = [
            "Armor:",
            "Utility:",
            "Fruits:"
        ]

        left_center_x = column_width / 2

        for i, title in enumerate(left_titles):
            section_top = int(section_height * i)

            # Przesuń Armor i Utility niżej
            extra_y = 50 if i == 0 else (15 if i == 1 else 0)

            draw_inventory_title(
                title,
                left_center_x,
                section_top + title_padding_y + extra_y,
                column_width - edge_size * 2 - 20
            )

        # =====================================================
        # PRAWA KOLUMNA — SWORDS / GUNS / PETS
        # =====================================================

        right_titles = [
            "Swords:",
            "Guns:",
            "Pets:"
        ]

        right_center_x = column_width * 2.5

        for i, title in enumerate(right_titles):
            section_top = int(section_height * i)

            # Przesuń tylko Swords niżej
            extra_y = 50 if i == 0 else 0

            draw_inventory_title(
                title,
                right_center_x,
                section_top + title_padding_y + extra_y,
                column_width - edge_size * 2 - 20
            )

        # =====================================================
        # TYTUŁY SEKCJI — FANTASY RPG
        # =====================================================

        title_font = pygame.font.Font(None, 44)

        title_color = (255, 220, 155)
        shadow_color = (35, 18, 10)
        gold_color = (195, 139, 67)
        light_gold = (255, 235, 185)

        section_height = screen_height / 3
        column_width = screen_width / 3

        title_padding_y = 22

        # =====================================================
        # FUNKCJA RYSOWANIA OZDOBNEGO TYTUŁU
        # =====================================================

        def draw_inventory_title(title, center_x, top_y, max_width):
            text = title_font.render(
                title,
                True,
                title_color
            )

            # Dopasowanie napisu do szerokości sekcji
            if text.get_width() > max_width:
                scale = max_width / text.get_width()

                text = pygame.transform.smoothscale(
                    text,
                    (
                        max(1, int(text.get_width() * scale)),
                        max(1, int(text.get_height() * scale))
                    )
                )

            text_rect = text.get_rect(
                midtop=(int(center_x), int(top_y))
            )

            # Cień napisu
            shadow = text.copy()
            shadow.fill(
                shadow_color,
                special_flags=pygame.BLEND_RGB_MULT
            )

            screen.blit(
                shadow,
                (text_rect.x + 3, text_rect.y + 4)
            )

            # Główny napis
            screen.blit(text, text_rect)

            # Złote podkreślenie
            line_y = text_rect.bottom + 8

            line_width = min(
                text_rect.width + 50,
                int(max_width * 0.72)
            )

            line_left = int(center_x - line_width / 2)
            line_right = int(center_x + line_width / 2)

            pygame.draw.line(
                screen,
                gold_color,
                (line_left, line_y),
                (line_right, line_y),
                2
            )

            # Jasny środek podkreślenia
            pygame.draw.line(
                screen,
                light_gold,
                (int(center_x - 18), line_y),
                (int(center_x + 18), line_y),
                2
            )

            # Ozdobne końcówki
            for ornament_x in (line_left, line_right):
                pygame.draw.circle(
                    screen,
                    light_gold,
                    (ornament_x, line_y),
                    3
                )

        # =====================================================
        # LEWA KOLUMNA — ARMOR / UTILITY / FRUITS
        # =====================================================

        left_titles = [
            "Armor:",
            "Utility:",
            "Fruits:"
        ]

        left_center_x = column_width / 2

        for i, title in enumerate(left_titles):
            section_top = int(section_height * i)

            # Armor niżej o 50 px, Utility niżej o 35 px
            extra_y = 50 if i == 0 else (15 if i == 1 else 0)

            draw_inventory_title(
                title,
                left_center_x,
                section_top + title_padding_y + extra_y,
                column_width - edge_size * 2 - 20
            )

        # =====================================================
        # PRAWA KOLUMNA — SWORDS / GUNS / PETS
        # =====================================================

        right_titles = [
            "Swords:",
            "Guns:",
            "Pets:"
        ]

        right_center_x = column_width * 2.5

        for i, title in enumerate(right_titles):
            section_top = int(section_height * i)

            # Tylko Swords niżej o 50 px
            extra_y = 50 if i == 0 else 0

            draw_inventory_title(
                title,
                right_center_x,
                section_top + title_padding_y + extra_y,
                column_width - edge_size * 2 - 20
            )

        # =====================================================
        # ŚRODKOWA KOLUMNA — QUEST
        # =====================================================

        center_column_x = screen_width / 2

        # Tytuł Quest przesunięty niżej
        quest_title_y = title_padding_y + 35

        draw_inventory_title(
            "Quest:",
            center_column_x,
            quest_title_y,
            column_width - edge_size * 2 - 20
        )

        # =====================================================
        # NAZWA AKTUALNEGO QUESTA
        # =====================================================

        quest_name = save_data.get(
            "quest_doing_rn_name",
            "No active quest"
        )

        quest_name = str(quest_name)

        quest_name_font = pygame.font.Font(None, 46)

        quest_name_color = (255, 225, 165)
        quest_shadow_color = (35, 18, 10)

        max_quest_width = int(
            column_width - edge_size * 2 - 40
        )

        # =====================================================
        # AUTOMATYCZNE ZAWIJANIE NAZWY QUESTA
        # =====================================================

        quest_lines = []
        current_line = ""

        for word in quest_name.split():
            test_line = f"{current_line} {word}".strip()

            if quest_name_font.size(test_line)[0] <= max_quest_width:
                current_line = test_line
            else:
                if current_line:
                    quest_lines.append(current_line)

                current_line = ""

                # Zawijanie bardzo długich słów
                for character in word:
                    test_word = current_line + character

                    if quest_name_font.size(test_word)[0] <= max_quest_width:
                        current_line = test_word
                    else:
                        if current_line:
                            quest_lines.append(current_line)

                        current_line = character

        if current_line:
            quest_lines.append(current_line)

        # =====================================================
        # RYSOWANIE NAZWY QUESTA — WYŚRODKOWANA
        # =====================================================

        quest_text_y = quest_title_y + 65
        quest_line_spacing = quest_name_font.get_linesize() + 5

        for line in quest_lines:
            quest_text = quest_name_font.render(
                line,
                True,
                quest_name_color
            )

            quest_rect = quest_text.get_rect(
                midtop=(
                    int(center_column_x),
                    int(quest_text_y)
                )
            )

            # Cień
            quest_shadow = quest_text.copy()
            quest_shadow.fill(
                quest_shadow_color,
                special_flags=pygame.BLEND_RGB_MULT
            )

            screen.blit(
                quest_shadow,
                (quest_rect.x + 3, quest_rect.y + 4)
            )

            # Nazwa questa
            screen.blit(
                quest_text,
                quest_rect
            )

            quest_text_y += quest_line_spacing

        # =====================================================
        # NAGRODY ZA QUEST — EXP + PIENIĄDZE
        # =====================================================

        # Wartości do zmiany
        quest_exp_reward = save_data["max_exp"]
        self.lvl = data["saves"][last_save]["lvl"]
        if self.lvl <= 5:
            quest_money_reward = 500
        elif self.lvl <= 10:
            quest_money_reward = 1000
        elif self.lvl <= 25:
            quest_money_reward = 2500
        elif self.lvl <= 50:
            quest_money_reward = 5000
        elif self.lvl <= 75:
            quest_money_reward = 7500
        elif self.lvl <= 80:
            quest_money_reward = 8000
        elif self.lvl <= 99:
            quest_money_reward = 10000
        elif self.lvl >= 100:
            quest_money_reward = 20000

        # Większa czcionka
        reward_font = pygame.font.Font(None, 48)

        # Kolory
        exp_color = (255, 220, 40)       # Żółty
        money_color = (60, 230, 90)      # Zielony
        reward_shadow_color = (35, 18, 10)

        # Pozycja pod nazwą questa
        reward_y = quest_text_y + 15

        # Szerokość środkowej kolumny
        center_left = int(screen_width / 3)
        center_right = int(screen_width * 2 / 3)

        reward_margin = 25

        # =====================================================
        # EXP — LEWA STRONA
        # =====================================================

        # =====================================================
        # EXP — ŚRODEK LEWEJ POŁOWY
        # =====================================================

        exp_text = reward_font.render(
            f"Exp: {quest_exp_reward}",
            True,
            exp_color
        )

        exp_rect = exp_text.get_rect(
            midtop=(
                int(screen_width / 3 + column_width / 4),
                int(reward_y)
            )
        )

        exp_shadow = exp_text.copy()
        exp_shadow.fill(
            reward_shadow_color,
            special_flags=pygame.BLEND_RGB_MULT
        )

        screen.blit(
            exp_shadow,
            (exp_rect.x + 3, exp_rect.y + 4)
        )
        screen.blit(exp_text, exp_rect)

        # =====================================================
        # PIENIĄDZE — ŚRODEK PRAWEJ POŁOWY
        # =====================================================

        money_text = reward_font.render(
            f"$: {quest_money_reward}",
            True,
            money_color
        )

        money_rect = money_text.get_rect(
            midtop=(
                int(screen_width / 3 + column_width * 3 / 4),
                int(reward_y)
            )
        )

        money_shadow = money_text.copy()
        money_shadow.fill(
            reward_shadow_color,
            special_flags=pygame.BLEND_RGB_MULT
        )

        screen.blit(
            money_shadow,
            (money_rect.x + 3, money_rect.y + 4)
        )
        screen.blit(money_text, money_rect)


        # =====================================================
        # POZIOM + PASEK EXP + STATYSTYKI
        # =====================================================

        player_lvl = int(save_data.get("lvl", 1))
        player_exp = int(save_data.get("exp", 0))
        player_max_exp = max(1, int(save_data.get("max_exp", 100)))

        points_to_give = int(save_data.get("stats_points_to_give", 0))

        health_and_def_stats = int(
            save_data.get("health_and_def_stats", 0)
        )
        energy_stats = int(save_data.get("energy_stats", 0))
        dmg_and_forget_resistance_stats = int(
            save_data.get("dmg_and_forget_resistance_stats", 0)
        )
        combo_stats = int(save_data.get("combo_stats", 0))

        center_left = int(screen_width / 3)
        center_right = int(screen_width * 2 / 3)
        center_x = (center_left + center_right) // 2
        center_width = center_right - center_left

        # Przesunięcie całego bloku w górę,
        # żeby zmieściły się punkty i obie linijki statystyk.
        level_section_y = int(screen_height * 0.80)

        level_font = pygame.font.Font(None, 46)
        exp_font = pygame.font.Font(None, 30)
        points_font = pygame.font.Font(None, 38)
        stat_font = pygame.font.Font(None, 32)
        plus_font = pygame.font.Font(None, 38)

        level_color = (255, 215, 100)
        exp_color = (255, 245, 220)
        points_color = (255, 225, 155)
        stat_color = (255, 235, 200)

        exp_bar_bg = (45, 30, 25)
        exp_bar_border = (190, 145, 75)
        exp_bar_fill = (70, 190, 100)
        text_shadow_color = (30, 20, 15)

        # =====================================================
        # 1. POZIOM GRACZA
        # =====================================================

        level_text = level_font.render(
            f"Lvl: {player_lvl}",
            True,
            level_color
        )

        level_rect = level_text.get_rect(
            midtop=(center_x, level_section_y)
        )

        level_shadow = level_text.copy()
        level_shadow.fill(
            text_shadow_color,
            special_flags=pygame.BLEND_RGB_MULT
        )

        screen.blit(
            level_shadow,
            (level_rect.x + 2, level_rect.y + 3)
        )
        screen.blit(level_text, level_rect)

        # =====================================================
        # 2. PASEK EXP
        # =====================================================

        bar_width = int(center_width * 0.72)
        bar_height = 27

        bar_x = center_x - bar_width // 2
        bar_y = level_rect.bottom + 10

        pygame.draw.rect(
            screen,
            exp_bar_bg,
            (bar_x, bar_y, bar_width, bar_height),
            border_radius=8
        )

        exp_progress = max(
            0,
            min(1, player_exp / player_max_exp)
        )

        filled_width = int((bar_width - 4) * exp_progress)

        if filled_width > 0:
            pygame.draw.rect(
                screen,
                exp_bar_fill,
                (
                    bar_x + 2,
                    bar_y + 2,
                    filled_width,
                    bar_height - 4
                ),
                border_radius=6
            )

        pygame.draw.rect(
            screen,
            exp_bar_border,
            (bar_x, bar_y, bar_width, bar_height),
            width=2,
            border_radius=8
        )

        exp_text = exp_font.render(
            f"{player_exp} / {player_max_exp}",
            True,
            exp_color
        )

        exp_rect = exp_text.get_rect(
            center=(center_x, bar_y + bar_height // 2)
        )

        exp_shadow = exp_text.copy()
        exp_shadow.fill(
            text_shadow_color,
            special_flags=pygame.BLEND_RGB_MULT
        )

        screen.blit(
            exp_shadow,
            (exp_rect.x + 1, exp_rect.y + 2)
        )
        screen.blit(exp_text, exp_rect)

        # =====================================================
        # 3. POINTS TO GIVE
        # =====================================================

        points_y = bar_y + bar_height + 12

        points_text = points_font.render(
            f"Points to give: {points_to_give}",
            True,
            points_color
        )

        points_rect = points_text.get_rect(
            center=(center_x, points_y + points_text.get_height() // 2)
        )

        points_shadow = points_text.copy()
        points_shadow.fill(
            text_shadow_color,
            special_flags=pygame.BLEND_RGB_MULT
        )

        screen.blit(
            points_shadow,
            (points_rect.x + 2, points_rect.y + 3)
        )
        screen.blit(points_text, points_rect)

        # =====================================================
        # 4. FUNKCJA RYSOWANIA PRZYCISKU +
        # =====================================================

        plus_size = 34

        def draw_stat_plus(center_button_x, center_button_y):
            base_rect = pygame.Rect(
                int(center_button_x - plus_size // 2),
                int(center_button_y - plus_size // 2),
                plus_size,
                plus_size
            )
            # Przycisk + delikatnie powiększa się po najechaniu.
            hovered = base_rect.collidepoint(pygame.mouse.get_pos())
            button_rect = base_rect.inflate(12, 12) if hovered else base_rect

            # Cień przycisku
            pygame.draw.rect(
                screen,
                (40, 22, 13),
                button_rect.move(2, 3),
                border_radius=7
            )

            # Tło
            pygame.draw.rect(
                screen,
                (105, 65, 32),
                button_rect,
                border_radius=7
            )

            # Złota ramka
            pygame.draw.rect(
                screen,
                (225, 180, 95),
                button_rect,
                width=2,
                border_radius=7
            )

            # Znak +
            plus_text = plus_font.render(
                "+",
                True,
                (255, 240, 190)
            )

            plus_rect = plus_text.get_rect(
                center=button_rect.center
            )

            screen.blit(plus_text, plus_rect)

            return button_rect

        # =====================================================
        # 5. IKONA SERCA — HEALTH / DEFENSE
        # =====================================================

        def draw_heart_icon(cx, cy):
            points = [
                (cx, cy + 12),
                (cx - 15, cy - 1),
                (cx - 15, cy - 8),
                (cx - 10, cy - 13),
                (cx - 4, cy - 13),
                (cx, cy - 7),
                (cx + 4, cy - 13),
                (cx + 10, cy - 13),
                (cx + 15, cy - 8),
                (cx + 15, cy - 1)
            ]

            pygame.draw.polygon(
                screen,
                (100, 15, 25),
                [(x + 2, y + 2) for x, y in points]
            )

            pygame.draw.polygon(
                screen,
                (220, 40, 55),
                points
            )

            pygame.draw.lines(
                screen,
                (255, 135, 135),
                False,
                points[2:6],
                2
            )

        # =====================================================
        # 6. IKONA ENERGII — BŁYSKAWICA
        # =====================================================

        def draw_energy_icon(cx, cy):
            points = [
                (cx + 3, cy - 16),
                (cx - 11, cy + 2),
                (cx - 2, cy + 2),
                (cx - 5, cy + 16),
                (cx + 12, cy - 5),
                (cx + 3, cy - 5)
            ]

            pygame.draw.polygon(
                screen,
                (90, 65, 15),
                [(x + 2, y + 2) for x, y in points]
            )

            pygame.draw.polygon(
                screen,
                (255, 210, 45),
                points
            )

            pygame.draw.polygon(
                screen,
                (255, 245, 155),
                points,
                2
            )

        # =====================================================
        # 7. IKONA PIĘŚCI — DAMAGE
        # =====================================================

        def draw_fist_icon(cx, cy):
            fist_color = (205, 145, 95)
            outline_color = (75, 38, 24)
            highlight_color = (245, 190, 135)

            # Dłoń
            pygame.draw.rect(
                screen,
                outline_color,
                (cx - 13, cy - 4, 25, 17),
                border_radius=5
            )

            pygame.draw.rect(
                screen,
                fist_color,
                (cx - 11, cy - 5, 22, 15),
                border_radius=4
            )

            # Palce
            for i in range(4):
                finger_x = cx - 11 + i * 6

                pygame.draw.rect(
                    screen,
                    outline_color,
                    (finger_x, cy - 13, 8, 13),
                    border_radius=3
                )

                pygame.draw.rect(
                    screen,
                    fist_color,
                    (finger_x + 1, cy - 12, 6, 11),
                    border_radius=2
                )

            # Kciuk
            pygame.draw.rect(
                screen,
                outline_color,
                (cx + 5, cy - 1, 11, 8),
                border_radius=3
            )

            pygame.draw.rect(
                screen,
                fist_color,
                (cx + 5, cy, 9, 6),
                border_radius=2
            )

            # Jasne linie na palcach
            for i in range(3):
                pygame.draw.line(
                    screen,
                    highlight_color,
                    (cx - 7 + i * 6, cy - 9),
                    (cx - 4 + i * 6, cy - 9),
                    1
                )

        # =====================================================
        # 8. IKONA COMBO — TRZY FIOLETOWE STRZAŁKI W GÓRĘ
        # =====================================================

        def draw_combo_icon(cx, cy):
            arrow_color = (175, 75, 255)
            arrow_outline = (70, 25, 110)
            arrow_highlight = (220, 165, 255)

            for offset_x in (-10, 0, 10):
                points = [
                    (cx + offset_x, cy - 13),
                    (cx + offset_x - 5, cy - 5),
                    (cx + offset_x - 2, cy - 5),
                    (cx + offset_x - 2, cy + 10),
                    (cx + offset_x + 2, cy + 10),
                    (cx + offset_x + 2, cy - 5),
                    (cx + offset_x + 5, cy - 5)
                ]

                pygame.draw.polygon(
                    screen,
                    arrow_outline,
                    points
                )

                inner_points = [
                    (cx + offset_x, cy - 11),
                    (cx + offset_x - 3, cy - 6),
                    (cx + offset_x - 1, cy - 6),
                    (cx + offset_x - 1, cy + 8),
                    (cx + offset_x + 1, cy + 8),
                    (cx + offset_x + 1, cy - 6),
                    (cx + offset_x + 3, cy - 6)
                ]

                pygame.draw.polygon(
                    screen,
                    arrow_color,
                    inner_points
                )

                pygame.draw.line(
                    screen,
                    arrow_highlight,
                    (cx + offset_x, cy - 9),
                    (cx + offset_x, cy - 3),
                    1
                )

        # =====================================================
        # 9. FUNKCJA RYSUJĄCA POJEDYNCZĄ STATYSTYKĘ
        # =====================================================

        stat_row_1_y = points_rect.bottom + 22
        stat_row_2_y = stat_row_1_y + 48

        # Środki lewej i prawej połowy środkowej kolumny
        left_stat_x = int(center_left + center_width * 0.25)
        right_stat_x = int(center_left + center_width * 0.75)


        def draw_stat_entry(
            stat_center_x,
            stat_center_y,
            stat_level,
            icon_function,
            description
        ):
            # Poziom statystyki
            stat_text = stat_font.render(
                f"Lvl: {stat_level}",
                True,
                stat_color
            )

            stat_rect = stat_text.get_rect(
                midright=(stat_center_x - 28, stat_center_y)
            )

            stat_shadow = stat_text.copy()
            stat_shadow.fill(
                text_shadow_color,
                special_flags=pygame.BLEND_RGB_MULT
            )

            screen.blit(
                stat_shadow,
                (stat_rect.x + 2, stat_rect.y + 2)
            )
            screen.blit(stat_text, stat_rect)

            # Przycisk +
            plus_center_x = stat_center_x + 2

            plus_rect = draw_stat_plus(
                plus_center_x,
                stat_center_y
            )

            # Ikona statystyki
            icon_center_x = plus_rect.right + 19

            icon_function(
                icon_center_x,
                stat_center_y
            )

            # Mały tekst pod ikoną
            # Mały tekst po prawej stronie ikony
            description_font = pygame.font.Font(None, 25)

            description_text = description_font.render(
                description,
                True,
                (255, 225, 170)
            )

            description_rect = description_text.get_rect(
                midleft=(
                    icon_center_x + 17,
                    stat_center_y
                )
            )

            screen.blit(
                description_text,
                description_rect
            )

            return plus_rect

        self.health_plus_rect = draw_stat_entry(
            left_stat_x,
            stat_row_1_y,
            health_and_def_stats,
            draw_heart_icon,
            "Health / Defense"
        )

        self.energy_plus_rect = draw_stat_entry(
            right_stat_x,
            stat_row_1_y,
            energy_stats,
            draw_energy_icon,
            "Energy"
        )

        self.damage_plus_rect = draw_stat_entry(
            left_stat_x,
            stat_row_2_y,
            dmg_and_forget_resistance_stats,
            draw_fist_icon,
            "Damage"
        )

        self.combo_plus_rect = draw_stat_entry(
            right_stat_x,
            stat_row_2_y,
            combo_stats,
            draw_combo_icon,
            "Combo"
        )

        # =====================================================
        # 12. CIENIOWANIE BRZEGÓW — NA SAMYM KOŃCU
        # =====================================================

        screen.blit(vignette, (0, 0))

        Player.set_position(settings.WIDTH // 2, settings.HEIGHT // 2)
        Player.draw(screen, 2)

        # =====================================================
        # BRĄZOWE, NIEKLIKALNE PRZYCISKI W EKWIPUNKU
        # =====================================================

        import pygame

        # Wymiary środkowej sekcji — dopasuj do swojego panelu
        middle_width = 600
        middle_height = 650

        middle_x = settings.WIDTH // 2 - middle_width // 2
        middle_y = settings.HEIGHT // 2 - middle_height // 2

        # Wygląd przycisków
        slot_size = 115
        slot_gap = 55

        slot_color = (126, 78, 43)
        slot_border = (65, 39, 23)
        slot_highlight = (164, 111, 68)
        slot_shadow = (76, 45, 26)

        # Odstęp przycisków od ścian sekcji
        wall_padding = 14

        # =====================================================
        # LEWA STRONA — 3 PRZYCISKI
        # =====================================================

        left_slots = []

        left_total_height = 3 * slot_size + 2 * slot_gap
        left_start_y = middle_y + (middle_height - left_total_height) // 2 + 12

        for i in range(3):
            slot_x = middle_x - slot_size - (-25)
            slot_y = left_start_y + i * (slot_size + slot_gap)

            left_slots.append(
                pygame.Rect(slot_x, slot_y, slot_size, slot_size)
            )

        # =====================================================
        # PRAWA STRONA — 4 PRZYCISKI
        # =====================================================

        right_slots = []

        right_total_height = 4 * slot_size + 3 * slot_gap
        right_start_y = middle_y + (middle_height - right_total_height) // 2 + 12

        for i in range(4):
            slot_x = middle_x + middle_width + (-25)
            slot_y = right_start_y + i * (slot_size + slot_gap)

            right_slots.append(
                pygame.Rect(slot_x, slot_y, slot_size, slot_size)
            )

        # =====================================================
        # RYSOWANIE PRZYCISKÓW
        # =====================================================

        mouse_pos = pygame.mouse.get_pos()
        hovered_inventory_slots = []

        for slot in left_slots + right_slots:
            # Powiększenie slotu pod kursorem bez przesuwania jego środka.
            hovered = slot.collidepoint(mouse_pos)
            draw_slot = slot.inflate(14, 14) if hovered else slot
            hovered_inventory_slots.append(draw_slot)

            # Cień pod przyciskiem
            shadow_rect = draw_slot.move(3, 4)
            pygame.draw.rect(
                screen,
                slot_shadow,
                shadow_rect,
                border_radius=12 if hovered else 10
            )

            # Główne brązowe tło
            pygame.draw.rect(
                screen,
                slot_highlight if hovered else slot_color,
                draw_slot,
                border_radius=12 if hovered else 10
            )

            # Ciemna obwódka
            pygame.draw.rect(
                screen,
                slot_border,
                draw_slot,
                width=4 if hovered else 3,
                border_radius=12 if hovered else 10
            )

            # Delikatne rozjaśnienie górnej krawędzi
            pygame.draw.line(
                screen,
                (205, 151, 99) if hovered else slot_highlight,
                (draw_slot.x + 10, draw_slot.y + 4),
                (draw_slot.right - 10, draw_slot.y + 4),
                3 if hovered else 2
            )

        # =====================================================
        # IKONY PRZYCISKÓW EKWIPUNKU
        # 1. Koszulka  2. Mikstura  3. Jabłko
        # 4. Miecz     5. Kusza     6. Spodnie  7. Pies
        # =====================================================

        import pygame
        import math

        def draw_inventory_icon(screen, slot, icon_type):
            # Środek przycisku
            cx, cy = slot.center

            # Skala ikony względem przycisku
            s = slot.width / 100

            def p(x, y):
                return (int(cx + x * s), int(cy + y * s))

            def polygon(color, points):
                pygame.draw.polygon(screen, color, [p(x, y) for x, y in points])

            def line(color, start, end, width=3):
                pygame.draw.line(
                    screen, color, p(*start), p(*end),
                    max(1, int(width * s))
                )

            def circle(color, x, y, radius):
                pygame.draw.circle(
                    screen, color, p(x, y), max(1, int(radius * s))
                )

            # =====================================================
            # 1. KOSZULKA — FANTASY ARMOR
            # =====================================================
            if icon_type == "shirt":
                # Metalowe naramienniki
                polygon((105, 112, 125), [
                    (-14, -29), (-30, -23), (-38, -10),
                    (-29, 0), (-17, -7)
                ])
                polygon((105, 112, 125), [
                    (14, -29), (30, -23), (38, -10),
                    (29, 0), (17, -7)
                ])

                # Główny napierśnik
                polygon((65, 75, 91), [
                    (-14, -29), (-24, -24), (-29, -9),
                    (-20, 0), (-17, 25), (17, 25),
                    (20, 0), (29, -9), (24, -24),
                    (14, -29), (8, -18), (-8, -18)
                ])

                # Metaliczne panele
                polygon((112, 124, 143), [
                    (-13, -19), (13, -19), (18, -5),
                    (13, 18), (-13, 18), (-18, -5)
                ])
                polygon((151, 161, 174), [
                    (-7, -15), (7, -15), (10, -3),
                    (6, 13), (-6, 13), (-10, -3)
                ])

                # Złote ozdoby
                line((224, 180, 83), (-22, -9), (-16, 0), 3)
                line((224, 180, 83), (22, -9), (16, 0), 3)
                line((224, 180, 83), (0, -13), (0, 17), 3)

                # Pas z klamrą
                polygon((73, 43, 29), [
                    (-18, 13), (18, 13), (18, 20), (-18, 20)
                ])
                pygame.draw.rect(
                    screen, (235, 190, 75),
                    pygame.Rect(
                        int(cx - 5 * s), int(cy + 13 * s),
                        max(1, int(10 * s)), max(1, int(7 * s))
                    ),
                    max(1, int(2 * s))
                )

                # Obrys pancerza
                polygon((39, 45, 58), [
                    (-14, -29), (-24, -24), (-29, -9),
                    (-20, 0), (-17, 25), (17, 25),
                    (20, 0), (29, -9), (24, -24),
                    (14, -29), (8, -18), (-8, -18)
                ])
                # Ponowne narysowanie metalowego wnętrza
                polygon((112, 124, 143), [
                    (-12, -17), (12, -17), (16, -4),
                    (12, 15), (-12, 15), (-16, -4)
                ])
                line((224, 180, 83), (0, -13), (0, 15), 3)



            # -------------------------------------------------
            # 2. MIKSTURA — STYL MINECRAFT
            # -------------------------------------------------
            elif icon_type == "potion":
                # Korek
                pygame.draw.rect(
                    screen, (105, 63, 34),
                    pygame.Rect(
                        int(cx - 9 * s), int(cy - 34 * s),
                        max(1, int(18 * s)), max(1, int(10 * s))
                    ),
                    border_radius=max(1, int(2 * s))
                )
                pygame.draw.rect(
                    screen, (207, 164, 91),
                    pygame.Rect(
                        int(cx - 11 * s), int(cy - 24 * s),
                        max(1, int(22 * s)), max(1, int(8 * s))
                    )
                )

                # Szklana butelka
                polygon((188, 218, 225), [
                    (-11, -16), (11, -16), (11, -5),
                    (23, 7), (23, 25), (17, 31),
                    (-17, 31), (-23, 25), (-23, 7),
                    (-11, -5)
                ])
                polygon((65, 100, 220), [
                    (-17, 10), (17, 10), (17, 24),
                    (12, 27), (-12, 27), (-17, 24)
                ])
                polygon((112, 156, 255), [
                    (-8, -12), (-3, -12), (-3, 3), (-8, 3)
                ])
                line((235, 240, 255), (-15, 6), (-15, 19), 3)

            # -------------------------------------------------
            # 3. JABŁKO
            # -------------------------------------------------
            elif icon_type == "apple":
                polygon((190, 35, 35), [
                    (-2, -14), (-15, -24), (-28, -16),
                    (-32, -2), (-27, 15), (-13, 27),
                    (0, 25), (13, 27), (27, 15),
                    (32, -2), (28, -16), (15, -24),
                    (2, -14)
                ])
                line((89, 52, 27), (0, -16), (3, -31), 5)
                polygon((54, 151, 62), [
                    (2, -25), (15, -34), (28, -30),
                    (19, -20), (8, -19)
                ])
                circle((255, 110, 85), -15, -8, 5)

            # -------------------------------------------------
            # 4. MIECZ
            # -------------------------------------------------
            elif icon_type == "sword":
                polygon((205, 218, 225), [
                    (-3, -35), (5, -28), (5, 12),
                    (0, 22), (-5, 12), (-5, -28)
                ])
                polygon((115, 125, 139), [
                    (-3, -35), (0, -42), (5, -28), (-3, -25)
                ])
                line((224, 174, 75), (-15, 7), (15, -1), 5)
                line((107, 65, 35), (0, 15), (0, 31), 7)
                circle((230, 180, 80), 0, 33, 5)

            # =====================================================
            # 5. ŁUK — PRZESUNIĘTY W PRAWO, STRZAŁA W LEWO
            # =====================================================
            elif icon_type == "crossbow":

                # Przesunięcie łuku w prawo
                bow_x = 10

                def bp(x, y):
                    return p(x + bow_x, y)

                # Drewniane ramiona łuku
                pygame.draw.arc(
                    screen,
                    (103, 57, 29),
                    pygame.Rect(
                        int(cx + (bow_x - 34) * s),
                        int(cy - 37 * s),
                        max(1, int(57 * s)),
                        max(1, int(74 * s))
                    ),
                    math.radians(65),
                    math.radians(295),
                    max(2, int(6 * s))
                )

                # Jasna krawędź drewna
                pygame.draw.arc(
                    screen,
                    (184, 119, 58),
                    pygame.Rect(
                        int(cx + (bow_x - 30) * s),
                        int(cy - 32 * s),
                        max(1, int(48 * s)),
                        max(1, int(64 * s))
                    ),
                    math.radians(65),
                    math.radians(295),
                    max(1, int(2 * s))
                )

                # Cięciwa
                line((225, 220, 202), (bow_x - 8, -35), (bow_x - 8, 35), 2)

                # Uchwyt
                line((70, 39, 24), (bow_x - 8, -8), (bow_x - 8, 9), 8)
                line((218, 173, 91), (bow_x - 11, -5), (bow_x - 5, -1), 2)
                line((218, 173, 91), (bow_x - 11, 2), (bow_x - 5, 6), 2)

                # Strzała pozioma, skierowana w LEWO
                line(
                    (220, 220, 215),
                    (bow_x + 25, 0),
                    (bow_x - 29, 0),
                    3
                )

                # Grot skierowany w lewo
                polygon((190, 199, 207), [
                    (bow_x - 38, 0),
                    (bow_x - 26, -6),
                    (bow_x - 28, 0),
                    (bow_x - 26, 6)
                ])

                # Pióra na końcu strzały
                polygon((170, 45, 42), [
                    (bow_x + 22, 0),
                    (bow_x + 30, -7),
                    (bow_x + 27, 0)
                ])
                polygon((170, 45, 42), [
                    (bow_x + 22, 0),
                    (bow_x + 30, 7),
                    (bow_x + 27, 0)
                ])

                # Złote zakończenia łuku
                circle((230, 184, 80), bow_x - 8, -35, 3)
                circle((230, 184, 80), bow_x - 8, 35, 3)

            # =====================================================
            # 6. SPODNIE — FANTASY LEG ARMOR
            # =====================================================
            elif icon_type == "pants":
                # Ciemna sylwetka spodni
                polygon((42, 47, 64), [
                    (-21, -28), (21, -28), (20, -10),
                    (16, 29), (2, 29), (0, 3),
                    (-3, 29), (-17, 29), (-20, -10)
                ])

                # Metalowe płyty na udach
                polygon((106, 119, 139), [
                    (-19, -17), (-3, -17), (-4, 0),
                    (-17, 3), (-20, -5)
                ])
                polygon((106, 119, 139), [
                    (3, -17), (19, -17), (20, -5),
                    (17, 3), (4, 0)
                ])

                # Panele kolanowe
                polygon((150, 159, 174), [
                    (-17, 3), (-4, 1), (-4, 12),
                    (-16, 14)
                ])
                polygon((150, 159, 174), [
                    (4, 1), (17, 3), (16, 14),
                    (4, 12)
                ])

                # Pasy skórzane
                line((103, 66, 35), (-20, -9), (20, -9), 4)
                line((103, 66, 35), (-18, 17), (-5, 17), 3)
                line((103, 66, 35), (5, 17), (18, 17), 3)

                # Złote klamry
                circle((231, 183, 76), -11, -9, 3)
                circle((231, 183, 76), 11, -9, 3)

                # Metaliczne krawędzie
                line((185, 192, 205), (-19, -15), (-16, -2), 2)
                line((185, 192, 205), (19, -15), (16, -2), 2)
                line((185, 192, 205), (-14, 26), (-5, 26), 2)
                line((185, 192, 205), (5, 26), (14, 26), 2)


            # =====================================================
            # 7. MAGICZNY SMOK — PET RPG
            # =====================================================
            elif icon_type == "dog":

                # Skrzydło z tyłu
                polygon((76, 73, 151), [
                    (5, -10), (18, -32), (30, -27),
                    (25, -13), (35, -17), (29, 1),
                    (17, 8)
                ])

                # Błona skrzydła
                polygon((125, 92, 203), [
                    (9, -12), (18, -29), (24, -16),
                    (29, -17), (23, 0), (15, 5)
                ])

                # Ogon smoka
                polygon((81, 53, 151), [
                    (17, 8), (30, 1), (37, -7),
                    (35, 5), (25, 16), (15, 14)
                ])

                # Tułów
                pygame.draw.ellipse(
                    screen,
                    (112, 75, 190),
                    pygame.Rect(
                        int(cx - 12 * s),
                        int(cy - 5 * s),
                        max(1, int(34 * s)),
                        max(1, int(25 * s))
                    )
                )

                # Brzuch
                pygame.draw.ellipse(
                    screen,
                    (190, 147, 226),
                    pygame.Rect(
                        int(cx - 4 * s),
                        int(cy + 3 * s),
                        max(1, int(21 * s)),
                        max(1, int(15 * s))
                    )
                )

                # Łapy
                for leg_x in (-7, 7, 17):
                    line(
                        (91, 57, 150),
                        (leg_x, 11),
                        (leg_x - 2, 22),
                        5
                    )
                    circle((220, 193, 246), leg_x - 2, 22, 3)

                # Szyja
                polygon((130, 90, 207), [
                    (-13, -8), (-7, -20), (7, -19),
                    (12, -5), (5, 7), (-8, 5)
                ])

                # Głowa
                pygame.draw.ellipse(
                    screen,
                    (145, 103, 215),
                    pygame.Rect(
                        int(cx - 24 * s),
                        int(cy - 31 * s),
                        max(1, int(34 * s)),
                        max(1, int(28 * s))
                    )
                )

                # Pysk
                polygon((177, 135, 226), [
                    (-23, -20), (-34, -16), (-32, -8),
                    (-22, -6), (-15, -12)
                ])

                # Rogi
                polygon((245, 219, 151), [
                    (-18, -27), (-22, -39), (-10, -29)
                ])
                polygon((245, 219, 151), [
                    (-4, -29), (2, -40), (5, -25)
                ])

                # Oko
                circle((255, 218, 77), -17, -20, 4)
                circle((37, 25, 45), -18, -20, 2)

                # Nozdrze
                circle((75, 43, 115), -30, -13, 2)

                # Małe zęby
                polygon((245, 239, 255), [
                    (-28, -7), (-23, -7), (-25, -2)
                ])

                # Kolce na grzbiecie
                polygon((238, 187, 255), [
                    (-6, -8), (-3, -17), (1, -7)
                ])
                polygon((238, 187, 255), [
                    (2, -6), (6, -15), (9, -4)
                ])

                # Magiczna obroża
                line((255, 190, 70), (-12, -2), (-5, 3), 3)
                circle((98, 238, 255), -9, 4, 3)

        # =====================================================
        # RYSOWANIE 7 IKON NA PRZYCISKACH
        # =====================================================

        inventory_icons = [
            "shirt",
            "potion",
            "apple",
            "sword",
            "crossbow",
            "pants",
            "dog"
        ]

        all_slots = left_slots + right_slots

        for slot, icon_type in zip(all_slots, inventory_icons):
            icon_slot = slot.inflate(8, 8) if slot.collidepoint(mouse_pos) else slot
            draw_inventory_icon(screen, icon_slot, icon_type)

        # =====================================================
        # PRZEDMIOTY W 6 PODPISANYCH SEKCJACH
        # UI TYLKO ODCZYTUJE LISTY I WYWOŁUJE draw_icon()
        # Slot oraz grafika przedmiotu są rysowane w odpowiednim module.
        # =====================================================

        inventory_sections = [
            {
                "title": "Armor:",
                "keys": ("up_armors_in_eq", "down_armors_in_eq"),
                "module": globals().get("armors"),
                "column": "left",
                "index": 0,
                "extra_y": 50
            },
            {
                "title": "Utility:",
                "keys": ("utilies_in_eq",),
                "module": utilities,
                "column": "left",
                "index": 1,
                "extra_y": 15
            },
            {
                "title": "Fruits:",
                "keys": ("fruits_in_eq",),
                "module": fruits,
                "column": "left",
                "index": 2,
                "extra_y": 0
            },
            {
                "title": "Swords:",
                "keys": ("swords_in_eq",),
                "module": swords,
                "column": "right",
                "index": 0,
                "extra_y": 50
            },
            {
                "title": "Guns:",
                "keys": ("guns_in_eq",),
                "module": guns,
                "column": "right",
                "index": 1,
                "extra_y": 0
            },
            {
                "title": "Pets:",
                "keys": ("pets_in_eq",),
                "module": globals().get("pets"),
                "column": "right",
                "index": 2,
                "extra_y": 0
            }
        ]

        section_font = pygame.font.Font(None, 39)
        empty_font = pygame.font.Font(None, 60)
        item_text_color = (255, 232, 190)
        item_shadow_color = (35, 18, 10)

        # Większe sloty i odstępy.
        item_slot_size = 124
        item_slot_gap = 18
        item_row_gap = 42
        item_stride_y = item_slot_size + item_row_gap

        # Każda z 6 sekcji ma osobny przewijany obszar.
        if not hasattr(self, "inventory_scroll_offsets"):
            self.inventory_scroll_offsets = {}
        self.inventory_section_viewports = {}
        self.inventory_section_max_scroll = {}
        
        def get_inventory_item_name(item):
            if isinstance(item, dict):
                return str(item.get("name") or item.get("item") or item.get("type") or "Item")
            if hasattr(item, "name"):
                return str(item.name)
            return str(item)

        def find_inventory_item_object(module, item_name):
            if module is None:
                return None
            wanted_name = str(item_name).strip().casefold()
            for value in vars(module).values():
                if not isinstance(value, type):
                    continue
                try:
                    item_object = value()
                except Exception:
                    continue
                class_name = value.__name__.strip().casefold()
                object_name = str(getattr(item_object, "name", "")).strip().casefold()
                if wanted_name in (class_name, object_name):
                    return item_object
            return None

        for section_index, section in enumerate(inventory_sections):
            section_items = []
            for key in section["keys"]:
                values = save_data.get(key, [])
                if isinstance(values, (list, tuple)):
                    section_items.extend(values)
                elif values:
                    section_items.append(values)

            column_center_x = column_width / 2 if section["column"] == "left" else column_width * 2.5
            section_top = int(section_height * section["index"])
            section_bottom = int(section_height * (section["index"] + 1))

            # Przewijany obszar wewnątrz konkretnej sekcji.
            content_top = int(section_top + 112 + section["extra_y"])
            viewport_bottom = int(section_bottom - 14)
            viewport = pygame.Rect(
                int(column_center_x - column_width / 2 + 20),
                content_top,
                int(column_width - 40),
                max(1, viewport_bottom - content_top)
            )

            self.inventory_section_viewports[section_index] = viewport

            if not section_items:
                empty_y = int(section_top + section_height * 0.50 + section["extra_y"] * 0.25)
                empty_text = empty_font.render("Empty", True, (218, 190, 151))
                empty_rect = empty_text.get_rect(center=(int(column_center_x), empty_y))
                empty_shadow = empty_text.copy()
                empty_shadow.fill(item_shadow_color, special_flags=pygame.BLEND_RGB_MULT)
                screen.blit(empty_shadow, (empty_rect.x + 2, empty_rect.y + 3))
                screen.blit(empty_text, empty_rect)
                self.inventory_scroll_offsets[section_index] = 0
                continue

            available_width = int(column_width - 70)
            items_per_row = max(1, min(5, (available_width + item_slot_gap) // (item_slot_size + item_slot_gap)))
            total_rows = (len(section_items) + items_per_row - 1) // items_per_row
            content_height = total_rows * item_stride_y
            # Przewijanie pojawia się, gdy zawartość nie mieści się w sekcji.
            # Uwzględnij również miejsce na podpis ostatniego przedmiotu.
            content_height = total_rows * item_stride_y + 34
            max_scroll = max(0, content_height - viewport.height)
            self.inventory_section_max_scroll[section_index] = max_scroll
            scroll_offset = max(0, min(self.inventory_scroll_offsets.get(section_index, 0), max_scroll))
            self.inventory_scroll_offsets[section_index] = scroll_offset

            previous_clip = screen.get_clip()
            screen.set_clip(viewport.clip(previous_clip))

            for item_index, item in enumerate(section_items):
                row_index = item_index // items_per_row
                column_index = item_index % items_per_row
                items_in_this_row = min(items_per_row, len(section_items) - row_index * items_per_row)
                row_width = items_in_this_row * item_slot_size + (items_in_this_row - 1) * item_slot_gap
                row_start_x = int(column_center_x - row_width / 2)
                slot_x = row_start_x + column_index * (item_slot_size + item_slot_gap)
                slot_y = content_top + row_index * item_stride_y - scroll_offset
                slot_center_x = slot_x + item_slot_size // 2
                slot_center_y = slot_y + item_slot_size // 2

                # Pomiń rysowanie obiektów, które są poza widocznym fragmentem.
                if slot_y + item_slot_size + 35 < viewport.top or slot_y > viewport.bottom:
                    continue

                item_name = get_inventory_item_name(item)
                item_object = find_inventory_item_object(section["module"], item_name)

                # Przedmiot nie rysuje własnej ramki slotu w ekwipunku.
                # Rysujemy ikonę na osobnej powierzchni, odcinamy krawędzie slotu
                # z draw_icon() (swords.py / guns.py), a następnie skalujemy samą ikonę.
                item_hover_rect = pygame.Rect(slot_x, slot_y, item_slot_size, item_slot_size)
                item_hovered = viewport.collidepoint(mouse_pos) and item_hover_rect.collidepoint(mouse_pos)

                draw_icon_method = getattr(item_object, "draw_icon", None) if item_object else None
                if callable(draw_icon_method):
                    try:
                        icon_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
                        try:
                            draw_icon_method(icon_surface, slot_center_x, slot_center_y)
                        except TypeError:
                            # Niektóre klasy mają draw_icon(screen), bez współrzędnych.
                            draw_icon_method(icon_surface)

                        # Zachowaj pełną ikonę razem z jej oryginalną obramówką.
                        # Nie dodawaj drugiej ramki podczas najechania.
                        crop_inset = 0
                        icon_rect = pygame.Rect(
                            slot_center_x - item_slot_size // 2 + crop_inset,
                            slot_center_y - item_slot_size // 2 + crop_inset,
                            item_slot_size - crop_inset * 2,
                            item_slot_size - crop_inset * 2
                        )
                        icon_rect.clamp_ip(icon_surface.get_rect())
                        if icon_rect.width > 0 and icon_rect.height > 0:
                            icon_crop = icon_surface.subsurface(icon_rect).copy()
                            # Delikatne powiększenie po najechaniu; zachowuje obramówkę.
                            # Środek pozostaje w miejscu, a powiększenie jest niewielkie.
                            display_size = int(item_slot_size * (1.10 if item_hovered else 1.0))
                            enlarged_icon = pygame.transform.smoothscale(
                                icon_crop, (display_size, display_size)
                            )
                            if item_hovered:
                                # Lekkie rozjaśnienie zgodne z efektem pozostałych slotów.
                                enlarged_icon.fill((18, 18, 18, 0), special_flags=pygame.BLEND_RGBA_ADD)
                            screen.blit(
                                enlarged_icon,
                                enlarged_icon.get_rect(center=(slot_center_x, slot_center_y))
                            )
                    except Exception as error:
                        print(f"Nie udało się narysować ikony {item_name}: {error}")

                name_surface = section_font.render(item_name, True, item_text_color)
                max_name_width = item_slot_size + 22
                if name_surface.get_width() > max_name_width:
                    scale = max_name_width / name_surface.get_width()
                    name_surface = pygame.transform.smoothscale(
                        name_surface,
                        (max(1, int(name_surface.get_width() * scale)), max(1, int(name_surface.get_height() * scale)))
                    )
                name_rect = name_surface.get_rect(midtop=(slot_center_x, slot_y + item_slot_size + 6))
                name_shadow = name_surface.copy()
                name_shadow.fill(item_shadow_color, special_flags=pygame.BLEND_RGB_MULT)
                screen.blit(name_shadow, (name_rect.x + 2, name_rect.y + 2))
                screen.blit(name_surface, name_rect)

            screen.set_clip(previous_clip)

            # Mały wskaźnik przewijania, gdy lista nie mieści się w sekcji.
            if max_scroll > 0:
                track = pygame.Rect(viewport.right - 7, viewport.top + 3, 4, max(12, viewport.height - 6))
                pygame.draw.rect(screen, (65, 37, 22), track, border_radius=2)
                thumb_height = max(18, int(track.height * viewport.height / max(viewport.height, content_height)))
                thumb_y = track.y + int((track.height - thumb_height) * scroll_offset / max_scroll)
                pygame.draw.rect(screen, (220, 174, 112), (track.x, thumb_y, track.width, thumb_height), border_radius=2)

    def draw_map(self, screen):
        data = save.load_game()

        last_save = data["variables"]["last_save"]

        if last_save not in data["saves"]:
            last_save = "save1"

        save_data = data["saves"][last_save]

        if save_data["quest_doing_rn"] == 1:
            data["saves"][last_save]["quest_doing_rn"] += 1
            data["saves"][last_save]["quests_done"] += 1
            self.give_exp_for_quest()
            save.save_game(data)

        screen.fill((0, 0, 0))

    def handle_stat_click(self, mouse_pos, data):
        last_save = data["variables"]["last_save"]
        save_data = data["saves"][last_save]

        # Brak punktów statystyk
        if save_data.get("stats_points_to_give", 0) <= 0:
            return False

        # Przycisk + -> nazwa statystyki
        stat_buttons = [
            (getattr(self, "health_plus_rect", None), "health_and_def_stats"),
            (getattr(self, "energy_plus_rect", None), "energy_stats"),
            (getattr(self, "damage_plus_rect", None), "dmg_and_forget_resistance_stats"),
            (getattr(self, "combo_plus_rect", None), "combo_stats")
        ]

        # Sprawdź kliknięty przycisk
        for button_rect, stat_name in stat_buttons:
            if (
                    button_rect is not None
                    and button_rect.collidepoint(mouse_pos)
            ):
                current_level = save_data.get(stat_name, 0)

                # Maksymalny poziom statystyki: 100
                if current_level >= 100:
                    return False

                # Zwiększ poziom statystyki
                save_data[stat_name] = current_level + 1

                # ==========================================
                # BONUSY STATYSTYK
                # ==========================================

                if stat_name == "health_and_def_stats":
                    # Każdy punkt Health = +5 MAX HP
                    save_data["max_health"] = (
                            save_data.get("max_health", 100) + 5
                    )

                    if hasattr(self, "max_health"):
                        self.max_health += 5

                elif stat_name == "energy_stats":
                    # Każdy punkt Energy = +5 MAX ENERGY
                    save_data["max_energy"] = (
                            save_data.get("max_energy", 100) + 5
                    )

                    if hasattr(self, "max_energy"):
                        self.max_energy += 5

                # Zużyj jeden punkt statystyk
                save_data["stats_points_to_give"] -= 1

                return True

        return False