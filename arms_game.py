from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, Range

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class ArmsArchipelagoOptions:
    arms_play_online: ArmsPlayOnline
    arms_two_only: ArmsTwoOnly
    arms_min_level: ArmsMinLevel
    arms_max_level: ArmsMaxLevel

# Main Class
class ArmsGame(Game):
    name = "ARMS"
    platform = KeymastersKeepGamePlatforms.SW

    is_adult_only_or_unrated = False

    options_cls = ArmsArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        li : List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Win Grand Prix as CHAR at level LEVEL",
                data={
                    "CHAR": (self.characters, 1),
                    "LEVEL": (self.level, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win as CHAR in MODE mode against level LVL OPPONENTS",
                data={
                    "CHAR": (self.characters, 1),
                    "MODE": (self.two_modes, 1),
                    "LVL": (self.level, 1),
                    "OPPONENTS": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win in 1-on-100 as CHAR",
                data={
                    "CHAR": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]

        if(not self.two_only):
            li.extend([
                GameObjectiveTemplate(
                    label="Win as CHAR in MODE mode against level LVL OPPONENTS",
                    data={
                        "CHAR": (self.characters, 1),
                        "MODE": (self.three_modes, 1),
                        "LVL": (self.level, 1),
                        "OPPONENTS": (self.characters, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Win as CHAR in MODE mode against level LVL OPPONENTS",
                    data={
                        "CHAR": (self.characters, 1),
                        "MODE": (self.four_modes, 1),
                        "LVL": (self.level, 1),
                        "OPPONENTS": (self.characters, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            ])

        if(self.play_online):
            li.extend([
                GameObjectiveTemplate(
                    label="Win an online match as CHAR",
                    data={
                        "CHAR": (self.characters, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,                    
                )
            ])

        return li
    

    @staticmethod
    def characters() -> List[str]:
        return [
            "Spring Man",
            "Ribbon Girl",
            "Ninjara",
            "Master Mummy",
            "Min Min",
            "Mechanica",
            "Twintelle",
            "Byte & Barq",
            "Kid Cobra",
            "Helix",
            "Max Brass",
            "Lola Pop",
            "Misango",
            "Springtron",
            "Dr. Coyle"
        ]
    
    @staticmethod
    def two_modes() -> List[str]:
        return [
            "Fight",
            "V-Ball",
            "Hoops",
            "Skilshot",
            "Hedlok Scramble"
        ]
    
    @staticmethod
    def three_modes() -> List[str]:
        return [
            "Fight",
            "Hedlok Scramble"
        ]
    
    @staticmethod
    def four_modes() -> List[str]:
        return [
            "Fight",
            "Team Fight"
            "V-Ball",
            "Skilshot",
            "Hedlok Scramble"
        ]

    @property
    def play_online(self) -> bool:
        return bool(self.archipelago_options.arms_play_online.value)
    
    @property
    def two_only(self) -> bool:
        return bool(self.archipelago_options.arms_two_only.value)
    
    def level(self) -> range:
        return range(int(self.archipelago_options.arms_min_level.value),int(self.archipelago_options.arms_max_level.value) +1)


# Archipelago Options
class ArmsPlayOnline(Toggle):
    """
    Indicates whether you want to play online matches in ARMS.
    """

    display_name = "ARMS Include Online Matches"

class ArmsTwoOnly(DefaultOnToggle):
    """
    Indicates whether you want to remove 3 and 4-player matches objectives in ARMS.
    """

    display_name = "ARMS 1v1 Only Matches"

class ArmsMinLevel(Range):
    """
    Indicates which will the be the minimal level for AIs for ARMS.
    """
    display_name = "ARMS Min AI Level"
    range_start = 1
    range_end = 7
    default = 1

class ArmsMaxLevel(Range):
    """
    Indicates which will the be the maximal level for AIs for ARMS.
    """
    display_name = "ARMS Max AI Level"
    range_start = 1
    range_end = 7
    default = 7