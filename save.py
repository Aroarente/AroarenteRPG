import json
import os
import hashlib
import base64

from cryptography.fernet import Fernet, InvalidToken


DOWNLOADS = os.path.join(
    os.path.expanduser("~"),
    "Downloads"
)

SAVE_FILE = os.path.join(
    DOWNLOADS,
    "AroarenteRpg_Data.json"
)


# ==========================================
# KLUCZ FERNET
# ==========================================

SECRET_KEY = base64.urlsafe_b64encode(
    hashlib.sha256(
        b"AroarenteRPG_HashKey"
    ).digest()
)

fernet = Fernet(SECRET_KEY)


# ==========================================
# DEFAULT SAVE
# ==========================================

DEFAULT_SAVE = {
    "money": 0,
    "fragments": 0,

    "lvl": 1,
    "exp": 0,
    "max_exp": 100,
    "prestige_lvl": 0,

    "health": 100,
    "max_health": 100,
    "energy": 100,
    "max_energy": 100,

    "stats_points_to_give": 0,
    "health_and_def_stats": 0,
    "dmg_and_forget_resistance_stats": 0,
    "energy_stats": 0,
    "combo_stats": 0,

    "character_name": "",
    "elemental": "",
    "elemental_lvl": 1,
    "difficulty": "",

    "fruits_in_eq": [],
    "current_fruit": "",

    "swords_in_eq": [],
    "current_sword": "",

    "guns_in_eq": [],
    "current_gun": "",

    "current_fighting_style": "",
    "fighting_styles_unlocked": [],

    "up_armors_in_eq": [],
    "current_up_armor": "",

    "down_armors_in_eq": [],
    "current_down_armor": "",

    "utilies_in_eq": [],
    "current_utility": "",

    "quests_done": 0,
    "quest_doing_rn": 0,
    "quest_doing_rn_name": "Watch cutscene",

    "game_progression": 0,

    "current_location_x": 1280,
    "current_location_y": 720,

    "current_world": "Kingdom",

    "worlds_unlocked": [
        "Kingdom"
    ],

    "current_map_on_x": 4,
    "current_map_on_y": 4,

    "cutsceene1_completed": False,
    "npc1_alive": True,
    "npc2_alive": True,
    "npc3_alive": True,
    "npc4_alive": True
}


# ==========================================
# DEFAULT DATA
# ==========================================

DEFAULT_DATA = {
    "saves": {
        "save1": DEFAULT_SAVE.copy(),
        "save2": DEFAULT_SAVE.copy(),
        "save3": DEFAULT_SAVE.copy(),
        "save4": DEFAULT_SAVE.copy()
    },

    "variables": {
        "last_save": "save0",

        "possible_worlds": [
            "Kingdom",
            "Hell",
            "Underwater"
        ],

        "possible_swords": [],
        "possible_guns": [],
        "possible_utilities": [],
        "possible_up_armors": [],
        "possible_down_armors": [],
        "possible_fighting_styles": [],

        "possible_fruits": [
            "Dough"
        ],

        "max_quests": 2,
        "quests_names": ["Watch cutscene", "Open inventory or map for first time", "Kill your first NPC"]
    }
}

# ==========================================
# UPDATE SAVE
# ==========================================

def update_save(data):

    changed = False

    # ======================================
    # GŁÓWNE SEKCJE
    # ======================================

    if "saves" not in data:
        data["saves"] = {}

        for save_number in range(1, 5):
            data["saves"][f"save{save_number}"] = (
                DEFAULT_SAVE.copy()
            )

        changed = True

    if "variables" not in data:
        data["variables"] = {}

        changed = True

    # ======================================
    # SAVE 1-4
    # ======================================

    for save_number in range(1, 5):

        save_name = f"save{save_number}"

        # Brak całego save'a
        if save_name not in data["saves"]:

            data["saves"][save_name] = (
                DEFAULT_SAVE.copy()
            )

            changed = True

        # Brakujące pola w save'ie
        for key, default_value in DEFAULT_SAVE.items():

            if key not in data["saves"][save_name]:

                # Kopiowanie list/danych
                if isinstance(default_value, list):
                    data["saves"][save_name][key] = (
                        default_value.copy()
                    )

                else:
                    data["saves"][save_name][key] = (
                        default_value
                    )

                changed = True

    # ======================================
    # VARIABLES
    # ======================================

    for key, default_value in DEFAULT_DATA["variables"].items():

        if key not in data["variables"]:

            if isinstance(default_value, list):
                data["variables"][key] = (
                    default_value.copy()
                )

            else:
                data["variables"][key] = (
                    default_value
                )

            changed = True

    return data, changed


