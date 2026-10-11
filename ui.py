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
import fruits
import elementals
katana = swords.Katana()


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

        # ==========================================
        # DELIKATNE PRZYCIEMNIENIE EKRANU
        # ==========================================

        dark_overlay = pygame.Surface(
            (settings.WIDTH, settings.HEIGHT),
            pygame.SRCALPHA
        )

        dark_overlay.fill((0, 0, 0, 240))

        screen.blit(
            dark_overlay,
            (0, 0)
        )

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
