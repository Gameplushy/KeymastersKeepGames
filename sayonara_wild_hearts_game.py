from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SayonaraWildHeartsArchipelagoOptions:
    pass


# Main Class
class SayonaraWildHeartsGame(Game):
    name = "Sayonara Wild Hearts"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.IOS
    ]

    is_adult_only_or_unrated = False

    options_cls = SayonaraWildHeartsArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Get all squares",
                data=dict()
            ),
            GameObjectiveTemplate(
                label="Don't die once",
                data=dict()
            )
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Get RANK Rank in LEVEL",
                data={
                    "RANK": (self.ranks, 1),
                    "LEVEL": (self.levels, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=23,
            ),
            GameObjectiveTemplate(
                label="Get RANK Rank in Album Arcade",
                data={
                    "RANK": (self.ranks, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get RANK Rank in Yolo Arcade",
                data={
                    "RANK": (self.ranks, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    def ranks(self) -> List[str]:
        return  [
            "Bronze",
            "Silver",
            "Gold"
        ]
    
    def levels(self) -> List[str]:
        return [
            "Clair De Lune",
            "Heartbreak I",
            "Doki Doki Rush",
            "Fighting Hearts",
            "Begin Again",
            "Heartbreak II",
            "Forest Ghost",
            "Forest Dub",
            "Laser Love",
            "Dead of Night",
            "Heartbreak III",
            "Hearts & Swords",
            "Parallel Universes",
            "Mine",
            "Heartbreak IV",
            "Night Drift",
            "Reverie",
            "The World We Knew",
            "Heartbreak V",
            "Transonic Gravity",
            "Hate Skulls",
            "Inside",
            "Wild Hearts Never Die"
        ]