# ==========================================
# SAVE GAME
# ==========================================

def save_game(data):

    data, _ = update_save(data)

    # ======================================
    # PYTHON DATA -> JSON
    # ======================================

    json_data = json.dumps(
        data,
        ensure_ascii=False,
        indent=4
    ).encode("utf-8")

    # ======================================
    # SZYFROWANIE
    # ======================================

    encrypted_data = fernet.encrypt(
        json_data
    )

    # ======================================
    # ZAPIS
    # ======================================

    os.makedirs(
        DOWNLOADS,
        exist_ok=True
    )

    with open(
        SAVE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            encrypted_data.decode("utf-8"),
            file
        )


# ==========================================
# LOAD GAME
# ==========================================
new_save_done = False

def load_game():
    global new_save_done
    if new_save_done == False:
        set_normal()
    else:
        pass

    # ======================================
    # BRAK SAVE'A
    # ======================================

    if not os.path.exists(SAVE_FILE):

        save_game(DEFAULT_DATA)

        return DEFAULT_DATA.copy()

    try:

        # ==================================
        # ODCZYT
        # ==================================

        with open(
            SAVE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            encrypted_data = json.load(file)

        # ==================================
        # ODSZYFROWANIE
        # ==================================

        json_data = fernet.decrypt(
            encrypted_data.encode("utf-8")
        )

        # ==================================
        # JSON -> PYTHON
        # ==================================

        data = json.loads(
            json_data.decode("utf-8")
        )

    except (
        json.JSONDecodeError,
        OSError,
        InvalidToken,
        ValueError,
        TypeError
    ):

        print(
            "The save has been modified, "
            "is corrupted, or is invalid!"
        )

        return None

    # ======================================
    # AKTUALIZACJA STAREGO SAVE'A
    # ======================================

    data, changed = update_save(data)

    # ======================================
    # ZAPIS PO AKTUALIZACJI
    # ======================================

    if changed:
        save_game(data)

    return data

def set_normal():
    global new_save_done
    new_save_done = True
    data = load_game()

    last_save = data["variables"]["last_save"]

    if last_save not in data["saves"]:
        last_save = "save1"

    data["variables"]["possible_worlds"] = (
        DEFAULT_DATA["variables"]["possible_worlds"].copy()
    )

    data["variables"]["possible_swords"] = (
        DEFAULT_DATA["variables"]["possible_swords"].copy()
    )

    data["variables"]["possible_guns"] = (
        DEFAULT_DATA["variables"]["possible_guns"].copy()
    )

    data["variables"]["possible_utilities"] = (
        DEFAULT_DATA["variables"]["possible_utilities"].copy()
    )

    data["variables"]["possible_up_armors"] = (
        DEFAULT_DATA["variables"]["possible_up_armors"].copy()
    )

    data["variables"]["possible_down_armors"] = (
        DEFAULT_DATA["variables"]["possible_down_armors"].copy()
    )

    data["variables"]["possible_fighting_styles"] = (
        DEFAULT_DATA["variables"]["possible_fighting_styles"].copy()
    )

    data["variables"]["possible_fruits"] = (
        DEFAULT_DATA["variables"]["possible_fruits"].copy()
    )

    data["variables"]["max_quests"] = (
        DEFAULT_DATA["variables"]["max_quests"]
    )

    data["variables"]["quests_names"] = (
        DEFAULT_DATA["variables"]["quests_names"].copy()
    )

    save_game(data)